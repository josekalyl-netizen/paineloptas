#!/usr/bin/env python3
"""Gera docs/o-que-falta.html (lista interativa do que falta para os dados reais)."""
import base64, html as H, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
logo = base64.b64encode((raiz / 'assets/logo-optas.png').read_bytes()).decode()
DATA = '25/11/2026'
itens = [
 ("Decisões","alta","Projeto Hapvida: onde entra o dinheiro?","Os extratos da W3G não trazem as comissões do Projeto Hapvida (100% da 1ª mensalidade). Em outubro o projeto implantou R$ 1.960,53 e em novembro R$ 21.343,07 até 25/11.","Em qual relatório/extrato vem e em que mês","A receber do projeto e lucro de outubro e novembro."),
 ("Dados","alta","Situação das propostas no SisWeb","Exportação com a situação (cancelada, sem confirmação da 1ª, cancelada na operadora, inadimplente, implantada) e a data do cancelamento.","Mesma exportação do SisWeb + 2 colunas","Cancelamentos saem da conta; explica as 231 parcelas não pagas."),
 ("Dados","média","Extratos novos todo mês","Mogi: falta o de novembro. Consolação: não houve extrato em outubro?","CSV do SisWeb, como os enviados","Recebido, vitalício, folha e créditos/débitos do mês."),
 ("Dados","média","Comissão da Optas em 5 propostas do SisWeb","Select, Unimed Santos, Biovida e duas Onmed (Qualicorp) estão sem a comissão da corretora cadastrada.","Cadastrar no SisWeb","A receber dessas propostas."),
 ("Acessos","alta","Projeto do Apps Script","Para publicar o painel e atualizar sozinho (chaves OPTAS_KEY, OPTAS_TV_KEY, OPTAS_PLANILHA_LEADS).","Compartilhar o projeto","Painel publicado, vidas e produção ao vivo."),
 ("Acessos","alta","SisWeb (exportação automática ou API)","Hoje os arquivos são enviados à mão.","Acesso / rotina de exportação","Propostas, parcelas e situação sem digitação."),
 ("Acessos","média","Kolmeya: liberar o IP","A leitura das respostas de SMS está com erro 403 (IP não liberado) e a aba Leads WhatsApp (SMS) está vazia.","Pedido ao suporte da Kolmeya","ROI por campanha a partir de dezembro."),
]
registrado = ("Grade V3; Projeto Hapvida 100%; adesão sem taxa; vitalício após o agenciamento e no lucro; Prevent por idade; vendedor (faixa pela produção total, 15% + valor por vida só implantadas, a partir de 25); "
  "reserva que passa para o mês seguinte; feriados de SP e Carnaval; SMS de Mogi jan–out; ROI geral até novembro; SisWeb (358 propostas, parcelas reais); extratos (23, de-para no centavo); "
  "créditos/débitos classificados; folha do extrato sobrepõe a estrutura; empréstimos fora do resultado; Valdecir 40% como custo de operação de Mogi; Gileade fora; a receber em simulação com ajuste aos 90 dias pelo vencimento do SisWeb; vendas fora do mês só pelo SisWeb; empréstimo da Joana fora do sistema; comissões dos vendedores = as dos relatórios de pagamento (sem folha à parte); vendas até novembro sem vendedor e, de dezembro em diante, vendedor informado pela Optas.")
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
var K='optas_falta_v4',S={{}};try{{S=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function upd(){{var t=0,o=0;document.querySelectorAll('.item').forEach(function(el){{t++;var on=!!S[el.dataset.id];el.classList.toggle('ok',on);el.querySelector('input').checked=on;if(on)o++;}});document.getElementById('cont').textContent=o+' de '+t;document.getElementById('bar').style.width=(t?o/t*100:0)+'%';}}
document.querySelectorAll('.item').forEach(function(el){{el.querySelector('input').addEventListener('change',function(e){{S[el.dataset.id]=e.target.checked;try{{localStorage.setItem(K,JSON.stringify(S))}}catch(x){{}}upd();}});}});upd();
</script></body></html>'''
(raiz / 'docs/o-que-falta.html').write_text(page, encoding='utf-8')
print(n, 'itens')
