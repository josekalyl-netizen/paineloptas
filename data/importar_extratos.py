#!/usr/bin/env python3
"""Importa os extratos de comissão (SisWeb, CSV) e faz o de-para com as propostas do ERP.
Uso: python3 -I data/importar_extratos.py <pasta com os CSVs de comissões>
Gera data/erp/extratos.json. Cada linha do CSV é uma linha de comissão; o cabeçalho do extrato e os
créditos/débitos vêm repetidos nas colunas (exportação "achatada")."""
import csv, json, pathlib, sys, collections
from decimal import Decimal
pasta = pathlib.Path(sys.argv[1]); raiz = pathlib.Path(__file__).resolve().parent
def brl(x):
    x = (x or '').replace('R$', '').replace('\xa0', '').replace(' ', '')
    if not x: return Decimal(0)
    neg = x.startswith('-'); x = x.lstrip('-').replace('.', '').replace(',', '.')
    return -Decimal(x) if neg else Decimal(x)
pct = lambda s: Decimal(s.replace('%', '').replace('.', '').replace(',', '.') or '0') / 100
iso = lambda d: d[6:10] + '-' + d[3:5] + '-' + d[0:2] if len(d) >= 10 else ''
f2 = lambda d: float(d)
E = json.loads((raiz / 'erp/propostas.json').read_text(encoding='utf-8'))
porNum = collections.defaultdict(list)
for e in E: porNum[e['numero']].append(e)
def acha(d):
    cs = porNum.get(d['proposta'], [])
    if len(cs) > 1:   # número repetido: operadora do grupo, depois mensalidade
        g = d['grupo'].lower()
        c2 = [x for x in cs if x['operadora'].lower() in g or (x.get('administradora') or '').lower() in g] or cs
        if len(c2) > 1: c2 = sorted(c2, key=lambda x: abs(Decimal(str(x['valor_mensal'])) - d['vlparc']))[:1]
        cs = c2
    return cs[0] if cs else None
extratos, linhas, cds = [], [], []
for arq in sorted(pasta.glob('*.csv')):
    rows = list(csv.reader(arq.read_text(encoding='utf-8-sig').splitlines()))
    if not rows or rows[0][:2] != ['textBox4', 'textBox18']: continue
    corretor = rows[1][5]
    unidade = 'Mogi' if 'Mogi' in corretor else ('Consolação' if ('VERUS' in corretor or 'Consola' in corretor) else corretor)
    vistos = {}
    for r in rows[1:]:
        cod = r[6].split(':')[-1].strip()
        if cod not in vistos:
            vistos[cod] = {'cd': set(), 'n': 0}
            extratos.append({'codigo': cod, 'unidade': unidade, 'geracao': iso(r[0]), 'previsao': iso(r[9]), 'mes': iso(r[9])[:7], 'obs': r[1],
                             'acumulado': f2(brl(r[18])), 'creditos_debitos': f2(brl(r[31])), 'bruto': f2(brl(r[41])), 'desp_adm': f2(brl(r[34])),
                             'ato_venda': f2(brl(r[48])), 'parcelas': f2(brl(r[49])), 'comissoes_liquido': f2(brl(r[51])), 'liquido': f2(brl(r[45]))})
        ex = extratos[-1] if extratos[-1]['codigo'] == cod else next(x for x in extratos if x['codigo'] == cod)
        d = {'grupo': r[64], 'cliente': r[86], 'cadastro': iso(r[98]), 'proposta': r[88], 'parc': int(r[89] or 0), 'vlparc': brl(r[90]), 'pct': pct(r[91]),
             'bruto': brl(r[92]), 'desp': brl(r[94]), 'liq': brl(r[96]), 'padm': r[97]}
        e = acha(d); k = d['parc'] - 1
        if e:
            vals = e['tabela']['valores']; vit = k >= len(vals) or (e['tabela']['vitDe'] and d['parc'] >= e['tabela']['vitDe'])
            esperado = vals[k] if k < len(vals) else None
        else:
            vit = d['parc'] > 1 and d['pct'] <= Decimal('0.05'); esperado = None
        linhas.append({'extrato': cod, 'unidade': unidade, 'mes': ex['mes'], 'grupo': d['grupo'], 'operadora': d['grupo'].split(' - ')[0], 'cliente': d['cliente'],
                       'cadastro': d['cadastro'], 'proposta': d['proposta'], 'parc': d['parc'], 'vl_parcela': f2(d['vlparc']), 'pct': f2(d['pct']),
                       'bruto': f2(d['bruto']), 'desp_adm': f2(d['desp']), 'liquido': f2(d['liq']), 'tipo': 'vitalicio' if vit else 'agenciamento',
                       'erp': e['id'] if e else None, 'esperado_erp': esperado})
        ck = tuple(r[101:128])
        if ck not in vistos[cod]['cd'] and r[121]:
            vistos[cod]['cd'].add(ck); cds.append({'extrato': cod, 'unidade': unidade, 'mes': ex['mes'], 'tipo': r[113], 'descricao': r[121], 'liquido': f2(brl(r[126]))})
# Conferência: Σ líquido das linhas = ato + parcelas; acumulado + comissões + créd/déb = líquido do extrato; Σ créd/déb = total do extrato
erros = []
for x in extratos:
    L = [l for l in linhas if l['extrato'] == x['codigo']]; C = [c for c in cds if c['extrato'] == x['codigo']]
    s = lambda it, k: sum(Decimal(str(i[k])) for i in it)
    if s(L, 'liquido') != Decimal(str(x['comissoes_liquido'])): erros.append((x['codigo'], 'linhas'))
    if s(C, 'liquido') != Decimal(str(x['creditos_debitos'])): erros.append((x['codigo'], 'créditos/débitos'))
    if Decimal(str(x['acumulado'])) + Decimal(str(x['comissoes_liquido'])) + Decimal(str(x['creditos_debitos'])) != Decimal(str(x['liquido'])): erros.append((x['codigo'], 'líquido'))
(raiz / 'erp/extratos.json').write_text(json.dumps({'extratos': extratos, 'linhas': linhas, 'creditos_debitos': cds}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(len(extratos), 'extratos ·', len(linhas), 'linhas ·', len(cds), 'créditos/débitos · com ERP', sum(1 for l in linhas if l['erp']), '· conferência:', erros or 'tudo bate')
