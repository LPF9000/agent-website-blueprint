"""Behavioral tests for fail-closed config, redirects, bounded HTTP and parsers; no live probes."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import health
import weekly
import validate

class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.c=json.loads((ROOT/'templates/environment/monitor.json').read_text())
        self.c.update(authorized=True, origin='https://www.python.org')
    def test_shipped_example_refuses_to_run(self):
        with self.assertRaises(health.ConfigError):
            health.validate_config(json.loads((ROOT/'templates/environment/monitor.json').read_text()))
    def test_credentials_cleartext_custom_ports_and_queries_rejected(self):
        for origin in ['http://www.python.org','https://a:b@www.python.org','https://www.python.org:444','https://www.python.org/?token=x']:
            c=deepcopy(self.c);c['origin']=origin
            with self.subTest(origin=origin),self.assertRaises(health.ConfigError):health.validate_config(c)
    def test_path_escape_and_token_paths_rejected(self):
        for path in ['//evil.org','/a?token=x','/%2fexample.com','/a/../private','/a%0dheader','/a\\b']:
            with self.subTest(path=path),self.assertRaises(health.ConfigError):health.safe_path(path)
    def test_private_or_mixed_dns_rejected(self):
        answers=[(2,1,6,'',('127.0.0.1',443)),(2,1,6,'',('1.1.1.1',443))]
        with patch('health.socket.getaddrinfo',return_value=answers),self.assertRaises(health.ConfigError):health.public_dns('www.python.org')
    def test_unexpected_redirect_fails_and_expected_does_not_follow(self):
        c=health.validate_config(self.c);c['expected_headers']={'x-content-type-options':'nosniff'}
        e={'path':'/old','status':301}
        h={'location':'/new','x-content-type-options':'nosniff'}
        self.assertIn('unexpected-redirect',health.check_response(c,e,301,h,b''))
        c['redirects']={c['origin']+'/old':c['origin']+'/new'}
        self.assertEqual([],health.check_response(c,e,301,h,b''))
        self.assertIsNone(health.NoRedirect().redirect_request(None,None,301,'',{},'https://elsewhere.invalid'))
    def test_header_and_marker_contract_failures(self):
        c=health.validate_config(self.c);c['expected_headers']={'x-content-type-options':'nosniff'}
        issues=health.check_response(c,{'path':'/','status':200,'contains':'Expected'},200,{},b'Wrong')
        self.assertIn('header-x-content-type-options',issues);self.assertIn('missing-public-marker',issues)
    def test_oversized_body_fails_without_unbounded_read(self):
        c=health.validate_config(self.c)
        response=MagicMock();response.__enter__.return_value=response;response.read.return_value=b'x'*(health.MAX_BODY+1)
        opener=MagicMock();opener.open.return_value=response
        with patch('health.public_dns'),patch('health.urllib.request.build_opener',return_value=opener),self.assertRaises(health.ConfigError):health.fetch(c,'/')
        response.read.assert_called_once_with(health.MAX_BODY+1)
    def test_sitemap_rejects_html_external_and_entities(self):
        for body in [b'<html/>',b'<!DOCTYPE x><urlset/>',b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://elsewhere.invalid/</loc></url></urlset>']:
            with self.subTest(body=body),self.assertRaises(ValueError):weekly.check_sitemap(body,self.c['origin'])
    def test_valid_sitemap_and_robots(self):
        body=b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://www.python.org/</loc></url></urlset>'
        self.assertEqual(1,weekly.check_sitemap(body,self.c['origin']))
        self.assertTrue(weekly.check_robots(b'User-agent: *\nAllow: /\nSitemap: https://www.python.org/sitemap.xml',self.c))
    def test_robots_blocking_indexable_root_fails(self):
        with self.assertRaises(ValueError):weekly.check_robots(b'User-agent: *\nDisallow: /\nSitemap: https://www.python.org/sitemap.xml',self.c)

class IntegrityTests(unittest.TestCase):
    def test_yaml_on_is_not_boolean_and_duplicates_rejected(self):
        data=validate.yaml.load('on:\n  push:\npermissions:\n  contents: read\n',Loader=validate.UniqueLoader)
        self.assertIn('on',data)
        with self.assertRaises(ValueError):validate.yaml.load('name: one\nname: two',Loader=validate.UniqueLoader)
    def test_workflow_rejects_unpinned_action_and_write_permission(self):
        data={'on':{'push':None},'permissions':{'contents':'write'},'jobs':{'job':{'timeout-minutes':5,'steps':[{'uses':'actions/checkout@main'}]}}}
        errors=validate.workflow_errors(data,'fixture')
        self.assertTrue(any('contents: read' in e for e in errors));self.assertTrue(any('full-SHA' in e for e in errors))
    def test_markdown_links_missing_anchors_and_repo_escape(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);p=root/'README.md';p.write_text('# Main\n\n## Existing\n')
            self.assertEqual([],validate.check_links(root,p,'[ok](#existing)'))
            self.assertTrue(validate.check_links(root,p,'[bad](#absent)'))
            self.assertTrue(validate.check_links(root,p,'[bad](missing.md)'))
            self.assertTrue(validate.check_links(root,p,'[bad](../outside.md)'))
    def test_json_reference_resolution(self):
        self.assertEqual([],validate.ref_errors({'definitions':{'A':{}},'x':{'$ref':'#/definitions/A'}}))
        self.assertTrue(validate.ref_errors({'x':{'$ref':'#/missing'}}))

if __name__=='__main__':unittest.main()
