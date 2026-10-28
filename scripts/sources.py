#!/usr/bin/env python3
"""Report discovery/stale sources; optional bounded HTTP reachability, not content review."""
import argparse
from datetime import date
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--topic')
    p.add_argument('--stale-days', type=int, default=30)
    p.add_argument('--live', action='store_true', help='At most 10 selected official URLs; no credential/auth access')
    args = p.parse_args()
    rows = json.loads((ROOT/'docs/sources.json').read_text())['sources']
    if args.topic:
        rows = [r for r in rows if r['topic'] == args.topic]
    if not rows:
        p.error('No source entries match the selected topic')
    if args.stale_days < 0:
        p.error('stale-days must be nonnegative')
    if args.live and len(rows) > 10:
        p.error('Select a topic with at most 10 entries for rate-conscious live checks')
    unavailable = False
    for r in rows:
        reviewed = r.get('last_reviewed')
        age = (date.today() - date.fromisoformat(reviewed)).days if reviewed else None
        state = 'DISCOVERY' if age is None else ('REVIEW DUE' if age > args.stale_days else 'REVIEW DATE WITHIN WINDOW; still recheck before use')
        print(f"{r['id']}: {state}")
        if args.live:
            # Register is owner-reviewed input. Never substitute arbitrary user URLs.
            req = urllib.request.Request(r['url'], headers={'User-Agent':'BlueprintDocsReview/0.1'}, method='HEAD')
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    print(f"  HTTP {response.status}: reachable, content NOT reviewed")
            except Exception:
                unavailable = True
                print('  UNVERIFIED: network/HTTP/tool limit; use official docs connector or navigation')
    print('No review dates changed. Read content/changelogs and run integration tests before claiming verification.')
    return int(unavailable)

if __name__ == '__main__':
    sys.exit(main())
