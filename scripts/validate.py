#!/usr/bin/env python3
"""Offline integrity checks for this blueprint, not a provider deployment/security audit."""
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
import urllib.parse
import yaml

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ['Purpose','When needed','Prerequisites','Recommended implementation','Setup','Security considerations','Free-tier limitations','Verification','Troubleshooting','Official documentation']
GUIDES = ['getting-started','website-planning','architecture-selection','github-setup','cloudflare-setup','domain-and-dns','frontend-development','database-options','supabase-setup','authentication','admin-dashboard','api-development','content-management','seo','accessibility','performance','security','testing','deployment','monitoring','maintenance','backup-and-recovery','cost-management','production-checklist','operational-failure-modes']

class UniqueLoader(yaml.SafeLoader):
    pass
# YAML 1.2-style booleans: GitHub's `on` must remain a string, not YAML 1.1 True.
UniqueLoader.yaml_implicit_resolvers = {k:[(tag,pat) for tag,pat in vals if tag != 'tag:yaml.org,2002:bool'] for k,vals in yaml.SafeLoader.yaml_implicit_resolvers.items()}
UniqueLoader.add_implicit_resolver('tag:yaml.org,2002:bool',re.compile(r'^(?:true|false|True|False|TRUE|FALSE)$'),list('tTfF'))
def unique_mapping(loader,node,deep=False):
    result={}
    for keynode,valnode in node.value:
        key=loader.construct_object(keynode,deep=deep)
        if key in result:
            raise ValueError('Duplicate YAML key')
        result[key]=loader.construct_object(valnode,deep=deep)
    return result
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)

def unique_json(pairs):
    out={}
    for key,value in pairs:
        if key in out: raise ValueError('Duplicate JSON key')
        out[key]=value
    return out

def headings(text):
    text=re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S)
    counts=Counter(); ids=set()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',text,re.M):
        base=re.sub(r'[^\w\- ]','',title.lower().replace('`','')).replace(' ','-')
        n=counts[base];counts[base]+=1
        ids.add(base+(f'-{n}' if n else ''))
    return ids

def check_links(root,p,text):
    errors=[]
    stripped=re.sub(r'^```.*?^```[^\n]*','',text,flags=re.M|re.S)
    for dest in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',stripped):
        dest=dest.strip('<>')
        parsed=urllib.parse.urlsplit(dest)
        if parsed.scheme or parsed.netloc:continue
        path=urllib.parse.unquote(parsed.path)
        target=(p.parent/path).resolve() if path else p.resolve()
        if not target.is_relative_to(root.resolve()):errors.append(f'{p.relative_to(root)}: link escapes repository')
        elif not target.exists():errors.append(f'{p.relative_to(root)}: missing link target {dest}')
        elif parsed.fragment and target.suffix=='.md' and urllib.parse.unquote(parsed.fragment) not in headings(target.read_text()):errors.append(f'{p.relative_to(root)}: missing anchor {dest}')
    return errors

def workflow_errors(data,path):
    errors=[]
    if not isinstance(data,dict):return [f'{path}: expected workflow mapping']
    if 'jobs' not in data or 'on' not in data:return [f'{path}: missing workflow on/jobs']
    if data.get('permissions') != {'contents':'read'}:errors.append(f'{path}: expected contents: read only')
    events=data['on']
    if isinstance(events,dict) and 'pull_request_target' in events:errors.append(f'{path}: unsafe PR event')
    for job in data['jobs'].values():
        if not isinstance(job.get('timeout-minutes'),int) or not 1<=job['timeout-minutes']<=15:errors.append(f'{path}: job timeout required, maximum 15')
        if job.get('permissions') and job['permissions'] != {'contents':'read'}:errors.append(f'{path}: job permissions expanded')
        for step in job.get('steps',[]):
            use=step.get('uses','')
            if use and not use.startswith('./') and not re.fullmatch(r'[\w.-]+/[\w./-]+@[0-9a-f]{40}',use):errors.append(f'{path}: action not full-SHA pinned')
            if use.startswith('actions/checkout@') and step.get('with',{}).get('persist-credentials') is not False:errors.append(f'{path}: checkout must not persist credentials')
            if 'upload-artifact@' in use and not 1<=step.get('with',{}).get('retention-days',0)<=7:errors.append(f'{path}: artifact retention must be 1..7')
    return errors

def ref_errors(data):
    errors=[]
    def walk(node):
        if isinstance(node,dict):
            for key,value in node.items():
                if key=='$ref' and isinstance(value,str) and value.startswith('#/'):
                    current=data
                    try:
                        for part in value[2:].split('/'):
                            current=current[part.replace('~1','/').replace('~0','~')]
                    except (KeyError,TypeError):errors.append('Unresolved JSON reference '+value)
                else:walk(value)
        elif isinstance(node,list):
            for item in node:walk(item)
    walk(data);return errors

