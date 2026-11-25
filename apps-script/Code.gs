/**
 * OPTAS · Painel gerencial inteligente — backend Google Apps Script
 *
 * Implantação:
 *  1. Neste MESMO projeto do painel TV atual (onde existe a função tvDadosWeb),
 *     adicione este arquivo (Code.gs → renomeie para Optas.gs se já existir um Code.gs)
 *     e o arquivo Index.html (gerado por build.py).
 *  2. Propriedades do script (Configurações do projeto → Propriedades do script):
 *       OPTAS_KEY     = chave de acesso exigida na URL (?k=...)
 *       OPTAS_TV_KEY  = chave usada hoje em tvDadosWeb('gerencial', <chave>)
 *       OPTAS_PLANILHA_LEADS = ID da planilha "Leads GNDI" (opcional; sem ela usa a planilha ativa)
 *  3. Implantar → Nova implantação → App da Web.
 *     URL de acesso: .../exec?k=<OPTAS_KEY>
 */

var OPTAS_ESTADO_PREFIXO = 'optas_estado_';
var OPTAS_CHUNK = 8000; // limite de 9 KB por propriedade

function doGet(e) {
  var props = PropertiesService.getScriptProperties();
  var chave = props.getProperty('OPTAS_KEY');
  if (!chave || !e || !e.parameter || e.parameter.k !== chave) {
    return HtmlService.createHtmlOutput('<p style="font-family:sans-serif">Acesso não autorizado.</p>');
  }
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('OPTAS · Painel gerencial inteligente')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/** Dados integrados + estado salvo (investimentos, recebidas, contratos). */
function optasCarregar() {
  return JSON.stringify({ dados: optasDadosIntegrados_(), estado: optasEstadoLer_() });
}

/**
 * Fonte integrada: reutiliza a função do painel gerencial atual.
 * Deve devolver o mesmo formato de tvDadosWeb('gerencial', ...):
 * { rotulo, atualizado, geral:{hap,fora}, equipes:[...], vendedores:[{nome,equipe,hap,proj,fora,meta}] }
 */
function optasDadosIntegrados_() {
  try {
    if (typeof tvDadosWeb === 'function') {
      var k = PropertiesService.getScriptProperties().getProperty('OPTAS_TV_KEY');
      var d = tvDadosWeb('gerencial', k);
      d = typeof d === 'string' ? JSON.parse(d) : d;
      try { optasVidasProjeto_(d); } catch (e2) { console.error('optasVidasProjeto_: ' + e2); }
      return d;
    }
  } catch (err) {
    console.error('optasDadosIntegrados_: ' + err);
  }
  return null; // o painel usa o snapshot embutido e sinaliza a indisponibilidade
}

/**
 * Vidas do Projeto Hapvida por vendedor no mês vigente, lidas da aba "Painel de Implantação":
 * vidas = só as IMPLANTADAS no mês (data da Hapvida) — decisão de 25/11/2026. Equipe Gileade não conta.
 * Grava em cada vendedor do tvDadosWeb o campo vidasHap (casando "Wanderleia G." com "Wanderleia Gugel Soares").
 */
function optasVidasProjeto_(d) {
  if (!d || !d.vendedores) return;
  var id = PropertiesService.getScriptProperties().getProperty('OPTAS_PLANILHA_LEADS');
  var ss = id ? SpreadsheetApp.openById(id) : SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss && ss.getSheetByName('Painel de Implantação'); if (!sh) return;
  var v = sh.getDataRange().getDisplayValues();
  var ini = -1;
  for (var r = 0; r < 5 && ini < 0; r++) for (var c = 0; c < v[r].length; c++) if (/VIGENTE/i.test(v[r][c])) { ini = c; break; }
  if (ini < 0) return;
  var num = function (x) { var n = parseInt(String(x).replace(/\D/g, ''), 10); return isNaN(n) ? 0 : n; };
  var chave = function (n) { var p = String(n).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/\./g, ' ').split(/\s+/).filter(String); return p[0] + ' ' + (p[1] ? p[1][0] : ''); };
  var vidas = {};
  v.forEach(function (row) {
    var nome = row[0]; if (!nome || /^(EQUIPE|TOTAL|Vendedor)/i.test(nome)) return;
    vidas[chave(nome)] = num(row[ini + 8]);   // Implantado (vidas)
  });
  d.vendedores.forEach(function (x) { var k = chave(x.nome); if (vidas[k] != null) x.vidasHap = vidas[k]; });
}

function optasEstadoSalvar(json) {
  JSON.parse(json); // valida
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var props = PropertiesService.getScriptProperties();
    var n = Number(props.getProperty(OPTAS_ESTADO_PREFIXO + 'n') || 0);
    for (var i = 0; i < n; i++) props.deleteProperty(OPTAS_ESTADO_PREFIXO + i);
    var partes = {};
    var total = Math.ceil(json.length / OPTAS_CHUNK);
    for (var j = 0; j < total; j++) partes[OPTAS_ESTADO_PREFIXO + j] = json.substr(j * OPTAS_CHUNK, OPTAS_CHUNK);
    partes[OPTAS_ESTADO_PREFIXO + 'n'] = String(total);
    partes[OPTAS_ESTADO_PREFIXO + 'em'] = new Date().toISOString();
    props.setProperties(partes, false);
    return true;
  } finally {
    lock.releaseLock();
  }
}

function optasEstadoLer_() {
  var props = PropertiesService.getScriptProperties();
  var n = Number(props.getProperty(OPTAS_ESTADO_PREFIXO + 'n') || 0);
  if (!n) return null;
  var s = '';
  for (var i = 0; i < n; i++) s += props.getProperty(OPTAS_ESTADO_PREFIXO + i) || '';
  return s;
}
