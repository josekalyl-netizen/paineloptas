#!/usr/bin/env python3
"""Gera docs/o-que-falta.html (lista interativa do que falta para os dados reais)."""
import base64, html as H, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
logo = base64.b64encode((raiz / 'assets/logo-optas.png').read_bytes()).decode()
DATA = '25/11/2026'
itens = [
 ("Dados para os números ficarem reais","alta","Fechamento de folha de cada mês (jan a out)","Relatório mensal com cada venda (vendedor, operadora, modalidade, produto, vidas, valor, cliente, CPF/CNPJ, projeto sim/não) e o que foi pago a cada vendedor.","Arquivo do fechamento (Excel, PDF ou CSV) mês a mês","Preenche a receber, comissões e lucro de janeiro a outubro; confere o que foi pago × a regra."),
 ("Dados para os números ficarem reais","alta","Vitalício recebido, mês a mês e proposta a proposta","O que entrou de vitalício em cada mês, por contrato.","Relatórios das operadoras","Vitalício real no lucro de cada mês e carteira ativa."),
 ("Dados para os números ficarem reais","alta","Agenciamento recebido (o que entrou, atrasou e falta)","Relatórios de recebimento das operadoras, para trocar o previsto pela grade pelo que realmente entrou.","Relatórios de recebimento","Caixa real, atrasos e cancelamentos."),
 ("Dados para os números ficarem reais","média","Data de nascimento nas vendas Prevent Senior","Só para as vendas Prevent: titular de 0 a 18 anos não comissiona.","Coluna no fechamento ou documentação do cliente","Comissão Prevent correta."),
 ("Dados para os números ficarem reais","média","Campanha de cada venda","Qual venda veio do SMS (ou de outra campanha), para o ROI.","Campo no ERP/CRM ou no fechamento","ROI do SMS por venda."),
 ("Acessos e integração","alta","ERP","Acesso ao ERP para buscar vendas, recebimentos e vitalícios direto da fonte.","Usuário/token (cadastrado de forma segura, nunca pelo chat)","Painel atualizado sem digitação."),
 ("Acessos e integração","alta","Projeto do Apps Script","Acesso ao projeto do painel atual para publicar, com as chaves OPTAS_KEY e OPTAS_TV_KEY.","Compartilhar o projeto","Painel publicado e atualizando sozinho."),
 ("Regras de negócio","baixa","Encargos da provisão (34,8%)","Validação da contabilidade: INSS 20% + RAT 1% + Terceiros 5,8% + FGTS 8% sobre 13º e férias.","Confirmado / valores corretos","Provisão mensal (R$ 1.623,15)."),
 ("Decisões que tomei e preciso que você confirme","média","Retorno do ROI","Retorno = comissão total contratada (todas as parcelas) das vendas da campanha.","Confirmo / outra base","ROI."),
 ("Decisões que tomei e preciso que você confirme","baixa","Investimento sem unidade","Quando o investimento não diz a unidade, divido pela produção de cada unidade. (Os SMS de 2026 são todos de Mogi.)","Confirmo / outra regra","Lucro líquido por unidade."),
]
registrado = ("Grade de Comissão V3 completa (Amil PME 1% de vitalício; Hapvida/NotreDame PME 290%); Projeto Hapvida 100%; adesão sem a taxa; vitalício depois da última parcela e somando no lucro; Prevent 0 a 18 sem comissão; "
  "vendedor: faixa pela produção total, projeto 15% + valor por vida a partir de 25; reserva que passa para o mês seguinte; feriados de SP capital e Carnaval; sócios sem VR/VT; custos replicados de outubro; "
  "SMS de Mogi jan–out (R$ 87.926,48); novembro sem investimento.")
grupos = []
for g in [x[0] for x in itens]:
    if g not in grupos: grupos.append(g)
cards = ''; n = 0
for g in grupos:
    cards += f'<h2>{H.escape(g)}</h2><div class="lista">'
    for it in [x for x in itens if x[0] == g]:
        n += 1
        pri = {'alta': 'Prioridade alta', 'média': 'Prioridade média', 'baixa': 'Prioridade baixa'}[it[1]]
        cards += (f'<label class="item p-{it[1]}" data-id="{H.escape(it[2])}"><input type="checkbox"><div class="corpo"><div class="topo"><span class="pri">{pri}</span><b>{H.escape(it[2])}</b></div>'
                  f'<p>{H.escape(it[3])}</p><div class="kv"><span><em>Formato</em>{H.escape(it[4])}</span><span><em>O que muda</em>{H.escape(it[5])}</span></div></div></label>')
    cards += '</div>'
