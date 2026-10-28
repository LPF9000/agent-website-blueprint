#!/usr/bin/env python3
"""Bounded, unauthenticated GET probes. Trusted owner-reviewed config only."""
import argparse
import ipaddress
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MAX_BODY = 1024 * 1024

class ConfigError(ValueError):
    pass

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def safe_path(path):
    if not isinstance(path, str) or not path.startswith('/') or path.startswith('//'):
        raise ConfigError('Use explicit origin-relative paths')
    decoded = urllib.parse.unquote(path)
    if any(c in decoded for c in ('?', '#', '\\', '\r', '\n', '\x00')) or decoded.startswith('//'):
        raise ConfigError('No queries, fragments, backslashes or controls in paths')
    if any(ord(c) < 32 or ord(c) > 126 for c in decoded) or '..' in decoded.split('/'):
        raise ConfigError('Unsafe path')
    return path

def validate_config(c):
    if c.get('authorized') is not True:
        raise ConfigError('Target authorization must be recorded before running probes')
    u = urllib.parse.urlsplit(c.get('origin', ''))
    try:
        port = u.port
    except ValueError as exc:
        raise ConfigError('Invalid origin port') from exc
    if (u.scheme != 'https' or not u.hostname or u.username or u.password or
        port not in (None, 443) or u.path not in ('', '/') or u.query or u.fragment):
        raise ConfigError('Use a canonical HTTPS origin, port 443, without credentials/path/query')
    host = u.hostname.lower()
    if host in ('localhost', 'example.com', 'example.org', 'example.net') or host.endswith(('.localhost', '.local', '.test', '.invalid', '.example')):
        raise ConfigError('Replace reserved/local example origin with an authorized public host')
    c = dict(c)
    c['origin'] = 'https://' + u.netloc.lower()
    if not isinstance(c.get('timeout_seconds'), (int, float)) or not 1 <= c['timeout_seconds'] <= 30:
        raise ConfigError('Timeout must be 1..30 seconds')
    if not isinstance(c.get('tls_min_days'), int) or not 1 <= c['tls_min_days'] <= 90:
        raise ConfigError('TLS minimum days must be 1..90')
    endpoints = c.get('endpoints', [])
    if not isinstance(endpoints, list) or not 1 <= len(endpoints) <= 10:
        raise ConfigError('Configure 1..10 explicitly safe endpoints')
    for e in endpoints:
        safe_path(e['path'])
        if not isinstance(e.get('status'), int) or not 200 <= e['status'] <= 499:
            raise ConfigError('Endpoint requires an expected status 200..499')
        if not isinstance(e.get('contains', ''), str) or len(e.get('contains', '')) > 200:
            raise ConfigError('Use a short public body marker')
    paths = c.get('weekly_paths', [])
    if not isinstance(paths, list) or len(paths) > 30:
        raise ConfigError('At most 30 weekly allowlisted paths')
    for p in paths:
        safe_path(p)
    for name in ('sitemap_path', 'robots_path'):
        safe_path(c[name])
    headers = c.get('expected_headers', {})
    if not isinstance(headers, dict) or not headers or any(not isinstance(k, str) or not isinstance(v, str) for k, v in headers.items()):
        raise ConfigError('Configure nonempty expected_headers mapping')
    redirects = c.get('redirects', {})
    if not isinstance(redirects, dict) or len(redirects) > 10:
        raise ConfigError('At most 10 intentional redirects')
    for src, dst in redirects.items():
        for url in (src, dst):
            parsed = urllib.parse.urlsplit(url)
            if parsed.scheme + '://' + parsed.netloc != c['origin']:
                raise ConfigError('Redirects must remain on the configured canonical origin')
            safe_path(parsed.path)
            if parsed.query or parsed.fragment:
                raise ConfigError('No query/fragment redirect targets')
    if not isinstance(c.get('expect_indexable'), bool):
        raise ConfigError('Set expect_indexable true or false explicitly')
    return c

def public_dns(host):
    addresses = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
        raise ConfigError('Target resolves to a non-public address')

def tls_days(host, timeout):
    context = ssl.create_default_context()
    with socket.create_connection((host, 443), timeout=timeout) as conn:
        with context.wrap_socket(conn, server_hostname=host) as wrapped:
            cert = wrapped.getpeercert()
            return (ssl.cert_time_to_seconds(cert['notAfter']) - time.time()) / 86400

def fetch(c, path):
    path = safe_path(path)
    host = urllib.parse.urlsplit(c['origin']).hostname
    public_dns(host)
    opener = urllib.request.build_opener(NoRedirect(), urllib.request.HTTPSHandler(context=ssl.create_default_context()))
    req = urllib.request.Request(c['origin'] + path, headers={'User-Agent': 'AgentWebsiteBlueprintHealth/0.1', 'Accept-Encoding': 'identity'}, method='GET')
    try:
        response = opener.open(req, timeout=c['timeout_seconds'])
    except urllib.error.HTTPError as exc:
        response = exc  # Inspect status without following redirects or dumping body/headers.
    with response:
        body = response.read(MAX_BODY + 1)
        if len(body) > MAX_BODY:
            raise ConfigError('Response exceeded 1 MiB safety bound')
        return response.code, {k.lower(): v for k, v in response.headers.items()}, body

def check_response(c, e, status, headers, body):
    issues = []
    url = c['origin'] + e['path']
    if status != e['status']:
        issues.append('unexpected-status')
    if 300 <= status < 400:
        location = urllib.parse.urljoin(url, headers.get('location', ''))
        if not headers.get('location') or c['redirects'].get(url) != location:
            issues.append('unexpected-redirect')
    for name, value in c['expected_headers'].items():
        actual = headers.get(name.lower(), '')
        if not actual or (value and value.lower() not in actual.lower()):
            issues.append('header-' + name.lower())
    marker = e.get('contains', '')
    if marker and marker not in body.decode('utf-8', errors='replace'):
        issues.append('missing-public-marker')
    return issues

def run(c):
    host = urllib.parse.urlsplit(c['origin']).hostname
    public_dns(host)
    remaining = tls_days(host, c['timeout_seconds'])
    failed = remaining < c['tls_min_days']
    print('TLS: ' + ('FAIL expiry threshold' if failed else 'PASS valid chain/hostname and expiry threshold'))
    for e in c['endpoints']:
        try:
            status, headers, body = fetch(c, e['path'])
            issues = check_response(c, e, status, headers, body)
            failed |= bool(issues)
            print(e['path'] + ': ' + (','.join(issues) if issues else 'PASS'))
        except Exception:
            failed = True
            print(e['path'] + ': FAIL request/response validation (details deliberately redacted)')
        time.sleep(0.25)
    return 1 if failed else 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path)
    args = parser.parse_args()
    try:
        return run(validate_config(json.loads(args.config.read_text())))
    except Exception:
        print('FAIL configuration/DNS/TLS validation; inspect trusted config and provider status without dumping secrets', file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
