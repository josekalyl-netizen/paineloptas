#!/usr/bin/env python3
"""Gera index.html e apps-script/Index.html a partir de src/painel.html.
Uso: python3 build.py [snapshot.json]"""
import base64, json, pathlib, sys
raiz = pathlib.Path(__file__).parent
src = (raiz / 'src/painel.html').read_text(encoding='utf-8')
logo = base64.b64encode((raiz / 'assets/logo-optas.png').read_bytes()).decode()
snap_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else raiz / 'data/snapshot.json'
snap_obj = json.loads(snap_path.read_text(encoding='utf-8'))
# Vidas do Projeto Hapvida por vendedor (planilha de leads). Nome curto do painel ("Wanderleia G.") = 1º nome + inicial do 2º.
vp = raiz / 'data/vidas-projeto.json'
if vp.exists():
    import unicodedata
    def chave(n):
        n = unicodedata.normalize('NFD', n).encode('ascii', 'ignore').decode().lower().replace('.', ' ').split()
        return n[0] + ' ' + (n[1][0] if len(n) > 1 else '')
    vid = {chave(k): v['implantado'] for k, v in json.loads(vp.read_text(encoding='utf-8'))['vendedores'].items()}
    for v in snap_obj.get('vendedores', []):
        if chave(v['nome']) in vid: v['vidasHap'] = vid[chave(v['nome'])]
snap = json.dumps(snap_obj, ensure_ascii=False, separators=(',', ':'))
inv = json.dumps(json.loads((raiz / 'data/investimentos-2026.json').read_text(encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))
erp_p = raiz / 'data/erp/propostas.json'
erp = erp_p.read_text(encoding='utf-8') if erp_p.exists() else '[]'
ext_p = raiz / 'data/erp/extratos.json'
extr = ext_p.read_text(encoding='utf-8') if ext_p.exists() else 'null'
html = src.replace('__LOGO__', logo).replace('__SNAP__', snap).replace('__INVBASE__', inv)
# index.html e preview.html: revisão (com Pendências e Regras)
# apps-script/Index.html: versão publicada, sem Pendências e Regras
(raiz / 'index.html').write_text(html.replace('__ERP__', erp).replace('__EXTRATOS__', extr).replace('__DEMO__', 'false').replace('__PUBLICADO__', 'false'), encoding='utf-8')
(raiz / 'apps-script/Index.html').write_text(html.replace('__ERP__', erp).replace('__EXTRATOS__', extr).replace('__DEMO__', 'false').replace('__PUBLICADO__', 'true'), encoding='utf-8')
(raiz / 'preview.html').write_text(html.replace('__ERP__', '[]').replace('__EXTRATOS__', 'null').replace('__DEMO__', 'true').replace('__PUBLICADO__', 'false'), encoding='utf-8')
print('ok', len(html), 'bytes')
