#!/usr/bin/env python3
"""Gera index.html e apps-script/Index.html a partir de src/painel.html.
Uso: python3 build.py [snapshot.json]"""
import base64, json, pathlib, sys
raiz = pathlib.Path(__file__).parent
src = (raiz / 'src/painel.html').read_text(encoding='utf-8')
logo = base64.b64encode((raiz / 'assets/logo-optas.png').read_bytes()).decode()
snap_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else raiz / 'data/snapshot.json'
snap = json.dumps(json.loads(snap_path.read_text(encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))
html = src.replace('__LOGO__', logo).replace('__SNAP__', snap)
(raiz / 'index.html').write_text(html, encoding='utf-8')
(raiz / 'apps-script/Index.html').write_text(html, encoding='utf-8')
print('ok', len(html), 'bytes')
