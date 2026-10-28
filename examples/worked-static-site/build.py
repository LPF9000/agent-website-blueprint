#!/usr/bin/env python3
"""Render a fictional static fixture; no dependencies, remote assets or deployment."""
import argparse
from html import escape
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STYLE = '''
:root { color-scheme: light; font-family: system-ui, sans-serif; color: #182f28; background: #f5f4ec; }
* { box-sizing: border-box; }
body { margin: 0; line-height: 1.65; }
header, main, footer { max-width: 58rem; margin: auto; padding: 1.5rem; }
header { display: flex; gap: 1rem; justify-content: space-between; flex-wrap: wrap; border-bottom: 1px solid #8b9b8e; }
nav { display: flex; gap: 1.25rem; }
a { color: #174f40; text-underline-offset: .2em; }
a:focus-visible { outline: 3px solid #815900; outline-offset: 4px; }
h1 { font-size: clamp(2rem, 6vw, 4rem); line-height: 1.15; max-width: 16ch; }
p { max-width: 65ch; }
main { min-height: 60vh; padding-block: 3rem; }
footer { border-top: 1px solid #8b9b8e; }
.skip { position: absolute; top: -10rem; left: 1rem; padding: .5rem; background: white; }
.skip:focus { top: .5rem; }
'''.strip() + '\n'


def page_html(title, heading, body, name, summary):
    values = [escape(v, quote=True) for v in (title, heading, body, name, summary)]
    title, heading, body, name, summary = values
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{summary}">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header><a href="/">{name}</a><nav aria-label="Main navigation"><a href="/">Home</a><a href="/visit/">Visit</a></nav></header>
<main id="main"><h1>{heading}</h1><p>{body}</p></main>
<footer><p>Fictional example for local inspection. No real event or organization.</p></footer>
</body>
</html>
'''


def render(content):
    """An explicit route map prevents source/configuration files becoming assets."""
    if not isinstance(content, dict) or set(content) != {'name', 'summary', 'pages'}:
        raise ValueError('Expected name, summary and pages')
    for key in ('name', 'summary'):
        if not isinstance(content[key], str) or not 1 <= len(content[key]) <= 300:
            raise ValueError('Invalid public text')
    pages = content['pages']
    if not isinstance(pages, list) or len(pages) != 2:
        raise ValueError('This fixture has exactly two pages')
    routes = {'/': 'index.html', '/visit/': 'visit/index.html'}
    found = set()
    files = {'assets/site.css': STYLE}
    for page in pages:
        if not isinstance(page, dict) or set(page) != {'path', 'title', 'heading', 'body'}:
            raise ValueError('Unexpected page fields')
        path = page['path']
        if path not in routes or path in found:
            raise ValueError('Unexpected or duplicate route')
        found.add(path)
        if any(not isinstance(page[k], str) or not 1 <= len(page[k]) <= 2000 for k in ('title', 'heading', 'body')):
            raise ValueError('Invalid page text')
        files[routes[path]] = page_html(page['title'], page['heading'], page['body'], content['name'], content['summary'])
    files['404.html'] = page_html('Page not found', 'Page not found', 'Use Home or Visit to return to this fictional example.', content['name'], 'This example page could not be found.')
    return files


def build(output, content_path=HERE / 'content.json'):
    files = render(json.loads(content_path.read_text(encoding='utf-8')))
    output = Path(output)
    # Refuse stale/unreviewed output rather than deleting unrelated files.
    if output.is_symlink():
        raise ValueError('Output must not be a symlink')
    expected = set(files)
    if output.exists():
        for p in output.rglob('*'):
            if p.is_symlink() or (p.is_file() and p.relative_to(output).as_posix() not in expected):
                raise ValueError('Output contains unexpected files; inspect it before rebuilding')
    for relative, text in files.items():
        dest = output / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding='utf-8')
    return sorted(files)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=HERE / 'dist')
    args = p.parse_args()
    paths = build(args.output)
    print(json.dumps({'files': paths, 'count': len(paths), 'scope': 'local static fixture; no deployment'}, sort_keys=True))

if __name__ == '__main__':
    main()
