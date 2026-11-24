// Auditoria completa dos cálculos do painel, em centavos.
// Uso: node testes/auditoria-centavos.js   (precisa do Playwright)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const saida = [];
  for (const f of ['preview.html', 'index.html']) {
    const p = await b.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + path.resolve(__dirname, '..', f)); await p.waitForTimeout(500);
    const r = await p.evaluate(() => {
      const c = x => Math.round(x * 100), falhas = [], ok = (n, a, b) => { if (c(a) !== c(b)) falhas.push(n + ': ' + a + ' ≠ ' + b); };
      const cent = x => x == null || Math.abs(c(x) - x * 100) < 1e-6;
      const U = REGRAS.unidades.map(u => R.unidades[u]);
      // vendedores → unidades → consolidado
      U.forEach(u => { const n = u.custos.unidade, vs = R.vendedores.filter(v => v.unidade === n);
        ok(n + ' produção = Σ vendedores', u.producao, vs.reduce((t, v) => t + v.producao, 0));
        ok(n + ' comissões = Σ vendedores', u.comissao, vs.reduce((t, v) => t + v.comissao, 0));
        vs.forEach(v => ok(v.nome + ' comissão = produção × faixa', v.comissao, r2(v.producao * v.pct))); });
      ok('produção = Σ unidades', R.producao, U.reduce((t, u) => t + u.producao, 0));
      ok('comissões = Σ unidades', R.comissoes, U.reduce((t, u) => t + u.comissao, 0));
      // propostas
      // propostas do mês: cada parcela = mensalidade × % da parcela da grade; 1ª parcela entra no mês
      const ps = R.ag.propostas.filter(p => p.aReceber != null);
      ps.forEach(p => { const rg = regraVenda(p.c); const taxa = rg.modalidade === 'ADESÃO' && !REGRAS.adesaoTaxaParaOptas; ok('1ª parcela ' + p.c.id_venda, p.aReceber, taxa ? 0 : r2(p.valor * rg.parc[0]));
        ok('total contratado ' + p.c.id_venda, p.agTotal, rg.parc.reduce((t, x, k) => t + (k === 0 && taxa ? 0 : r2(p.valor * x)), 0)); ok('próximas ' + p.c.id_venda, p.futuro, p.agTotal - p.aReceber); });
      if (ps.length) ok('1ª parcela do mês = Σ propostas', R.ag.valor, ps.reduce((t, p) => t + p.aReceber, 0));
      // parcelas de vendas anteriores, recalculadas de forma independente
      let ant = 0; carteiraCompleta().forEach(c => { const ini = String(c.data_venda || c.data_inicio || '').slice(0, 7); if (!ini || ini >= R.mes) return; if (/cancel/i.test(c.situacao || '') && (!c.cancelado_em || String(c.cancelado_em).slice(0, 7) <= R.mes)) return; const rg = regraVenda(c); if (!rg || rg.ag == null) return; const k = (+R.mes.slice(0, 4) - +ini.slice(0, 4)) * 12 + (+R.mes.slice(5, 7) - +ini.slice(5, 7)); if (rg.parc[k] && !(k === 0 && rg.modalidade === 'ADESÃO' && !REGRAS.adesaoTaxaParaOptas)) ant += r2(r2(+c.valor_mensal) * rg.parc[k]); });
      ok('parcelas anteriores', R.caixaAnt.total, ant);
      U.forEach(u => { if (u.recebidas != null) ok(u.custos.unidade + ' a receber = 1ª parcela + anteriores', u.recebidas, (u.primeira || 0) + (u.anteriores || 0)); });
      if (R.recebidas != null) { ok('a receber = 1ª parcela + anteriores', R.recebidas, R.primeira + R.caixaAnt.total); ok('1ª parcela = Σ unidades', R.primeira, U.reduce((t, u) => t + (u.primeira || 0), 0)); }
      // investimento
      ok('investido = Σ lançamentos', R.investido, ESTADO.investimentos.filter(i => (i.data || '').slice(0, 7) === R.mes).reduce((t, i) => t + (+i.valor || 0), 0));
      ok('investido = Σ unidades', R.investido, U.reduce((t, u) => t + u.investido, 0));
      ok('ROI tab investido = investido', R.roi.total, R.investido);
      // resultado: unidades e consolidado
      const chk = (n, x) => { if (!x) return;
        Object.keys(x).forEach(k => { if (typeof x[k] === 'number' && !/^m[A-Z]/.test(k) && !cent(x[k])) falhas.push(n + ' ' + k + ' com fração de centavo'); });
        ok(n + ' custo da operação = fixos + provisão', x.custoOp, x.fixo + x.provisao);
        ok(n + ' custo de operação total = operação + impostos', x.custoOpTotal, x.custoOp + x.imposto);
        ok(n + ' custos do mês = op. total + comissões', x.custos, x.custoOpTotal + x.comissoes);
        ok(n + ' lucro bruto = a receber − custos', x.operacional, x.recebidas - x.custos);
        ok(n + ' lucro líquido = lucro bruto − investido', x.financeiro, x.operacional - x.investido);
        if (x.recebidas) { if (Math.abs(x.mBruta - x.operacional / x.recebidas) > 1e-12) falhas.push(n + ' margem bruta'); if (Math.abs(x.mLiquida - x.financeiro / x.recebidas) > 1e-12) falhas.push(n + ' margem líquida'); if (Math.abs(x.mMkt - x.investido / x.recebidas) > 1e-12) falhas.push(n + ' margem mkt'); } };
      U.forEach(u => chk(u.custos.unidade, u.res)); chk('consolidado', R.res);
      if (R.res) ['recebidas', 'imposto', 'comissoes', 'reserva', 'fixo', 'provisao', 'custoOp', 'custoOpTotal', 'custos', 'operacional', 'investido', 'financeiro'].forEach(k => ok('consolidado ' + k + ' = Σ unidades', R.res[k], U.reduce((t, u) => t + u.res[k], 0)));
      ok('reserva = Σ unidades', R.reservaMkt, U.reduce((t, u) => t + u.reservaMkt, 0));
      // mínimos: menor 1ª parcela que zera o lucro bruto / cobre a reserva
      const lb = (rec, x) => r2(rec - r2(rec * REGRAS.imposto) - x.comissoes - x.custoOp);
      [['consolidado', R.res]].concat(U.map(u => [u.custos.unidade, u.res])).forEach(([n, x]) => { if (!x) return;
        const m = minimos(x.comissoes, x.custoOp, x.reserva);
        if (lb(m.empate, x) < 0 || lb(r2(m.empate - 0.01), x) >= 0) falhas.push(n + ' mínimo para não fechar no vermelho');
        if (lb(m.sustentavel, x) < x.reserva || lb(r2(m.sustentavel - 0.01), x) >= x.reserva) falhas.push(n + ' mínimo com reserva'); });
      // ROI
      const ro = R.roi; if (ro.invAtrib > 0) { if (Math.abs(ro.roi - (ro.retorno - ro.invAtrib) / ro.invAtrib) > 1e-12) falhas.push('ROI'); ok('retorno = Σ campanhas', ro.retorno, Object.values(ro.porCamp).reduce((t, g) => t + g.retorno, 0)); }
      // vitalício
      ok('vitalício = Σ contratos', R.vit.total, R.vit.contratos.reduce((t, x) => t + x.vit, 0));
      // ano
      const a = resumoAno(+R.mes.slice(0, 4)); a.meses.forEach(m => { if (m.resultado != null) { ok(m.mes + ' lucro bruto', m.resultado, m.recebidas - m.saiu); ok(m.mes + ' lucro líquido = bruto − investido', m.depois, m.resultado - (m.investido || 0)); } });
      // comissões exportadas
      const d = linhasComissao(); R.vendedores.forEach(v => { const pv = d.propostas.filter(x => x['Vendedor(a)'] === v.nome); if (pv.length) ok(v.nome + ' comissão exportada = Σ propostas', v.comissao, pv.reduce((t, x) => t + x['Comissão do vendedor (R$)'], 0)); });
      return { falhas, resumo: R.res ? { primeiraParcela: R.primeira, parcelasAnteriores: R.caixaAnt.total, aReceber: R.res.recebidas, impostos: R.res.imposto, custoOperacao: R.res.custoOp, custoOperacaoTotal: R.res.custoOpTotal, comissoes: R.res.comissoes, custosDoMes: R.res.custos, lucroBruto: R.res.operacional, margemBruta: +(R.res.mBruta * 100).toFixed(2), investido: R.res.investido, reserva: R.res.reserva, lucroLiquido: R.res.financeiro, margemLiquida: +(R.res.mLiquida * 100).toFixed(2), roi: R.roi.roi } : 'sem a receber' };
    });
    saida.push([f, r, errs]); await p.close();
  }
  saida.forEach(o => console.log(o[0], JSON.stringify(o[1], null, 1), o[2].length ? o[2] : ''));
  await b.close();
  process.exit(saida.some(o => o[1].falhas.length || o[2].length) ? 1 : 0);
})();
