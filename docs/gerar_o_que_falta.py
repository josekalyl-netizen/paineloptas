#!/usr/bin/env python3
"""Gera docs/o-que-falta.html (lista interativa do que falta para os dados reais)."""
import base64, html as H, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
logo = base64.b64encode((raiz / 'assets/logo-optas.png').read_bytes()).decode()
DATA = '25/11/2026'
itens = [
 ("Regras de negócio","alta","Projeto Hapvida conta na faixa da unidade?","Hoje a faixa do vendedor (Consolação 30%/50%, Mogi 20% a 50%) é calculada só sobre a produção FORA do projeto; o projeto paga 15% + valor por vida. A produção do projeto também deve contar para atingir a faixa?","Sim (soma para a faixa) / Não (como está)","Muda a comissão de quem vende projeto e fora."),
 ("Regras de negócio","média","Vitalício entra no lucro?","Hoje o vitalício aparece separado e não soma no lucro bruto/líquido. Deve somar (com 15% de imposto)?","Sim / Não","Muda lucro bruto, líquido e margens."),
 ("Regras de negócio","média","Reserva de marketing não usada","A verba que sobrar no mês passa para o mês seguinte ou zera no fechamento?","Acumula / Zera","Muda o saldo disponível para investir."),
 ("Regras de negócio","média","Feriados e recessos","Dias sem expediente: aniversário de São Paulo, aniversário de Mogi, Carnaval, Corpus Christi, 24/12, 31/12, recesso de fim de ano.","Aba “Feriados e recessos” da planilha","Muda VR/VT de cada mês."),
 ("Regras de negócio","baixa","Encargos da provisão (34,8%)","Validação da contabilidade: INSS 20% + RAT 1% + Terceiros 5,8% + FGTS 8% sobre 13º e férias.","Confirmado / valores corretos","Muda a provisão mensal (R$ 1.623,15)."),
 ("Regras de negócio","baixa","Sócias recebem VR/VT?","Hoje o VR/VT por pessoa é dividido só pelos CLT (5 e 4).","Sim / Não","Muda o valor por pessoa."),
 ("Decisões que tomei e preciso que você confirme","média","Investimento sem unidade","Quando o investimento não diz se é de Mogi ou Consolação, divido pela produção de cada unidade.","Confirmo / outra regra","Muda o lucro líquido de cada unidade."),
 ("Decisões que tomei e preciso que você confirme","média","Meta “não fechar no vermelho e investir”","Usa a reserva de marketing (15% da produção), não o valor realmente investido.","Confirmo / usar o investido","Muda o valor da segunda meta."),
 ("Decisões que tomei e preciso que você confirme","média","Retorno do ROI","Retorno = comissão total contratada (todas as parcelas) das vendas da campanha.","Confirmo / outra base","Muda o ROI."),
 ("Dados para os números ficarem reais","alta","Vendas de 2026, venda a venda","Cada venda: data, unidade, vendedor, Projeto Hapvida (sim/não), operadora, modalidade, produto/condição, valor mensal, situação, nº do contrato, campanha/origem, cliente, CPF/CNPJ, vidas e data de nascimento do titular (PF/adesão).","Aba “Vendas 2026” da planilha","Base de tudo: a receber por parcela, comissões, vidas do projeto, ROI, gráficos."),
 ("Dados para os números ficarem reais","alta","Carteira ativa","Todos os contratos rodando (de qualquer ano): nº, operadora, modalidade, valor atual, data de início, situação.","Aba “Carteira ativa” da planilha","Parcelas que ainda entram e vitalício previsto."),
 ("Dados para os números ficarem reais","alta","Relatórios de vitalício recebido","Quanto entrou de vitalício por operadora em cada mês.","Aba “Vitalício recebido” ou os relatórios das operadoras","Comparação previsto × recebido."),
 ("Dados para os números ficarem reais","média","Custos reais de cada mês","Salários, VR, VT, operação e outros custos de janeiro a dezembro, por unidade.","Aba “Custos mensais” (outubro já preenchido)","Lucro real de cada mês do ano."),
 ("Dados para os números ficarem reais","média","Investimentos em marketing de 2026","Cada investimento: data, campanha, valor (e unidade, se houver).","Aba “Investimentos mkt” ou escrever no painel","Lucro líquido e ROI reais."),
 ("Dados para os números ficarem reais","baixa","Equipe","Admissões e saídas de 2026.","Aba “Equipe” da planilha","Quantas pessoas havia em cada mês."),
 ("Acessos e integração","alta","CRM (PipeRun)","Acesso à API do PipeRun para trazer as vendas com campanha/origem, vidas e cliente automaticamente. A chave é cadastrada de forma segura no ambiente, nunca pelo chat.","Liberar acesso / token de API","Vendas sem digitação; ROI automático."),
 ("Acessos e integração","alta","Planilha Google","Link da planilha onde a equipe registra as vendas hoje.","Link compartilhado","O painel lê os dados direto da planilha."),
 ("Acessos e integração","média","Documentação dos clientes","Onde ficam os documentos dos clientes (para ler a data de nascimento dos titulares).","Pasta / sistema e forma de acesso","Prevent Senior 0 a 18 anos não comissiona."),
 ("Acessos e integração","média","Projeto do Apps Script","Acesso ao projeto do painel TV atual para publicar o painel novo, com as chaves OPTAS_KEY e OPTAS_TV_KEY.","Compartilhar o projeto","Painel publicado e atualizando sozinho."),
]
registrado = ("Grade de Comissão V3 (02/10/2026) completa, com Amil PME 1% de vitalício e Hapvida/NotreDame PME 290%; Projeto Hapvida 100% em parcela única; "
  "adesão sem a 1ª parcela (taxa); vitalício depois da última parcela; Prevent 0 a 18 anos sem comissão; vendedor no projeto 15% + valor por vida a partir de 25 vidas; "
  "caixa por parcelas; custos de outubro; VR/VT por dia útil; faixas dos vendedores de Consolação e Mogi.")
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
var K='optas_falta_v2',S={{}};try{{S=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function upd(){{var t=0,o=0;document.querySelectorAll('.item').forEach(function(el){{t++;var on=!!S[el.dataset.id];el.classList.toggle('ok',on);el.querySelector('input').checked=on;if(on)o++;}});document.getElementById('cont').textContent=o+' de '+t;document.getElementById('bar').style.width=(t?o/t*100:0)+'%';}}
document.querySelectorAll('.item').forEach(function(el){{el.querySelector('input').addEventListener('change',function(e){{S[el.dataset.id]=e.target.checked;try{{localStorage.setItem(K,JSON.stringify(S))}}catch(x){{}}upd();}});}});upd();
</script></body></html>'''
(raiz / 'docs/o-que-falta.html').write_text(page, encoding='utf-8')
print(n, 'itens')
