#!/usr/bin/env python3
"""Envios de SMS (Kolmeya) do centro de custos NOVO OPTAS MOGI, jan–out/2026, transcritos dos relatórios mensais.
Gera data/investimentos-2026.json. Valor = envios × R$ 0,0530 (conferido linha a linha), arredondado ao centavo."""
import json, pathlib
from decimal import Decimal, ROUND_HALF_UP
L = """2026-01-22|1444984|44716|2369.948|22012026_SÃO PAULO_SEM-MEI_ARQ1_VALDECIR.csv
2026-01-27|1448918|47870|2537.110|EXP-2_SÃO PAULO_SEM MEI_AMIL_OPTAS MOGI.csv
2026-02-03|1455127|45329|2402.437|EXP-4_SÃO PAULO_SEM MEI_AMIL_OPTAS MOGI.csv
2026-02-05|1457576|53166|2817.798|VALDERCIR_ABC-E-GRANDE-SP_AMIL.csv
2026-02-24|1472490|57407|3042.571|BRASILIA-SEM-MEIexportacao1-empresaqui-19022026
2026-02-25|1473913|24259|1285.727|BRASILIA-SEM-MEIexportacao2-empresaqui-19022026
2026-02-26|1476074|12336|653.808|EXP-GUA-SEM-MEI-exportacao-empresaqui-26022026
2026-03-03|1479141|36784|1949.552|ABC E ALTO TIETE_SEM-MEI_exportacao-empresaqui-03032026
2026-03-10|1486153|55362|2934.186|SMS-VALDECIR-10-3-26.csv
2026-03-18|1494654|55180|2924.540|exportacao1-empresaqui-08032026
2026-03-24|1500029|45242|2397.826|exportacao2-empresaqui-08032026
2026-03-26|1502625|36478|1933.334|SMS VALDECIR - DDD11 exportacao1-empresaqui-07072025
2026-04-01|1507746|42023|2227.219|VALDECIR_SP_18-11-2025.csv
2026-04-09|1514140|57810|3063.930|exportacao1-empresaqui-01042026-hig.csv
2026-04-28|1529529|51453|2727.009|CAMPINAS E SP_VALDECIR.csv
2026-05-14|1541731|36419|1930.207|henrique_SÃO PAULO-SEM-MEI-ABERTAS DE 17012024 A 17092025
2026-05-19|1545008|39784|2108.552|sp valdecir - 2023 a 06-24.csv
2026-05-27|1551374|29711|1574.683|SMS VALDECIR 27:05 - MOGI 01:23 A 06:24.csv
2026-06-03|1556357|35920|1903.760|SMS- VALDECIR- 2023 A 2024 - 02 DE JUNHO.csv
2026-06-10|1560044|37621|1993.913|SMS - VALDECIR - JULHO 23 A JAN 25 - CLEAN.csv
2026-06-25|1571509|62051|3288.703|SMS - VALDECIR - 25-06 - TESTE LISTA KALYL.csv
2026-07-01|1574510|51474|2728.122|VALDECIR MOGI - 01-07.csv
2026-07-14|1582644|72210|3827.130|40CONSULTORIA_SP E BRASILIA.csv
2026-07-16|1582657|57893|3068.329|14072026_LISTA ALESSANDRO.csv
2026-07-22|1587796|42466|2250.698|HENRIQUE_americana-campinas-jundiai-mogi-sbc-sjc-sorocaba-TODOS_HIG.csv
2026-07-22|1587812|63996|3391.788|MASSA_sistema_kalyl.csv
2026-07-30|1592188|63147|3346.791|sms_w3g_20260729_1313.csv
2026-08-05|1596018|61106|3238.618|sms_w3g_20260805_1306.csv
2026-08-11|1599341|61309|3249.377|sms_w3g_20260811_0158.csv
2026-08-18|1603366|37385|1981.405|sms_w3g_zona-sul_20260817_1916.csv
2026-08-18|1603367|37652|1995.556|sms_w3g_20260817_1935.csv
2026-08-20|1605037|47000|2491.000|sulamerica-brasilia.csv
2026-08-20|1605038|18278|968.734|PORTO.csv
2026-08-26|1607575|29092|1541.876|sms_w3g_zona-sul_20260824_2113 (1).csv
2026-08-26|1608313|31185|1652.805|porto-26-08.csv
2026-09-10|1617760|33487|1774.811|AMIL - 10.09.csv
2026-10-07|1637869|44389|2352.617|SAO PAULO_SEM MEI_ABERTAS EM 01012025 A 30042026.csv"""
out, erros = [], []
for ln in L.splitlines():
    d, n, q, v, arq = ln.split('|')
    exato = Decimal(v)
    if Decimal(q) * Decimal('0.053') != exato: erros.append((n, q, v))
    out.append({'id': 'sms' + n, 'data': d, 'valor': float(exato.quantize(Decimal('0.01'), ROUND_HALF_UP)), 'valorExato': v,
                'categoria': 'SMS', 'campanha': 'SMS', 'unidade': 'Mogi', 'envios': int(q),
                'texto': 'Kolmeya #' + n + ' · ' + q + ' envios × R$ 0,0530 · ' + arq, 'origem': 'relatório Kolmeya'})
assert not erros, erros
# arredondamento por mês (maiores restos): a soma do mês = total exato do mês arredondado ao centavo
from collections import defaultdict
grupos = defaultdict(list)
for x in out: grupos[x['data'][:7]].append(x)
for g in grupos.values():
    ex = [Decimal(x['valorExato']) * 100 for x in g]; base = [int(e) for e in ex]
    alvo = int((sum(ex)).quantize(Decimal('1'), ROUND_HALF_UP)); resto = alvo - sum(base)
    ordem = sorted(range(len(g)), key=lambda i: ex[i] - base[i], reverse=True)
    for i in ordem[:resto]: base[i] += 1
    for x, b in zip(g, base): x['valor'] = b / 100
p = pathlib.Path(__file__).with_name('investimentos-2026.json')
p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
tot = {}
for x in out: tot[x['data'][:7]] = round(tot.get(x['data'][:7], 0) + x['valor'], 2)
print(len(out), 'lançamentos'); [print(k, f'{v:,.2f}') for k, v in sorted(tot.items())]; print('total', f"{sum(tot.values()):,.2f}")