cont = {k: sum(1 for x in itens if x[1] == k) for k in ('alta', 'média', 'baixa')}
css = (raiz / 'docs/o-que-falta.css').read_text() if (raiz / 'docs/o-que-falta.css').exists() else ''
page = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>OPTAS · O que falta</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><style>
:root{{--bg:#FBF7F3;--card:#FFFDFB;--tint:#F4ECE4;--line:#E8DDD2;--ink:#1E1A17;--ink-2:#4A4038;--mute:#6E625A;--or:#FF811B;--or-d:#A84A0A;--green:#1F9D5C;--red:#D93A2B;--red-t:#FDE6E2;--gold-t:#FFF4D6;--gold-d:#9A6700}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif;font-size:15px;line-height:1.45}}
.wrap{{max-width:1100px;margin:0 auto;padding:24px clamp(14px,3vw,32px) 60px}}.hd{{display:flex;align-items:center;gap:16px;flex-wrap:wrap}}.hd img{{height:56px}}
.hd .k{{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--or-d)}}h1{{font-family:Montserrat;font-weight:800;font-size:clamp(22px,3.4vw,32px)}}h1 span{{color:var(--or)}}
.prog{{background:var(--card);border-radius:14px;padding:16px 18px;margin:20px 0 6px;box-shadow:0 1px 0 #E6DCD2,0 6px 20px rgba(110,80,50,.06);border-top:4px solid var(--or)}}
.prog .l{{display:flex;justify-content:space-between;font-weight:700}}.bar{{height:12px;background:var(--tint);border-radius:999px;overflow:hidden;margin-top:10px}}.bar i{{display:block;height:100%;background:var(--green);border-radius:999px;transition:width .3s}}
.resumo{{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;font-size:13px;color:var(--mute)}}.resumo b{{color:var(--ink)}}h2{{font-family:Montserrat;font-weight:800;font-size:19px;margin:28px 0 10px}}
.lista{{display:grid;gap:10px}}.item{{display:grid;grid-template-columns:28px 1fr;gap:12px;background:var(--card);border-radius:12px;padding:14px 16px;box-shadow:0 1px 0 #E6DCD2;border-left:5px solid var(--line);cursor:pointer}}
.item.p-alta{{border-left-color:var(--red)}}.item.p-média{{border-left-color:var(--or)}}.item.p-baixa{{border-left-color:var(--gold-d)}}.item input{{width:22px;height:22px;accent-color:var(--green);margin-top:2px}}
.topo{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}.topo b{{font-size:15.5px}}.pri{{font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;border-radius:6px;padding:2px 7px}}
.p-alta .pri{{background:var(--red-t);color:var(--red)}}.p-média .pri{{background:#FFE3CC;color:var(--or-d)}}.p-baixa .pri{{background:var(--gold-t);color:var(--gold-d)}}
.item p{{margin-top:6px;color:var(--ink-2)}}.kv{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px;font-size:13px}}@media(max-width:640px){{.kv{{grid-template-columns:1fr}}}}
.kv span{{background:var(--bg);border-radius:8px;padding:7px 10px}}.kv em{{display:block;font-style:normal;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--mute)}}
.item.ok{{border-left-color:var(--green);opacity:.6}}.item.ok b{{text-decoration:line-through}}.ft{{margin-top:30px;font-size:12.5px;color:var(--mute)}}
</style></head><body><div class="wrap">
<div class="hd"><img src="data:image/png;base64,{logo}" alt="OPTAS"><div><div class="k">Painel gerencial · {DATA}</div><h1>O que falta para os <span>dados reais</span></h1></div></div>
<div class="prog"><div class="l"><span>Enviados</span><span id="cont">0 de {n}</span></div><div class="bar"><i id="bar"></i></div>
<div class="resumo"><span><b>{cont['alta']}</b> de prioridade alta</span><span><b>{cont['média']}</b> média</span><span><b>{cont['baixa']}</b> baixa</span></div></div>
{cards}<div class="ft">Já registrado: {H.escape(registrado)} As marcações ficam salvas neste navegador.</div></div>
<script>
var K='optas_falta_v3',S={{}};try{{S=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function upd(){{var t=0,o=0;document.querySelectorAll('.item').forEach(function(el){{t++;var on=!!S[el.dataset.id];el.classList.toggle('ok',on);el.querySelector('input').checked=on;if(on)o++;}});document.getElementById('cont').textContent=o+' de '+t;document.getElementById('bar').style.width=(t?o/t*100:0)+'%';}}
document.querySelectorAll('.item').forEach(function(el){{el.querySelector('input').addEventListener('change',function(e){{S[el.dataset.id]=e.target.checked;try{{localStorage.setItem(K,JSON.stringify(S))}}catch(x){{}}upd();}});}});upd();
</script></body></html>'''
(raiz / 'docs/o-que-falta.html').write_text(page, encoding='utf-8')
print(n, 'itens')
