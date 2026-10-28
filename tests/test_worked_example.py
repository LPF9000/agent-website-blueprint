"""Verify actual artifact and loopback HTTP behavior; no hosted-site claims."""
from copy import deepcopy
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples/worked-static-site'
spec = importlib.util.spec_from_file_location('worked_build', EXAMPLE / 'build.py')
worked = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worked)

class Structure(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags = []; self.links = []; self.robots = None; self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs); self.tags.append(tag)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag == 'a': self.links.append(attrs.get('href', ''))
        if tag == 'meta' and attrs.get('name') == 'robots': self.robots = attrs.get('content')

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

class WorkedExampleTests(unittest.TestCase):
    def test_repeatable_artifact_and_no_unexpected_files(self):
        with tempfile.TemporaryDirectory() as d:
            output = Path(d) / 'dist'
            paths = worked.build(output)
            self.assertEqual(paths, ['404.html', 'assets/site.css', 'index.html', 'visit/index.html'])
            first = {p: (output / p).read_bytes() for p in paths}
            worked.build(output)
            self.assertEqual(first, {p: (output / p).read_bytes() for p in paths})
            (output / 'private.txt').write_text('synthetic unexpected file')
            with self.assertRaises(ValueError): worked.build(output)
            self.assertTrue((output / 'private.txt').exists(), 'Do not delete unreviewed files')

    def test_content_is_escaped_and_unapproved_routes_rejected(self):
        content = json.loads((EXAMPLE / 'content.json').read_text())
        content['pages'][0]['body'] = '<script>alert("example")</script>'
        rendered = worked.render(content)['index.html']
        self.assertNotIn('<script>', rendered)
        self.assertIn('&lt;script&gt;', rendered)
        content['pages'][0]['path'] = '/../private'
        with self.assertRaises(ValueError): worked.render(content)

    def test_html_landmarks_metadata_and_local_navigation(self):
        files = worked.render(json.loads((EXAMPLE / 'content.json').read_text()))
        for path, body in files.items():
            if not path.endswith('.html'): continue
            p = Structure(); p.feed(body)
            self.assertEqual(p.tags.count('main'), 1)
            self.assertEqual(p.tags.count('h1'), 1)
            self.assertEqual(p.tags.count('title'), 1)
            self.assertIn('nav', p.tags)
            self.assertEqual(p.robots, 'noindex, nofollow')
            self.assertIn('main', p.ids)
            self.assertNotIn('script', p.tags)
            for link in p.links:
                if link.startswith('#'):
                    self.assertIn(link[1:], p.ids)
                else:
                    self.assertIn(link, ('/', '/visit/'))
                    artifact = 'index.html' if link == '/' else 'visit/index.html'
                    self.assertIn(artifact, files)

    def test_actual_loopback_http_routes_and_not_found(self):
        with tempfile.TemporaryDirectory() as d:
            output = Path(d) / 'dist'; worked.build(output)
            server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(output)))
            thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
            base = f'http://127.0.0.1:{server.server_port}'
            try:
                for path, marker in [('/', 'Look closely. Write a little.'), ('/visit/', 'Plan a visit'), ('/assets/site.css', 'focus-visible')]:
                    with urllib.request.urlopen(base + path, timeout=3) as response:
                        self.assertEqual(response.status, 200)
                        self.assertIn(marker, response.read().decode())
                with self.assertRaises(urllib.error.HTTPError) as denied:
                    urllib.request.urlopen(base + '/not-a-real-route', timeout=3)
                self.assertEqual(denied.exception.code, 404)
            finally:
                server.shutdown(); server.server_close(); thread.join(timeout=3)