def run(root=ROOT):
    errors=[]; counts=Counter()
    required=['README.md','AGENTS.md','LICENSE','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','.gitignore','.env.example']
    required+=['prompts/'+n+'.md' for n in ['START-HERE','website-builder','resume-project','security-auditor','deployment-reviewer','maintenance-agent']]
    required+=['planning/'+n+'-template.md' for n in ['requirements','roadmap','progress','decision-log','architecture','handoff','deployment']]
    required+=['docs/'+f'{i:02}-{slug}.md' for i,slug in enumerate(GUIDES,1)]
    required+=['security/'+n+'.md' for n in ['security-baseline','threat-model-template','authentication-security','api-security','cloudflare-security','database-security','dependency-security','incident-response','security-audit-checklist']]
    required+=['automation/'+n+'.md' for n in ['daily-checks','weekly-checks','monthly-checks','dependency-updates','uptime-monitoring']]
    required+=['examples/'+n+'/README.md' for n in ['static-website','business-website','product-catalog','events-calendar','authenticated-app','admin-api']]
    required+=['templates/'+n+'/README.md' for n in ['environment','github','cloudflare','supabase','api','security']]
    for name in required:
        if not (root/name).is_file():errors.append('Missing required file '+name)
    paths=[p for p in root.rglob('*') if p.is_file() and not any(x in p.relative_to(root).parts for x in ('.git','__pycache__','.venv'))]
    for p in paths:
        rel=str(p.relative_to(root));counts['files']+=1
        try:text=p.read_text()
        except UnicodeError:errors.append(rel+': unexpected binary');continue
        if not text.strip():errors.append(rel+': empty file')
        if re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',text):errors.append(rel+': possible hardcoded credential')
        if p.suffix=='.md':
            counts['markdown']+=1;errors.extend(check_links(root,p,text))
            if re.match(r'docs/\d\d-',rel) or rel=='docs/source-freshness.md':
                for section in SECTIONS:
                    # Source freshness intentionally groups purpose/when and implementation/setup.
                    if rel=='docs/source-freshness.md':break
                    if '## '+section+'\n' not in text:errors.append(rel+': missing guide section '+section)
                if len(text.split())<180:errors.append(rel+': guide too sparse')
        if p.suffix=='.json':
            counts['json']+=1
            try:
                data=json.loads(text,object_pairs_hook=unique_json)
                errors.extend(rel+': '+e for e in ref_errors(data))
                if 'openapi' in data:
                    for operations in data['paths'].values():
                        for method,op in operations.items():
                            if method in ('post','patch','delete','put') and not op.get('security'):errors.append(rel+': mutation missing explicit security')
            except Exception as exc:errors.append(rel+': invalid JSON '+str(exc))
        if p.suffix in ('.yml','.yaml'):
            counts['yaml']+=1
            try:
                data=yaml.load(text,Loader=UniqueLoader)
                if 'workflows/' in rel:errors.extend(workflow_errors(data,rel))
                elif p.name=='dependabot.yml' and (data.get('version')!=2 or not data.get('updates')):errors.append(rel+': invalid Dependabot structure')
            except Exception as exc:errors.append(rel+': invalid YAML '+str(exc))
    if (root/'.env.example').exists():
        for line in (root/'.env.example').read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('#') and ('=' not in line or line.split('=',1)[1].strip()):errors.append('.env.example: values must be empty')
    sql=(root/'templates/supabase/content.sql').read_text() if (root/'templates/supabase/content.sql').exists() else ''
    for table in ('products','events'):
        if f'alter table public.{table} enable row level security;' not in sql:errors.append('SQL missing RLS '+table)
    if re.search(r'grant\s+(?:all|insert|update|delete)\b',sql,re.I):errors.append('Read-only SQL template has write grant')
    sourcefile=root/'docs/sources.json'
    if sourcefile.exists():
        sources=json.loads(sourcefile.read_text())['sources']
        if len({s['id'] for s in sources})!=len(sources):errors.append('Duplicate source IDs')
        for s in sources:
            if not s['url'].startswith('https://'):errors.append('Non-HTTPS source URL')
            reviewed=s.get('last_reviewed')
            if reviewed and date.fromisoformat(reviewed)>date.today():errors.append('Future source review date')
            if s['status']=='discovery' and reviewed:errors.append('Discovery source has unearned review date')
    for error in errors:print('FAIL '+error)
    print(json.dumps({'counts':dict(counts),'errors':len(errors),'scope':'offline integrity; not runtime/provider or complete security verification'},sort_keys=True))
    return int(bool(errors))

if __name__=='__main__':
    sys.exit(run())
