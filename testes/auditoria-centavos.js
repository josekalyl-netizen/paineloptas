const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const out = [];
 for (const f of ['preview.html','index.html']) {
 const p = await b.newPage({ viewport: { width: 1440, height: 1000 } }); const errs=[]; p.on('pageerror', e => errs.push(e.message));
 await p.goto('file:///home/user/paineloptas/'+f); await p.waitForTimeout(400);
 const r = await p.evaluate(() => {
   const c = x => Math.round(x*100), falhas = [], ok = (nome, a, b) => { if (c(a) !== c(b)) falhas.push(nome + ': ' + a + ' ≠ ' + b); };
   const cents = x => x == null || Math.abs(c(x) - x*100) < 1e-6;
   const U = REGRAS.unidades.map(u => R.unidades[u]);
   // vendedores → unidade → consolidado
   U.forEach(u => { const vs = R.vendedores.filter(v => v.unidade === u.custos.unidade);
     ok(u.custos.unidade+' produção', u.producao, vs.reduce((t,v)=>t+v.producao,0)); ok(u.custos.unidade+' comissões', u.comissao, vs.reduce((t,v)=>t+v.comissao,0));
     vs.forEach(v => { ok(v.nome+' comissão', v.comissao, r2(v.producao*v.pct)); if(!cents(v.comissao)) falhas.push(v.nome+' comissão com fração de centavo'); }); });
   ok('produção total', R.producao, U.reduce((t,u)=>t+u.producao,0)); ok('comissões total', R.comissoes, U.reduce((t,u)=>t+u.comissao,0));
   // propostas
   const ps = R.ag.propostas.filter(p => p.aReceber != null);
   ps.forEach(p => { ok('proposta '+p.c.id_venda, p.aReceber, r2(p.valor*p.pct)); ok('imposto '+p.c.id_venda, p.liquido + p.imposto, p.aReceber); });
   if (ps.length) { ok('a receber = Σ propostas', R.ag.valor, ps.reduce((t,p)=>t+p.aReceber,0)); ok('imposto = Σ propostas', R.res.imposto, ps.reduce((t,p)=>t+p.imposto,0)); ok('líquido = Σ propostas', R.res.recebidas - R.res.imposto, ps.reduce((t,p)=>t+p.liquido,0)); }
   // resultado por unidade e consolidado
   const chk = (n, x) => { if (!x) return; ['recebidas','imposto','comissoes','reserva','fixo','provisao','operacional','financeiro'].forEach(k => { if (!cents(x[k])) falhas.push(n+' '+k+' com fração de centavo: '+x[k]); });
     ok(n+' operacional', x.operacional, x.recebidas - x.imposto - x.comissoes - x.fixo - x.provisao); ok(n+' financeiro', x.financeiro, x.operacional - x.reserva); };
   U.forEach(u => chk(u.custos.unidade, u.res)); chk('consolidado', R.res);
   if (R.res) ['recebidas','imposto','comissoes','reserva','fixo','provisao','operacional','financeiro'].forEach(k => ok('consolidado '+k+' = Σ unidades', R.res[k], U.reduce((t,u)=>t+u.res[k],0)));
   ok('reserva = Σ unidades', R.reservaMkt, U.reduce((t,u)=>t+u.reservaMkt,0));
   // mínimos
   U.forEach(u => { const m = minimos(u.comissao, Math.round((u.custos.fixo+u.custos.provisao)*100)/100, u.reservaMkt); const x = m.empate, resto = Math.round((x - Math.round(x*0.15*100)/100)*100) - Math.round((u.comissao+u.custos.fixo+u.custos.provisao)*100); if (resto < 0 || resto > 1) falhas.push(u.custos.unidade+' mínimo não fecha: sobra '+resto+' centavos'); });
   return { falhas, resumo: R.res ? { aReceber: R.res.recebidas, imposto: R.res.imposto, comissoes: R.res.comissoes, fixo: R.res.fixo, provisao: R.res.provisao, lucro: R.res.operacional, reserva: R.res.reserva, depois: R.res.financeiro } : 'sem a receber (modo real: Projeto Hapvida pendente)' };
 });
 out.push([f, r, errs]); await p.close(); }
 out.forEach(o => console.log(o[0], JSON.stringify(o[1], null, 1), o[2]));
 await b.close(); })();
