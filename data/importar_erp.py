#!/usr/bin/env python3
"""Importa as exportações do ERP (propostas, parcelas e beneficiários) para data/erp/propostas.json.
Uso: python3 -I data/importar_erp.py <pasta com os CSVs>
- Data da venda = data de cadastro (DtProducao).
- Comissão da Optas = parcelas de Ordem 1 (corretora Optas Mogi / Verus Consolação), valor = VlParcela × PcComissao.
- Adesão (GeraComissaoPrimeira = False): a 1ª parcela é a taxa de angariação e não entra.
- Chave da proposta = número + operadora + modalidade (o número se repete entre operadoras)."""
import csv, glob, json, pathlib, sys
from decimal import Decimal, ROUND_HALF_UP
pasta = pathlib.Path(sys.argv[1])
def ler(layout):
    out = []
    for f in sorted(pasta.glob('*.csv')):
        linhas = f.read_text(encoding='utf-8-sig').replace('\r\n', '\n').split('\n')
        if linhas[0].strip() != '#LayoutImportacao' + layout: continue
        rows = list(csv.reader(linhas[1:], delimiter=';'))
        h = rows[0]
        out += [dict(zip(h, r)) for r in rows[1:] if len(r) > 1]
    return out
dec = lambda x: Decimal((x or '0').replace('.', '').replace(',', '.')) if x and ',' in x else Decimal(x or '0')
r2 = lambda d: float(d.quantize(Decimal('0.01'), ROUND_HALF_UP))
iso = lambda d: (d[6:10] + '-' + d[3:5] + '-' + d[0:2]) if d and len(d) >= 10 else ''
MOD = {'Pme': 'PME', 'PmeOdonto': 'PME', 'Empresarial': 'PME', 'Individual': 'PF', 'Familiar': 'PF', 'IndividualOdonto': 'PF', 'FamiliarOdonto': 'PF', 'Adesao': 'ADESÃO', 'Vida': 'VIDA', 'PetGrupal': 'PET'}
P, Q, B = ler('Proposta'), ler('Parcela'), ler('Beneficiario')
chave = lambda x: (x['PropostaNumero'], x['IdOperadora'], x['IdModalidade'])
# Na adesão, as parcelas vêm com a administradora (Qualicorp, Supermed, TECGROUP...) no lugar da operadora
chaveP = lambda p: (p['PropostaNumero'], p['IdAdministradora'] if p['TxtModalidade'] == 'Adesao' and p.get('IdAdministradora') not in ('', '0', None) else p['IdOperadora'], p['IdModalidade'])
parc, tit = {}, {}
for q in Q:
    if q['Ordem'] != '1': continue
    parc.setdefault(chave(q), []).append(q)
for b in B:
    if b['TxtGrauParentesco'] == 'Titular' and chave(b) not in tit: tit[chave(b)] = iso(b['DtNascimento'])
out, sem = [], []
for p in P:
    k = chaveP(p); qs = parc.get(k)
    if qs is None:   # PME por administradora (Qualicorp, TECGROUP): procura pela administradora; senão, único grupo do número
        alt = [c for c in parc if c[0] == p['PropostaNumero'] and c[2] == p['IdModalidade']]
        cand = [c for c in alt if c[1] in (p.get('IdAdministradora'), p['IdOperadora'])] or (alt if len(alt) == 1 else [])
        qs = parc.get(cand[0], []) if cand else []
    if not qs: sem.append(p['PropostaNumero'])
    adesao_taxa = p['GeraComissaoPrimeira'] == 'False'
    ag, vit = {}, {}
    for q in qs:
        n = int(q['Parcela']); pc = dec(q['PcComissao']); val = r2(dec(q['VlParcela']) * pc)
        (vit if q['Vitalicio'] == 'True' else ag)[n] = (float(pc), val)
    if adesao_taxa and 1 in ag: ag[1] = (0.0, 0.0)
    ult = max(ag) if ag else 0
    tabela = {'nome': p['TxtOperadora'], 'erp': True, 'modalidade': MOD.get(p['TxtModalidade'], p['TxtModalidade'].upper()),
              'parc': [ag.get(i, (0.0, 0))[0] for i in range(1, ult + 1)], 'valores': [ag.get(i, (0, 0.0))[1] for i in range(1, ult + 1)],
              'vit': (sorted(v[0] for v in vit.values())[0] if vit else 0), 'vitDe': (min(vit) if vit else None)}
    tabela['ag'] = round(sum(tabela['parc']), 6)
    out.append({'id': 'erp-' + '-'.join(k), 'contrato': 'erp-' + '-'.join(k), 'numero': p['PropostaNumero'], 'origem_dado': 'ERP',
                'unidade': 'Mogi' if 'Mogi' in p['TxtLoja'] else ('Consolação' if 'Consola' in p['TxtLoja'] else p['TxtLoja']),
                'operadora': p['TxtOperadora'], 'administradora': p['TxtAdministradora'] if p['TxtModalidade'] == 'Adesao' else '', 'modalidade': tabela['modalidade'], 'modalidade_erp': p['TxtModalidade'], 'produto': p['TxtSubProduto'],
                'data_venda': iso(p['DtProducao']), 'vigencia': iso(p['DtVigencia']), 'implantacao': iso(p['DtImplantacao']),
                'valor_mensal': r2(dec(p['VlProducao'])), 'vidas': int(p['QtdeBeneficiarios'] or 0), 'cliente': p['Segurado'], 'documento': p['Documento'],
                'data_nascimento': tit.get(k, ''), 'situacao': '', 'projeto': '', 'tabela': tabela})
dst = pathlib.Path(__file__).resolve().parent / 'erp' / 'propostas.json'
dst.parent.mkdir(exist_ok=True)
dst.write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(len(out), 'propostas ·', len(sem), 'sem parcelas da Optas:', sem)
