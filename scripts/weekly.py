#!/usr/bin/env python3
"""Bounded allowlisted public-page, sitemap and robots checks; never a crawler."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import time
import urllib.parse
import urllib.robotparser
import xml.etree.ElementTree as ET
from health import fetch, safe_path, validate_config

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.extend(v for k, v in attrs if k == 'href' and v)

def check_sitemap(body, origin):
    if b'<!DOCTYPE' in body.upper() or b'<!ENTITY' in body.upper():
        raise ValueError('No DTD/entities in sitemap')
    root = ET.fromstring(body)
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    if root.tag not in (ns + 'urlset', ns + 'sitemapindex'):
        raise ValueError('Expected namespaced sitemap urlset/index')
    entries = root.findall(ns + ('url' if root.tag == ns + 'urlset' else 'sitemap'))
    if not entries or len(entries) > 50000:
        raise ValueError('Invalid sitemap entry count')
    for entry in entries:
        loc = entry.find(ns + 'loc')
        if loc is None or not loc.text:
            raise ValueError('Sitemap entry missing loc')
        u = urllib.parse.urlsplit(loc.text)
        if u.scheme + '://' + u.netloc != origin or u.query or u.fragment:
            raise ValueError('Only canonical same-origin sitemap locations expected')
        safe_path(u.path or '/')
    return len(entries)

def check_robots(body, c):
    text = body.decode('utf-8')
    has_agent = False
    sitemap = False
    for line in text.splitlines():
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        if ':' not in line:
            raise ValueError('Malformed robots directive')
        name, value = (x.strip() for x in line.split(':', 1))
        if name.lower() == 'user-agent':
            has_agent |= bool(value)
        if name.lower() == 'sitemap':
            sitemap |= value == c['origin'] + c['sitemap_path']
    if not has_agent or not sitemap:
        raise ValueError('robots must declare user-agent and intended sitemap')
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(text.splitlines())
    if c['expect_indexable'] and not rp.can_fetch('*', c['origin'] + '/'):
        raise ValueError('robots blocks public root despite indexable contract')
    return True

def run(c):
    failed = False
    bodies = {}
    paths = list(dict.fromkeys([c['sitemap_path'], c['robots_path']] + c['weekly_paths']))
    for path in paths:
        try:
            status, headers, body = fetch(c, path)
            if status != 200:
                raise ValueError('Expected 200, no redirect')
            bodies[path] = (headers, body)
            if path == c['sitemap_path']:
                count = check_sitemap(body, c['origin'])
                print('sitemap: PASS syntax/canonical locations; entries=' + str(count))
            elif path == c['robots_path']:
                check_robots(body, c)
                print('robots: PASS basic directives and intended sitemap')
            else:
                print(path + ': PASS HTTP 200')
        except Exception:
            failed = True
            print(path + ': FAIL status/content validation (details redacted)')
        time.sleep(0.5)
    checked_links = 0
    omitted = 0
    for path in c['weekly_paths']:
        if path not in bodies:
            continue
        headers, body = bodies[path]
        if 'text/html' not in headers.get('content-type', ''):
            failed = True
            print(path + ': FAIL expected HTML')
            continue
        p = Links()
        p.feed(body.decode('utf-8', errors='replace'))
        for href in p.links:
            resolved = urllib.parse.urlsplit(urllib.parse.urljoin(c['origin'] + path, href))
            if resolved.scheme + '://' + resolved.netloc != c['origin']:
                continue
            # Never follow discovered URLs: report only within reviewed path coverage.
            dest = resolved.path or '/'
            if resolved.query or resolved.fragment or dest not in c['weekly_paths']:
                omitted += 1
            else:
                checked_links += 1
                if dest not in bodies:
                    failed = True
                    print(path + ': FAIL broken internal link within allowlist')
    print(f'Internal link coverage: {checked_links} within allowlist; {omitted} links/anchors/queries not checked')
    print('Sitemap indexes are syntax/location checked only; child maps are not fetched. No semantic business/SEO/accessibility guarantee.')
    return int(failed)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('config', type=Path)
    a = p.parse_args()
    try:
        return run(validate_config(json.loads(a.config.read_text())))
    except Exception:
        print('FAIL configuration; no privileged diagnostic output', file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
