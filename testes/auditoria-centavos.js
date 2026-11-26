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
        ok(n + ' produção = projeto (Σ vendedores) + fora (ERP no mês atual)', u.producao, vs.reduce((t, v) => t + v.prodHap, 0) + (u.foraERP ? ERP.filter(c => c.data_venda.slice(0, 7) === R.mes && unidadeCanon(c.unidade) === n && statusProposta(c) !== 'cancelada').reduce((t, c) => t + c.valor_mensal, 0) : vs.reduce((t, v) => t + v.prodFora, 0)));
        if (u.foraERP) ok(n + ' 1ª parcela = projeto + fora do ERP', u.primeira, (u.primeiraProjeto || 0) + u.foraERP.primeira);
        ok(n + ' comissões = Σ vendedores', u.comissao, vs.reduce((t, v) => t + v.comissao, 0));
        vs.forEach(v => {
          // fora do projeto: faixa da unidade sobre a produção total, aplicada à produção fora · projeto: só 15%
          const f = faixaComissao(v.unidade, r2(v.prodHap + v.prodFora)); ok(v.nome + ' faixa', v.pct, f.pct); ok(v.nome + ' comissão fora', v.comFora, r2(v.prodFora * f.pct));
          ok(v.nome + ' 15% projeto', v.comProjeto, r2(v.prodHap * 0.15));
          if (v.vidasProjeto != null) { const vid = v.vidasFonte != null && !R.ag.propostas.length ? v.vidasFonte : R.ag.propostas.filter(p => projeto(p.c.projeto) && p.c.vendedor === v.nome).reduce((t, p) => t + (+p.c.vidas || 0), 0); ok(v.nome + ' vidas projeto', v.vidasProjeto, vid);
          }
          // Projeto Hapvida: vendedor recebe só 15% (premiação por vida vem do relatório W3G como custo)
          ok(v.nome + ' sem valor por vida na comissão', v.bonusVidas == null ? 0 : 1, 0);
          ok(v.nome + ' comissão total', v.comissao, v.comFora + v.comProjeto); }); });
      ok('produção = Σ unidades', R.producao, U.reduce((t, u) => t + u.producao, 0));
      ok('comissões = Σ unidades', R.comissoes, U.reduce((t, u) => t + u.comissao, 0));
      // propostas
      // propostas do mês: cada parcela = mensalidade × % da parcela da grade; 1ª parcela entra no mês
      const ps = R.ag.propostas.filter(p => p.aReceber != null);
      ps.forEach(p => { const rg = regraVenda(p.c); const taxa = rg.modalidade === 'ADESÃO' && !REGRAS.adesaoTaxaParaOptas; ok('1ª parcela ' + p.c.id_venda, p.aReceber, taxa ? 0 : r2(p.valor * rg.parc[0]));
        ok('total contratado ' + p.c.id_venda, p.agTotal, rg.parc.reduce((t, x, k) => t + (k === 0 && taxa ? 0 : r2(p.valor * x)), 0)); ok('próximas ' + p.c.id_venda, p.futuro, p.agTotal - p.aReceber); });
      if (ps.length) ok('1ª parcela do mês = Σ propostas', R.ag.valor, ps.reduce((t, p) => t + p.aReceber, 0));
      // parcelas de vendas anteriores, recalculadas de forma independente
      let ant = 0; carteiraCompleta().forEach(c => { const ini = String(c.data_venda || c.data_inicio || '').slice(0, 7); if (!ini || ini >= R.mes) return; if (/cancel/i.test(c.situacao || '') && (!c.cancelado_em || String(c.cancelado_em).slice(0, 7) <= R.mes)) return; const rg = regraVenda(c); if (!rg || rg.ag == null) return; const k = (+R.mes.slice(0, 4) - +ini.slice(0, 4)) * 12 + (+R.mes.slice(5, 7) - +ini.slice(5, 7)); if (rg.valores) { ant += rg.valores[k] || 0; return; } if (rg.parc[k] && !(k === 0 && rg.modalidade === 'ADESÃO' && !REGRAS.adesaoTaxaParaOptas)) ant += r2(r2(+c.valor_mensal) * rg.parc[k]); });
      ok('parcelas anteriores', R.caixaAnt.total, ant);
      U.forEach(u => { if (u.recebidas != null) ok(u.custos.unidade + ' a receber = 1ª parcela + anteriores + vitalício + outras receitas', u.recebidas, (u.primeira || 0) + (u.anteriores || 0) + (u.vitalicio || 0) + (u.outrasReceitas || 0)); });
      if (R.recebidas != null) { ok('a receber = 1ª parcela + anteriores + vitalício + outras receitas', R.recebidas, R.primeira + R.caixaAnt.total + R.vitalicio + U.reduce((t, u) => t + (u.outrasReceitas || 0), 0));
        { const v = R.vit, us = REGRAS.unidades; const esp = us.reduce((t, u) => t + (v.recebidoPorUnidade[u] || 0), 0) + (v.recebidoSemUnidade || 0);
          ok('vitalício no a receber = só o recebido', R.vitalicio, esp); } } // cada custo no mês a que se refere: "COMISSÃO NOVEMBRO 2025 - VALDECIR" → 2025-11; 13º sem mês pago em janeiro → dezembro anterior
      if (typeof EXTRATOS !== 'undefined' && EXTRATOS && EXTRATOS.creditos_debitos) EXTRATOS.creditos_debitos.forEach(c => { const d = norm(c.descricao).toUpperCase(); let m = null;
        const x = d.match(/VALDECIR/) && d.match(/(JANEIRO|FEVEREIRO|MARCO|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO) (20\d\d)/);
        if (x) m = x[2] + '-' + String(MESES_N.indexOf(x[1]) + 1).padStart(2, '0');
        if (/13.? SALARIO/.test(d) && +c.mes.slice(5, 7) <= 2) m = (+c.mes.slice(0, 4) - 1) + '-12';
        if (m && mesDevido(c) !== m) falhas.push('mês devido ' + c.descricao + ': ' + mesDevido(c) + ' ≠ ' + m); });
      if (R.recebidas != null) { ok('1ª parcela = Σ unidades', R.primeira, U.reduce((t, u) => t + (u.primeira || 0), 0)); }
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
      U.forEach(u => ok(u.custos.unidade + ' comissão no resultado (0 com folha do extrato ou média)', u.res ? u.res.comissoes : 0, u.res ? (u.custos.fonteCustos !== 'estrutura' ? 0 : u.comissao) : 0));
      ok('reserva = Σ unidades', R.reservaMkt, U.reduce((t, u) => t + u.reservaMkt, 0));
      // mínimos: menor 1ª parcela que zera o lucro bruto / cobre a reserva
      // imposto (26/11/2026): parte com desconto W3G (proporção do bruto das linhas com despesa adm. no mês/unidade) = 8,5% W3G + 8,5%; resto = 15%
      const imp = (rec, mes, u) => { let b = 0, d = 0; (extratosOn() ? EXTRATOS.linhas : []).forEach(l => { if (l.mes !== mes || !(l.pct_adm > 0) || (u && unidadeCanon(l.unidade) !== u)) return; b += l.bruto; d -= l.desp_adm; });
        b = r2(b); d = r2(d); const com = Math.min(b, Math.max(rec, 0)), sem = r2(rec - com), w = b ? r2(d * com / b) : 0; return r2(w + r2((com - w) * 0.085) + r2(sem * 0.15)); };
      U.forEach(u => { if (u.res) ok(u.custos.unidade + ' imposto (% Adm. 8,5%: desconto W3G + 8,5% sobre o que sobrou · 0%: 15%)', u.res.imposto, imp(u.recebidas, R.mes, u.custos.unidade)); });
      Object.keys(ESTADO.fechamentos).forEach(k => { const f = ESTADO.fechamentos[k]; if (!f.base) return; REGRAS.unidades.forEach(u => { const x = f.unidades[u]; if (x && x.recebidas != null) ok(k + ' ' + u + ' imposto', x.imposto, imp(x.recebidas, k, u)); }); if (f.recebidas != null) ok(k + ' imposto = Σ unidades', f.imposto, REGRAS.unidades.reduce((t, u) => t + (f.unidades[u].imposto || 0), 0)); });
      [['consolidado', R.res, undefined]].concat(U.map(u => [u.custos.unidade, u.res, u.custos.unidade])).forEach(([n, x, un]) => { if (!x) return;
        const lb = rec => r2(rec - imp(rec, R.mes, un) - x.comissoes - x.custoOp);
        const m = minimos(x.comissoes, x.custoOp, x.reserva, R.mes, un);
        if (lb(m.empate) < 0 || lb(r2(m.empate - 0.01)) >= 0) falhas.push(n + ' mínimo para não fechar no vermelho');
        if (lb(m.sustentavel) < x.reserva || lb(r2(m.sustentavel - 0.01)) >= x.reserva) falhas.push(n + ' mínimo com reserva'); });
      // ERP: cada mês base = 1ª parcela das cadastradas + anteriores + vitalício, por unidade e consolidado
      if (!DEMO && ERP.length) Object.keys(ESTADO.fechamentos).filter(k => ESTADO.fechamentos[k].fonte === 'ERP').forEach(k => { const f = ESTADO.fechamentos[k];
        REGRAS.unidades.forEach(u => { const x = f.unidades[u]; ok(k + ' ' + u + ' a receber ERP', x.recebidas, x.primeira + x.anteriores + x.vitalicio + (x.outrasReceitas || 0)); ok(k + ' ' + u + ' outras receitas', x.outrasReceitas || 0, lancExtratos(k, u).receitas);
          const cad = ERP.filter(c => c.data_venda.slice(0, 7) === k && unidadeCanon(c.unidade) === u && statusProposta(c) !== 'cancelada');
          ok(k + ' ' + u + ' produção ERP', x.producao, cad.reduce((t, c) => t + c.valor_mensal, 0)); ok(k + ' ' + u + ' 1ª parcela ERP', x.primeira, cad.reduce((t, c) => t + valorParcelaERP(c, 0, c.tabela.valores[0] || 0), 0)); });
        ok(k + ' a receber ERP = Σ unidades', f.recebidas, REGRAS.unidades.reduce((t, u) => t + f.unidades[u].recebidas, 0)); });
      // extratos: cada extrato fecha (linhas = ato + parcelas; acumulado + comissões + créd/déb = líquido)
      // livro do a receber: cada parcela recebida = Σ linhas do extrato; perdida = mais de 90 dias depois da prevista; previstas encadeadas de 30 em 30 dias
      if (!DEMO && ERP.length && extratosOn()) { const Lv = livroReceber(), hoje = hojeISO();
        Lv.itens.forEach(it => { const id = it.c.id + '|' + it.parcela;
          if (it.situacao === 'recebida') ok('livro ' + id + ' recebido', it.valor, EXTRATOS.linhas.filter(l => l.erp === it.c.id && l.parc === it.parcela).reduce((t, l) => t + l.bruto, 0));
          else { if (it.c.tabela.venc && it.c.tabela.venc[it.parcela - 1] && it.prevista !== it.c.tabela.venc[it.parcela - 1]) falhas.push('livro ' + id + ' prevista ≠ vencimento SisWeb'); const d = diasEntre(it.prevista, hoje); if ((d <= 0 ? 'em dia' : d < 90 ? 'atrasada' : 'perdida') !== it.situacao) falhas.push('livro ' + id + ' situação'); } });
        const dp = deParaERP(), tudo = Lv.itens.reduce((t, it) => t + it.valor, 0); ok('livro = recebidas + em dia + atrasadas + perdidas', tudo, dp.vPagas + dp.vEmDia + dp.vAtrasadas + dp.vPerdidas);
        const ar = itensAReceber(); ok('aba A receber = em dia + atrasadas (+ projeto)', ar.reduce((t, x) => t + x.valor, 0), dp.vEmDia + dp.vAtrasadas + ar.filter(x => x.tipo === 'projeto').reduce((t, x) => t + x.valor, 0)); }
      if (extratosOn()) EXTRATOS.extratos.forEach(x => { const L = EXTRATOS.linhas.filter(l => l.extrato === x.codigo), C = EXTRATOS.creditos_debitos.filter(c => c.extrato === x.codigo);
        ok('extrato ' + x.codigo + ' linhas', L.reduce((t, l) => t + l.liquido, 0), x.comissoes_liquido); ok('extrato ' + x.codigo + ' créd/déb', C.reduce((t, c) => t + c.liquido, 0), x.creditos_debitos);
        ok('extrato ' + x.codigo + ' líquido', x.acumulado + x.comissoes_liquido + x.creditos_debitos, x.liquido); });
      // créditos/débitos: receitas e custos por tipo, unidade e mês = soma independente dos lançamentos
      if (extratosOn()) { const meses = [...new Set(EXTRATOS.creditos_debitos.map(c => mesDevido(c)).concat(Array.from({ length: 12 }, (_, i) => '2026-' + String(i + 1).padStart(2, '0'))))];
        meses.forEach(m => REGRAS.unidades.forEach(u => { const cs = EXTRATOS.creditos_debitos.filter(c => mesDevido(c) === m && unidadeCanon(c.unidade) === u), lx = lancExtratos(m, u);
          ok(m + ' ' + u + ' receitas dos extratos', lx.receitas, cs.filter(c => /receita|custo/.test(tipoCD(c.descricao)[3]) && c.liquido >= 0).reduce((t, c) => t + c.liquido, 0));  // regra do sinal: sem sinal = a receber
          ok(m + ' ' + u + ' custos dos extratos', lx.custos, -cs.filter(c => /receita|custo/.test(tipoCD(c.descricao)[3]) && c.liquido < 0).reduce((t, c) => t + c.liquido, 0));  // "-" = custo
          const cu = custosUnidade(u, m), real = cs.some(c => tipoCD(c.descricao)[0] === 'A');
          ok(m + ' ' + u + ' folha dos extratos', lx.folha, -cs.filter(c => tipoCD(c.descricao)[3] === 'folha').reduce((t, c) => t + c.liquido, 0));
          const med = cu.fonteCustos === 'media';
          ok(m + ' ' + u + ' custo fixo (' + (real ? 'folha real + extratos' : med ? 'média 3 meses + extratos' : 'estrutura + extratos') + ')', cu.fixo, real ? lx.folha + lx.custos : med ? lx.folha + cu.media + lx.custos : cu.fixoEstrutura + lx.custos);
          if (med) { const ms = []; for (let i = 1; i <= 36 && ms.length < 3; i++) { const d = new Date(+m.slice(0, 4), +m.slice(5, 7) - 1 - i, 1), k = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0'), v = lancExtratos(k, u).salario; if (v) ms.push(v); }
            for (let i = 1; i <= 36 && ms.length < 3; i++) { const d = new Date(+m.slice(0, 4), +m.slice(5, 7) - 1 + i, 1), k = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0'), v = lancExtratos(k, u).salario; if (v) ms.push(v); }
            ok(m + ' ' + u + ' salário = média de 3 meses registrados', cu.mediaSalario.valor, r2(ms.reduce((t, v) => t + v, 0) / ms.length));
            if (lx.salario) falhas.push(m + ' ' + u + ' média usada com salário registrado'); }
          if (real && cu.provisao !== 0) falhas.push(m + ' ' + u + ' provisão deveria ser zero com folha real'); }));
        const semTipo = EXTRATOS.creditos_debitos.filter(c => tipoCD(c.descricao)[0] === '?'); if (semTipo.length) falhas.push(semTipo.length + ' crédito(s)/débito(s) sem classificação'); }
      // reserva: saldo dos meses anteriores e limite
      { const an = Object.keys(ESTADO.fechamentos).filter(k => k.slice(0, 4) === R.mes.slice(0, 4) && k < R.mes && ESTADO.fechamentos[k].producao != null);
        ok('saldo de reserva anterior', R.reservaAnterior, an.reduce((t, k) => t + ESTADO.fechamentos[k].reserva - (ESTADO.fechamentos[k].investido || 0), 0));
        ok('limite = reserva + saldo', R.roi.reserva, R.reservaMkt + R.reservaAnterior); }
      // investimentos reais de SMS (Mogi) por mês = total do relatório
      if (!DEMO) { const tot = { '2026-01': 4907.06, '2026-02': 10202.34, '2026-03': 12139.44, '2026-04': 8018.16, '2026-05': 5613.44, '2026-06': 7186.38, '2026-07': 18612.86, '2026-08': 17119.37, '2026-09': 1774.81, '2026-10': 2352.62 };
        Object.keys(tot).forEach(m => { ok('SMS ' + m, ESTADO.investimentos.filter(i => i.data.slice(0, 7) === m).reduce((t, i) => t + i.valor, 0), tot[m]); const f = ESTADO.fechamentos[m]; if (f) ok('Ano ' + m + ' investido', f.investido, tot[m]); }); }
      // ROI
      const ro = R.roi;
      if (ro.modo === 'geral') { ok('ROI geral investido = investido do mês', ro.invAtrib, R.investido);
        const rts = REGRAS.unidades.map(u => R.unidades[u].primeira); if (rts.some(x => x != null)) ok('ROI geral retorno = Σ 1ª parcela das unidades', ro.retorno, rts.reduce((t, x) => t + (x || 0), 0));
        if (R.ag.base) ok('ROI geral retorno = 1ª parcela de todas as vendas (projeto + fora do SisWeb)', ro.retorno, R.ag.valor + REGRAS.unidades.reduce((t, u) => t + (R.unidades[u].foraERP ? R.unidades[u].foraERP.primeira : 0), 0));
        if (ro.invAtrib > 0 && ro.retorno != null && Math.abs(ro.roi - (ro.retorno - ro.invAtrib) / ro.invAtrib) > 1e-12) falhas.push('ROI geral');
        REGRAS.unidades.forEach(u => { const x = ro.porUnidade[u]; ok(u + ' ROI investido', x.investido, R.invUnidade[u]); }); }
      else if (ro.invAtrib > 0) { if (Math.abs(ro.roi - (ro.retorno - ro.invAtrib) / ro.invAtrib) > 1e-12) falhas.push('ROI'); ok('retorno = Σ campanhas', ro.retorno, Object.values(ro.porCamp).reduce((t, g) => t + g.retorno, 0)); }
      // vitalício
      ok('vitalício = Σ contratos', R.vit.total, R.vit.contratos.reduce((t, x) => t + x.vit, 0));
      if (R.vit.recebido != null) { ok('vitalício recebido = Σ por operadora', R.vit.recebido, Object.keys(R.vit.porOp).reduce((t, k) => t + (R.vit.porOp[k].recebido || 0), 0));
        if (extratosOn()) { const L = EXTRATOS.linhas.filter(l => l.mes === R.mes && l.tipo === 'vitalicio'); ok('vitalício recebido = Σ linhas dos extratos', R.vit.recebido, L.reduce((t, l) => t + l.bruto, 0)); ok('mensalidades do vitalício = Σ linhas', R.vit.mensalRec, L.reduce((t, l) => t + l.vl_parcela, 0)); } }
      // ano
      const a = resumoAno(+R.mes.slice(0, 4)); a.meses.forEach(m => { if (m.resultado != null) { ok(m.mes + ' lucro bruto', m.resultado, m.recebidas - m.saiu); ok(m.mes + ' lucro líquido = bruto − investido', m.depois, m.resultado - (m.investido || 0)); } });
      // detalhe dos custos (aba Ano): Σ itens = custos do mês, por unidade e no total
      // entradas e saídas: Σ categorias = a receber e custos de cada unidade; resultado = lucro bruto guardado
      Object.keys(ESTADO.fechamentos).forEach(m => { const f = fluxoMes(m), d = ESTADO.fechamentos[m]; if (!f || d.resultado == null) return; REGRAS.unidades.forEach(u => {
        ok(m + ' ' + u + ' entradas = Σ categorias', f.ent.un[u], f.ent.cats.reduce((t, g) => t + (g.un[u] || 0), 0)); ok(m + ' ' + u + ' saídas = Σ categorias', f.sai.un[u], f.sai.cats.reduce((t, g) => t + (g.un[u] || 0), 0));
        if (d.unidades[u].recebidas != null) ok(m + ' ' + u + ' entradas = a receber', f.ent.un[u], d.unidades[u].recebidas); if (d.unidades[u].saiu != null) ok(m + ' ' + u + ' saídas = custos', f.sai.un[u], d.unidades[u].saiu); });
        ok(m + ' resultado do quadro = lucro bruto', f.ent.total - f.sai.total, d.resultado); });
      // ano: Σ unidades = total (bruto, investido e líquido); líquido = bruto − investido
      { const t = resumoAno(+R.mes.slice(0, 4)); if (t.nRec) { const us = REGRAS.unidades.map(u => t.unidades[u]);
        ok('ano lucro bruto = Σ unidades', t.resultado, us.reduce((a, x) => a + x.resultado, 0)); ok('ano lucro líquido = Σ unidades', t.depois, us.reduce((a, x) => a + x.depois, 0));
        ok('ano investido = Σ unidades', t.investidoTotal, us.reduce((a, x) => a + x.investido, 0)); ok('ano líquido = bruto − investido', t.depois, t.resultado - t.investidoTotal);
        us.forEach((x, k) => ok(REGRAS.unidades[k] + ' ano líquido = bruto − investido', x.depois, x.resultado - x.investido)); } }
      // a receber detalhado: Σ de onde vem = a receber guardado do mês, por unidade
      Object.keys(ESTADO.fechamentos).forEach(m => { const rd = receberDetalhe(m); if (!rd) return; REGRAS.unidades.forEach(u => { const x = rd.unidades[u]; if (x.guardado != null) ok(m + ' ' + u + ' a receber detalhado', x.total, x.guardado); ok(m + ' ' + u + ' Σ linhas do a receber', x.total, x.linhas.reduce((t, l) => t + l.valor, 0)); }); });
      Object.keys(ESTADO.fechamentos).forEach(m => { const f = ESTADO.fechamentos[m]; if (f.resultado == null || f.exemplo) return; const cd = custoDetalhe(m); if (!cd) return;
        REGRAS.unidades.forEach(u => { const x = f.unidades[u]; if (x && x.saiu != null) ok(m + ' ' + u + ' detalhe dos custos = custos do mês', cd.unidades[u].total, x.saiu); });
        ok(m + ' detalhe dos custos total', cd.total, f.saiu); });
      // cancelar proposta atrasada: parcelas não recebidas saem do a receber; desfazer volta ao que era
      if (!DEMO && ERP.length) { const at = livroReceber().itens.filter(it => it.situacao === 'atrasada')[0];
        if (at) { const antes = R.recebidas, antesT = itensAReceber().reduce((t, x) => t + x.valor, 0), bak = JSON.stringify(ESTADO.cancelados || {});
          const naoRec = livroReceber().itens.filter(it => it.c.id === at.c.id && (it.situacao === 'atrasada' || it.situacao === 'em dia'));
          ESTADO.cancelados = Object.assign({}, ESTADO.cancelados, { [at.c.id]: { data: '2026-11-25' } }); _livro = null; calcular();
          ok('cancelada: sai do a receber exatamente o não recebido', antesT - itensAReceber().reduce((t, x) => t + x.valor, 0), naoRec.reduce((t, x) => t + x.valor, 0));
          if (livroReceber().itens.some(it => it.c.id === at.c.id && it.situacao !== 'recebida' && it.situacao !== 'cancelada')) falhas.push('cancelada: sobrou parcela em aberto');
          ESTADO.cancelados = JSON.parse(bak); _livro = null; calcular(); ok('desfazer cancelamento volta ao a receber', R.recebidas, antes); } }
      // comissões exportadas
      const d = linhasComissao(); R.vendedores.forEach(v => { const pv = d.propostas.filter(x => x['Vendedor(a)'] === v.nome); if (pv.length) ok(v.nome + ' comissão exportada = Σ propostas', v.comissao, pv.reduce((t, x) => t + x['Comissão do vendedor (R$)'], 0)); });
      // aba Vitalício: carteira por unidade e composição do ano
      if (extratosOn()) { const ano = R.mes.slice(0, 4);
        for (let m = 1; m <= 12; m++) { const k = ano + '-' + String(m).padStart(2, '0'); if (k > R.mes) break; let n = 0, men = 0;
          REGRAS.unidades.forEach(u => { const x = carteiraMes(k, u); ok(k + ' ' + u + ' parcelas = contratos + acumuladas', x.parcelas, x.contratos + x.acumuladas); n += x.parcelas; men += x.mensalParcelas; });
          const v = calcVitalicio(k); if (v.recebido != null) { ok(k + ' carteira: parcelas = vitalício do mês', n, v.linhas); ok(k + ' carteira: mensalidades = vitalício do mês', men, v.mensalRec); } }
        const c = composicaoAno(+ano), L = EXTRATOS.linhas.filter(l => l.mes.slice(0, 4) === ano && l.mes <= R.mes);
        ok('composição: parcelas = Σ linhas', c.n, L.length); ok('composição: mensalidades = Σ linhas', c.mensal, L.reduce((t, l) => t + l.vl_parcela, 0)); ok('composição: comissão = Σ linhas', c.liquido, L.reduce((t, l) => t + l.liquido, 0));
        ok('composição: vitalício = Σ linhas de vitalício', c.grupos[4].liquido, L.filter(l => l.tipo === 'vitalicio').reduce((t, l) => t + l.liquido, 0)); }
      return { falhas, resumo: R.res ? { primeiraParcela: R.primeira, parcelasAnteriores: R.caixaAnt.total, aReceber: R.res.recebidas, impostos: R.res.imposto, custoOperacao: R.res.custoOp, custoOperacaoTotal: R.res.custoOpTotal, comissoes: R.res.comissoes, custosDoMes: R.res.custos, lucroBruto: R.res.operacional, margemBruta: +(R.res.mBruta * 100).toFixed(2), investido: R.res.investido, reserva: R.res.reserva, lucroLiquido: R.res.financeiro, margemLiquida: +(R.res.mLiquida * 100).toFixed(2), roi: R.roi.roi } : 'sem a receber' };
    });
    saida.push([f, r, errs]); await p.close();
  }
  saida.forEach(o => console.log(o[0], JSON.stringify(o[1], null, 1), o[2].length ? o[2] : ''));
  await b.close();
  process.exit(saida.some(o => o[1].falhas.length || o[2].length) ? 1 : 0);
})();
