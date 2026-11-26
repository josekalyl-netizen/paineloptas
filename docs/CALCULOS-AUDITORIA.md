# Painel OPTAS — Memória de cálculo para auditoria

**Versão do sistema:** v4.5 · 26/11/2026 · **Período:** janeiro a novembro de 2026 · **Unidades:** Consolação e Mogi

Este documento descreve **todos** os cálculos do painel: de onde vem cada número, qual fórmula é usada e a que ele se refere. No fim estão os números de cada mês, com as somas, para conferência.

Convenções:

- Valores em reais (R$).
- "−" indica saída.
- "Relatório" é o relatório de pagamento do SisWeb (W3G), aquele que a Optas recebe todo dia 5.

**Resultado 2026 (jan–nov), como está no painel:**

| | Consolação | Mogi | **Total** |
|---|--:|--:|--:|
| A receber | 446.655,73 | 516.709,38 | **963.365,11** |
| Saídas (custos + provisão + imposto) | 465.297,64 | 489.525,88 | **954.823,52** |
| Lucro bruto | −18.641,91 | 27.183,50 | **8.541,59** |
| Investido em marketing | 0,00 | 87.926,48 | **87.926,48** |
| Lucro líquido | −18.641,91 | −58.373,03 | **−77.014,94** |

---

## 1. Fontes de dados

| Fonte | O que traz | Quantidade usada |
|---|---|---|
| **Relatórios de pagamento do SisWeb (W3G)** | Linha a linha: proposta, operadora, parcela, % Adm., bruto, desconto adm. e **Líquido**. Também traz a seção **Créditos e Débitos** (salários, benefícios, campanhas, estornos, boletos etc.) e o cabeçalho (nº do relatório, data de geração, previsão de pagamento, acumulado) | 23 relatórios (21 de 2026 e 2 de Mogi de 2025, que não entram em 2026) · 3.816 linhas de comissão · 231 créditos/débitos |
| **Propostas do SisWeb** | Proposta, operadora, modalidade (PF/PME/Adesão), mensalidade, vidas, data de cadastro, situação e comissão da Optas por parcela | 358 propostas |
| **Painel gerencial (PipeRun + ASI)** | Produção do **Projeto Hapvida** por vendedor no mês atual (instantâneo de 23/11/2026) | só o mês atual (novembro) |
| **Investimentos em marketing** | Lançamentos (data, valor, categoria, unidade). Ex.: envios de SMS Kolmeya | 37 lançamentos · R$ 87.926,48 em 2026 |
| **Parâmetros informados pela Optas** | Salários, VR, VT, custo operacional, encargos, faixas de comissão, grade de comissão das operadoras, imposto | ver seção 2 |

Os dados de clientes (nomes, CPF/CNPJ, telefones) ficam só no arquivo do sistema e não estão neste documento.

---

## 2. Parâmetros fixos

| Parâmetro | Consolação | Mogi | Uso |
|---|--:|--:|---|
| Salários brutos (inclui PJ da sócia) | 15.315,76 | 10.521,33 | Estrutura (só sem relatório nenhum) e base da provisão |
| PJ da sócia (já dentro dos salários) | 10.000,00 | 5.000,00 | Sai da base da provisão |
| **Base CLT da provisão** (salários − PJ) | **5.315,76** | **5.521,33** | Provisão de 13º e férias |
| Pessoas CLT | 5 | 4 | VR/VT por pessoa |
| Vale-refeição (out/2026) | 4.140,40 | 3.640,40 | Estrutura · dividido pelos dias úteis de out/2026 |
| Vale-transporte (out/2026) | 1.576,24 | 1.691,30 | Estrutura · idem |
| **Custo operacional** (aluguel, água, luz, internet) | 0,00 | **2.300,00** | Soma todo mês: não vem no relatório |
| Encargos sobre 13º e férias | 34,8% | 34,8% | INSS patronal 20% + RAT 1% + Terceiros 5,8% + FGTS 8% |
| Imposto sobre linha **com** desconto da W3G (% Adm. > 0; a W3G paga metade) | 6,5% | 6,5% | Imposto |
| Imposto sobre o **resto** | 15% | 15% | Imposto |
| Reserva de marketing | 15% da produção | 15% da produção | Informativo / mínimo sustentável |
| Faixas de comissão do vendedor (sobre a produção total do mês) | 30% até 4.999,99 · 50% a partir de 5.000 | 20% · 25% (3.000) · 30% (6.000) · 40% (9.000) · 50% (12.000) | Comissão do vendedor |
| Projeto Hapvida (Optas recebe) | 100% da 1ª mensalidade, sem vitalício | idem | 1ª parcela no mês sem relatório |
| Projeto Hapvida (vendedor recebe) | 15% da mensalidade + R$ 20/vida a partir de 25 vidas, R$ 25 a partir de 35 e R$ 35 a partir de 50 | idem | Comissão do vendedor |

**Arredondamento.** Todo valor é arredondado ao centavo em cada etapa (meio centavo para cima). Somas são feitas em centavos, então o total é sempre igual à soma das partes. Quando um valor sem unidade precisa ser dividido entre as unidades, o rateio é feito pelos maiores restos: não sobra nem falta centavo.

---

## 3. Mês de referência e situação de cada mês

**Mês de referência de um relatório = mês da data de previsão de pagamento.**

- O relatório 424786 tem previsão em 05/05/2026, então é de maio/2026, mesmo tendo sido gerado em 10/08/2026.
- Quando há dois relatórios no mesmo mês, os dois somam. Foi o caso da Consolação em março/2026 (420722 e 420789).

Cada unidade, em cada mês, fica em uma de três situações:

| Situação | Quando | Como calcula |
|---|---|---|
| **Relatório** | Existe relatório da unidade com previsão no mês | Vale **só o relatório** (seção 4) + custo operacional + provisão + imposto |
| **Coberto pelo relatório seguinte** | Não há relatório no mês, mas há relatório depois (o seguinte já traz o que seria deste mês) | A receber = 0 · imposto = 0 · saídas = gastos com o mês escrito na descrição (vêm no relatório seguinte, seção 4.2) + custo operacional + provisão. Hoje: **Consolação, outubro/2026** |
| **Estimativa** | Depois do último relatório da unidade | Seção 5. Hoje: **Mogi, novembro/2026** |

Os relatórios de Mogi de 2025 (422414 e 422415) não entram nas contas de 2026, a não ser algum débito deles com mês escrito de 2026 (seção 4.2).

---

## 4. Mês com relatório — a regra

**Regra do relatório (decisão da Optas, sem exceções):** no relatório, cada linha conta pelo **Líquido** (última coluna):

- **valor positivo = entrada (a receber)**
- **valor com "−" = saída (custo)**

Vale para as linhas de comissão e para todos os Créditos e Débitos, seja o que for:

- salário, benefícios, férias, 13º e rescisão;
- vales, boletos, estornos, adiantamentos e SMS;
- campanhas, acertos, retiradas e aluguel.

Linha com Líquido R$ 0,00 não conta. São 7 linhas: a 1ª parcela de adesão retida, que não veio para a Optas.

### 4.1 Entradas (a receber), por categoria

| Categoria | O que entra |
|---|---|
| 1ª parcela | Líquido positivo das linhas de comissão com parcela = 1 |
| Parcelas seguintes | Líquido positivo das linhas com parcela ≥ 2 |
| Vitalício | Líquido positivo das linhas marcadas como vitalício |
| Créditos | Todo valor positivo da seção Créditos e Débitos (campanhas, premiações, acertos, devoluções de desconto, estornos devolvidos, departamento de seguros, retiradas, aluguel etc.) |
| **A receber** | 1ª parcela + parcelas seguintes + vitalício + créditos |

### 4.2 Saídas do relatório — cada gasto no mês dele

**Valores com "−" nos relatórios** = soma, em módulo, de todo Líquido negativo: linhas de comissão negativas e débitos.

**Mês devido (pedido da Optas, 26/11/2026: "cada gasto no seu devido mês, conforme ele se identifica"):** o débito vai para o mês escrito na descrição, venha no relatório que vier. As entradas (valores positivos) continuam no mês do relatório.

| Tipo de débito | Como o mês é lido | Exemplo |
|---|---|---|
| Salário, benefícios, férias, rescisão | nome do mês na descrição; sem nome, a data dd/mm | "SALÁRIOS - AGOSTO" (relatório de setembro) → agosto · "SALÁRIO - JOANA 07/09" → setembro |
| Comissão Valdecir 40% | nome do mês | "COMISSÃO NOVEMBRO 2025" (relatório de jan/26) → nov/25 |
| Vale, AD de comissão com folha negativa | data dd/mm | "VALE - 07/01" (relatório de fev/26) → jan/26 |
| 13º sem mês, pago em janeiro ou fevereiro | dezembro do ano anterior | Mogi, jan/26 → dez/25 |
| Todo o resto (boletos, estornos, AD de parcela, campanhas, 10%, taxa) e débito sem mês escrito | mês do relatório | — |

Sem ano escrito, vale o mês mais recente até o do relatório. Gasto que cai em 2025 sai de 2026.

**Salário ou benefício que ainda não chegou:** como o salário é pago no relatório do mês seguinte, o último mês ainda não tem o seu. Nesse mês entra a **média dos últimos 3 meses** (marcada como estimativa), trocada pelo valor real quando o relatório chegar. Hoje: Consolação nov/26 (salário); Mogi set/26 e out/26 (salário e benefícios).

**Conferência:** a soma dos gastos de todos os meses (sem as estimativas) é igual à soma de todos os "−" de todos os relatórios, por unidade. Nada some e nada conta duas vezes.


**O salário não é descontado de novo.** O SisWeb já tira salário, benefícios, férias, 13º etc. do valor que a Optas recebe, e o painel usa exatamente esses valores do relatório.

### 4.3 Prova de que o painel usa o valor do SisWeb

Para cada relatório:

> **A receber − valores com "−" = Comissões (líquido) + Créditos e Débitos do relatório**

É o valor do mês que a Optas recebe, antes do **acumulado**. O acumulado é o saldo de meses anteriores que o SisWeb carrega para o relatório seguinte. Ele não entra no mês para não contar duas vezes, porque cada mês já entrou no seu próprio relatório.

Exemplo, Consolação janeiro/2026 (relatório 414272):

| | Valor |
|---|--:|
| A receber | 23.637,06 |
| Valores com "−" | −33.097,45 |
| **Diferença** | **−9.460,39** |
| Comissões líquido do relatório | 23.637,06 |
| Créditos/Débitos do relatório | −33.097,45 |
| **Soma** | **−9.460,39** |

O Líquido final do SisWeb (−33.342,54) é esse valor somado ao acumulado (−23.882,15).

### 4.4 Lançamentos especiais (justificativas da Optas)

Todos seguem a regra do sinal, sem exceção. As justificativas abaixo só explicam a origem, e nenhuma muda a conta.

| Lançamento | Valor | Relatório | Justificativa |
|---|--:|---|---|
| RETIRADAS … E BOLETO APARTAMENTO | +64.773,05 | 424786 (Consolação, mai/26) | ≈ R$ 50 mil de salário da sócia (nos primeiros meses ela recebeu por cartão e outros pagamentos, sem desconto no relatório) + ≈ R$ 14 mil emprestados para o apartamento. Entra pelo sinal |
| BOLETO … ALUGUEL VERUS | −22.744,32 | 420722 (Consolação, mar/26) | Aluguel. Entra pelo sinal |
| BOLETO … ALUGUEL VERUS … ACERTO | +22.744,32 | 424786 (Consolação, mai/26) | Reembolso do aluguel pago do próprio bolso. Entra pelo sinal; com o de março, soma zero |
| ACERTO FOLHA | +33.342,54 | 417832 (Consolação, fev/26) | Entra pelo sinal |
| LEADS – 44.716 SMS | −2.369,95 | 422418 (Mogi, fev/26) | Mesmo envio do investimento Kolmeya #1444984 (22/01/2026). Ver seção 10 |

---

## 5. Mês sem relatório (estimativa) — hoje só Mogi, novembro/2026

### 5.1 A receber

| Parte | Cálculo |
|---|---|
| **1ª parcela das vendas do mês** | **Projeto Hapvida:** produção do Projeto no mês (painel gerencial) × 100%. **Outras vendas:** propostas do SisWeb cadastradas no mês × 1ª parcela da comissão da Optas (a do SisWeb; sem ela, a grade da operadora/modalidade/vidas). Mogi nov/26: 21.842,59 (Projeto) + 1.829,03 (3 propostas do SisWeb) = **23.671,62** |
| **Parcelas seguintes** | Propostas anteriores do SisWeb: parcela k (k = meses desde a venda) × comissão daquela parcela. Parcela **já recebida** num relatório: 0 (já entrou no mês do relatório). **Cancelada** pela Optas ou **não recebida em 90 dias** depois da data prevista: 0. Mogi nov/26: **27.001,25** |
| Vitalício | Só o que um relatório mostrou como recebido (sem previsão) → 0 em nov/26 |
| Créditos | Só os lançados em relatório → 0 em nov/26 |

A **data prevista** de cada parcela é o vencimento do SisWeb. Sem vencimento, conta 30 dias a partir do último pagamento (ou do cadastro, se ainda não houve pagamento). A situação de cada parcela é:

- **recebida:** achada em um relatório;
- **em dia:** a data prevista ainda não chegou;
- **atrasada:** passou da data prevista há menos de 90 dias;
- **não recebida:** passou da data prevista há 90 dias ou mais. Nesse caso sai da conta.

### 5.2 Saídas

| Parte | Cálculo |
|---|---|
| Salário | Média dos **últimos 3 meses** com salário em relatório. Mogi: jun 25.159,89 · jul 24.384,15 · ago 22.768,71 → **24.104,25** |
| Benefícios | Média dos últimos 3 meses com benefícios em relatório. Mogi: jun 5.035,58 · jul 6.045,28 · ago 5.840,30 → **5.640,39** |
| Custo operacional | 2.300,00 |
| Provisão | 826,97 (seção 7) |
| Imposto | 15% sobre tudo (sem relatório não há linha com desconto da W3G): 50.672,87 × 15% = **7.600,93** |

O salário de cada lançamento vai para o **mês a que se refere**, lido na descrição: "SALÁRIOS – SETEMBRO 2026" conta em setembro, e "SALÁRIO – … 07/09" também. Sem ano na descrição, vale o mês mais recente até o desconto. Sem mês na descrição, vale o mês do desconto. Esta regra serve só para a média da estimativa.

### 5.3 Estrutura informada

Só se uma unidade não tiver **nenhum** relatório; hoje nenhuma das duas está nessa situação. O custo é a soma de:

- salários brutos;
- VR e VT: valor por dia útil de out/2026 × dias úteis do mês;
- custo operacional;
- comissões dos vendedores (seção 8).

**Dias úteis** = segunda a sexta, menos os feriados abaixo. Feriado não paga VR nem VT.

| Tipo | Feriados |
|---|---|
| Nacionais | 1/1, Sexta-feira Santa, 21/4, 1/5, 7/9, 12/10, 2/11, 15/11, 20/11, 25/12 |
| Estadual | 9/7 |
| Móveis | Corpus Christi · Carnaval (segunda e terça) |
| Municipais | 25/1 nas duas unidades · 1/9 em Mogi |

---

## 6. Imposto

O imposto é calculado linha a linha, pelo **% Adm.** de cada linha do relatório:

| Linha | Imposto |
|---|---|
| % Adm. > 0: a W3G já descontou 8,5% como despesa adm. (paga metade do imposto) | **6,5% sobre o Líquido** da linha, que é o valor que sobrou depois do desconto da W3G |
| % Adm. 0,00%, créditos positivos e tudo o que não vem de relatório | **15%** |

Fórmulas do mês:

- **Base 6,5%** = Σ Líquido positivo das linhas com % Adm. > 0, limitada ao a receber.
- **Base 15%** = a receber − base 6,5%.
- **Imposto** = base 6,5% × 6,5% + base 15% × 15%, cada parte arredondada ao centavo.
- Mês coberto pelo relatório seguinte: imposto = 0, porque o a receber é 0.

Exemplo, Consolação novembro/2026: 25.998,81 × 6,5% = 1.689,92 e 38.175,64 × 15% = 5.726,35, total **7.416,27**.

> Decisão de 26/11/2026: quando a W3G paga metade do imposto (linha com % Adm. 8,50%), a Optas paga **6,5%** e não mais 8,5%. Em 2026 isso reduziu o imposto de 118.625,31 para 110.662,41 (−7.962,90).

---

## 7. Provisão de 13º e férias — entra em **todo mês**, com ou sem relatório

| Parte | Fórmula | Consolação | Mogi |
|---|---|--:|--:|
| 13º | base CLT ÷ 12 | 442,98 | 460,11 |
| Férias + 1/3 | base CLT ÷ 3 ÷ 12 | 147,66 | 153,37 |
| Encargos | (13º + férias) × 34,8% | 205,54 | 213,49 |
| **Provisão do mês** | soma | **796,18** | **826,97** |

Total das duas unidades: R$ 1.623,15 por mês.

---

## 8. Comissão dos vendedores

O cálculo é este:

- **Fora do Projeto Hapvida:** a faixa da unidade é escolhida pela produção **total** do vendedor no mês (Projeto + fora). Comissão = percentual da faixa × produção fora do Projeto.
- **Projeto Hapvida:** 15% da mensalidade + valor por vida pela quantidade de vidas do mês. Abaixo de 25 vidas não há valor por vida.
- **Comissão do vendedor** = comissão fora + 15% do Projeto + valor por vida.

**No resultado:** quando há relatório ou média de relatórios, a comissão dos vendedores **não sai à parte** (= 0), porque os pagamentos já estão no relatório. Ela só sai à parte na estrutura informada (seção 5.3). A aba Comissões mostra o valor a pagar a cada vendedor; o resultado não usa esse valor.

---

## 9. Resultado do mês (por unidade; o consolidado é a soma das unidades)

| Linha | Fórmula |
|---|---|
| **A receber** | seção 4.1 (com relatório), 5.1 (estimativa) ou 0 (coberto pelo seguinte) |
| Custo fixo | valores com "−" no relatório + custo operacional · na estimativa: média do salário + média dos benefícios + custos lançados + custo operacional · na estrutura: seção 5.3 |
| Provisão | seção 7 |
| **Custo da operação** | custo fixo + provisão |
| Imposto | seção 6 |
| **Custo da operação total** | custo da operação + imposto |
| Comissões à parte | seção 8 (hoje 0) |
| **Saídas (custos do mês)** | custo da operação total + comissões à parte |
| **Lucro bruto** | a receber − saídas |
| Investido | investimentos em marketing do mês (seção 10) |
| **Lucro líquido** | lucro bruto − (investido − SMS já descontado no relatório) |
| Margem bruta | lucro bruto ÷ a receber |
| Margem líquida | lucro líquido ÷ a receber |
| % de marketing | investido ÷ a receber |

**Ano** = soma dos meses. **Consolidado** = soma das unidades, centavo a centavo.

---

## 10. Investimento em marketing

- O investimento entra no **mês da data** do lançamento.
- Um lançamento com unidade fica nessa unidade.
- Um lançamento sem unidade é rateado pela produção de cada unidade no mês, pelos maiores restos.
- **SMS já descontado no relatório.** Se um relatório da mesma unidade traz a linha de SMS com o **mesmo número de envios** do lançamento, ela já saiu como custo no relatório. Esse lançamento não desconta de novo do lucro líquido, mas continua no total investido e no ROI.
  - Único caso: Mogi, Kolmeya #1444984, 44.716 envios, R$ 2.369,95 (lançado em jan/26, descontado no relatório de fev/26).
  - Por isso, no ano de Mogi, lucro bruto − investido ≠ lucro líquido em exatamente R$ 2.369,95.

---

## 11. Reserva de marketing e mínimo para não fechar no vermelho

A reserva e o mínimo são informativos e não entram nas saídas.

| Indicador | Cálculo |
|---|---|
| Produção do mês | Soma das mensalidades vendidas no mês: Projeto Hapvida + propostas do SisWeb (propostas canceladas não entram). Nos meses anteriores ao atual, conta só o SisWeb |
| Reserva de marketing | 15% × produção |
| Saldo da reserva | Σ (reserva − investido) dos meses anteriores do ano + reserva do mês. Pode ficar negativo |
| **Mínimo para empatar** | Menor a receber x, em centavos, tal que x − imposto(x) ≥ comissões à parte + custo fixo + provisão |
| **Mínimo sustentável** | Idem, somando também a reserva de marketing do mês |

---

## 12. ROI do marketing

ROI = (1ª parcela gerada pelas vendas fora do Projeto Hapvida − investido) ÷ investido.

O imposto (15% da 1ª parcela) e a comissão do vendedor aparecem ao lado só como informação.

**Hoje o ROI não é mostrado.** Sem a lista de quais vendas vieram do SMS, ele não seria real. Volta a aparecer quando a lista de vendas do SMS for enviada. A partir de dez/2026, o ROI passa a ser calculado venda a venda, por campanha.

---

## 13. Vitalício

O vitalício começa **depois da última parcela de agenciamento** da grade, e o percentual de cada operadora/modalidade está na grade V3 de 02/10/2026.

No a receber entra **só o vitalício que aparece como recebido** num relatório, sem previsão. A aba Vitalício mostra o previsto da carteira apenas como informação.

---

## 14. Grade de comissão das operadoras (propostas do SisWeb)

A comissão de cada proposta é escolhida nesta ordem:

1. **Comissão da Optas cadastrada no SisWeb:** é a que vale.
2. **Proposta sem comissão no SisWeb:** usa a **Grade de Comissão V3 (02/10/2026)**. A grade é escolhida por operadora, modalidade (PF/PME/Adesão), produto, faixa de vidas e idade do titular (Prevent Senior). Cada parcela = mensalidade × % da parcela.
3. **Fora da faixa de vidas:** usa a faixa mais próxima. Ex.: Select PME com 1 vida usa a faixa de 2 a 29.
4. **Operadora fora da grade** (Onmed, Unimed Santos): sem comissão (R$ 0,00), com aviso.

Na **Adesão**, a 1ª parcela é a taxa de angariação e não vem para a Optas (= 0).

---

## 15. Como o próprio sistema se confere

O teste `testes/auditoria-centavos.js` abre o sistema e confere ao centavo, em todos os meses:

- a receber = Σ positivos do relatório;
- saídas do relatório = Σ negativos do relatório;
- a receber − saídas = comissões líquido + créditos/débitos;
- base 6,5% e base 15% = linhas do relatório;
- imposto = 6,5% + 15%;
- provisão = fórmula da seção 7;
- lucro bruto = a receber − saídas;
- lucro líquido = lucro bruto − investido (com o ajuste do SMS);
- unidades somadas = consolidado;
- meses somados = ano;
- entradas e saídas por categoria = totais.

Resultado atual: **nenhuma falha**.

Também foi feita uma conta independente, direto dos arquivos dos relatórios e sem usar o código do painel, para todos os meses com relatório. **Bate ao centavo** com o painel.

---

## 16. Números de cada mês (memória de cálculo)

Os valores abaixo são os do painel. As tabelas de cada unidade somam o total da linha final, e o consolidado é a soma das duas unidades.

#### Consolação — entradas (a receber)

| Mês | Situação | Relatório(s) | 1ª parcela | Parcelas seguintes | Vitalício | Créditos (campanhas, acertos…) | **A receber** |
|---|---|---|--:|--:|--:|--:|--:|
| jan/26 | relatório | 414272 | 7.460,19 | 15.901,93 | 274,94 | 0,00 | **23.637,06** |
| fev/26 | relatório | 417832 | 2.895,81 | 13.760,68 | 428,14 | 37.592,54 | **54.677,17** |
| mar/26 | relatório | 420722+420789 | 26.169,32 | 13.983,71 | 11.172,54 | 2.133,88 | **53.459,45** |
| abr/26 | relatório | 424785 | 1.640,06 | 1.638,77 | 2.150,77 | 0,00 | **5.429,60** |
| mai/26 | relatório | 424786 | 6.119,06 | 14.650,56 | 6.242,50 | 87.734,44 | **114.746,56** |
| jun/26 | relatório | 424787 | 14.398,51 | 9.691,29 | 6.096,60 | 1.485,76 | **31.672,16** |
| jul/26 | relatório | 424792 | 13.136,71 | 18.891,45 | 5.271,55 | 0,00 | **37.299,71** |
| ago/26 | relatório | 424793 | 2.543,95 | 12.447,87 | 5.477,94 | 1.216,15 | **21.685,91** |
| set/26 | relatório | 425632 | 5.522,87 | 16.956,95 | 5.285,83 | 12.108,01 | **39.873,66** |
| out/26 | coberto pelo seguinte | — | 0,00 | 0,00 | 0,00 | 0,00 | **0,00** |
| nov/26 | relatório | 427670 | 25.711,68 | 23.231,87 | 11.480,86 | 3.750,04 | **64.174,45** |
| **Total** | | | **105.598,16** | **141.155,08** | **53.881,67** | **146.020,82** | **446.655,73** |

#### Consolação — imposto

| Mês | Base 6,5% (linhas com % Adm. > 0, W3G paga metade) | Imposto 6,5% | Base 15% (resto) | Imposto 15% | **Imposto** |
|---|--:|--:|--:|--:|--:|
| jan/26 | 11.142,88 | 724,29 | 12.494,18 | 1.874,13 | **2.598,42** |
| fev/26 | 14.146,87 | 919,55 | 40.530,30 | 6.079,55 | **6.999,10** |
| mar/26 | 13.525,13 | 879,13 | 39.934,32 | 5.990,15 | **6.869,28** |
| abr/26 | 2.316,18 | 150,55 | 3.113,42 | 467,01 | **617,56** |
| mai/26 | 15.777,64 | 1.025,55 | 98.968,92 | 14.845,34 | **15.870,89** |
| jun/26 | 10.861,78 | 706,02 | 20.810,38 | 3.121,56 | **3.827,58** |
| jul/26 | 20.141,96 | 1.309,23 | 17.157,75 | 2.573,66 | **3.882,89** |
| ago/26 | 13.922,90 | 904,99 | 7.763,01 | 1.164,45 | **2.069,44** |
| set/26 | 18.475,34 | 1.200,90 | 21.398,32 | 3.209,75 | **4.410,65** |
| out/26 | 0,00 | 0,00 | 0,00 | 0,00 | **0,00** |
| nov/26 | 25.998,81 | 1.689,92 | 38.175,64 | 5.726,35 | **7.416,27** |
| **Total** | **146.309,49** | **9.510,13** | **300.346,24** | **45.051,95** | **54.562,08** |

#### Consolação — saídas e resultado

| Mês | Gastos dos relatórios (no mês escrito na descrição) | Estimativa (média 3 meses, ainda sem relatório) | Custo operacional | Provisão 13º/férias | Imposto | **Saídas** | **Lucro bruto** | Investido | SMS já no relatório | **Lucro líquido** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| jan/26 | 30.509,85 | — | 0,00 | 796,18 | 2.598,42 | **33.904,45** | **−10.267,39** | 0,00 | — | **−10.267,39** |
| fev/26 | 28.209,50 | — | 0,00 | 796,18 | 6.999,10 | **36.004,78** | **18.672,39** | 0,00 | — | **18.672,39** |
| mar/26 | 88.656,20 | — | 0,00 | 796,18 | 6.869,28 | **96.321,66** | **−42.862,21** | 0,00 | — | **−42.862,21** |
| abr/26 | 26.733,55 | — | 0,00 | 796,18 | 617,56 | **28.147,29** | **−22.717,69** | 0,00 | — | **−22.717,69** |
| mai/26 | 33.095,30 | — | 0,00 | 796,18 | 15.870,89 | **49.762,37** | **64.984,19** | 0,00 | — | **64.984,19** |
| jun/26 | 30.645,67 | — | 0,00 | 796,18 | 3.827,58 | **35.269,43** | **−3.597,27** | 0,00 | — | **−3.597,27** |
| jul/26 | 42.418,96 | — | 0,00 | 796,18 | 3.882,89 | **47.098,03** | **−9.798,32** | 0,00 | — | **−9.798,32** |
| ago/26 | 35.108,20 | — | 0,00 | 796,18 | 2.069,44 | **37.973,82** | **−16.287,91** | 0,00 | — | **−16.287,91** |
| set/26 | 30.156,84 | — | 0,00 | 796,18 | 4.410,65 | **35.363,67** | **4.509,99** | 0,00 | — | **4.509,99** |
| out/26 | 26.022,13 | — | 0,00 | 796,18 | 0,00 | **26.818,31** | **−26.818,31** | 0,00 | — | **−26.818,31** |
| nov/26 | 8.538,91 | 21.882,47 | 0,00 | 796,18 | 7.416,27 | **38.633,83** | **25.540,62** | 0,00 | — | **25.540,62** |
| **Total** | **380.095,11** | **21.882,47** | **0,00** | **8.757,98** | **54.562,08** | **465.297,64** | **−18.641,91** | **0,00** | **0,00** | **−18.641,91** |

#### Mogi — entradas (a receber)

| Mês | Situação | Relatório(s) | 1ª parcela | Parcelas seguintes | Vitalício | Créditos (campanhas, acertos…) | **A receber** |
|---|---|---|--:|--:|--:|--:|--:|
| jan/26 | relatório | 422416 | 12.775,98 | 26.882,69 | 1.087,34 | 9.900,00 | **50.646,01** |
| fev/26 | relatório | 422418 | 20.509,05 | 38.285,22 | 2.370,77 | 2.850,00 | **64.015,04** |
| mar/26 | relatório | 422421 | 6.003,01 | 19.823,51 | 1.675,75 | 1.579,45 | **29.081,72** |
| abr/26 | relatório | 422422 | 5.187,59 | 9.224,63 | 1.978,67 | 1.411,24 | **17.802,13** |
| mai/26 | relatório | 423291 | 17.123,34 | 10.840,56 | 2.106,91 | 1.130,00 | **31.200,81** |
| jun/26 | relatório | 423292 | 11.048,79 | 16.698,13 | 1.878,27 | 0,00 | **29.625,19** |
| jul/26 | relatório | 424781 | 21.530,90 | 22.500,04 | 2.101,63 | 5.050,00 | **51.182,57** |
| ago/26 | relatório | 424782 | 26.600,09 | 23.995,54 | 2.340,86 | 3.001,71 | **55.938,20** |
| set/26 | relatório | 425400 | 24.489,23 | 29.829,43 | 1.759,00 | 3.260,98 | **59.338,64** |
| out/26 | relatório | 426505 | 31.035,67 | 33.392,75 | 3.095,77 | 9.682,01 | **77.206,20** |
| nov/26 | estimativa | — | 23.671,62 | 27.001,25 | 0,00 | 0,00 | **50.672,87** |
| **Total** | | | **199.975,27** | **258.473,75** | **20.394,97** | **37.865,39** | **516.709,38** |

#### Mogi — imposto

| Mês | Base 6,5% (linhas com % Adm. > 0, W3G paga metade) | Imposto 6,5% | Base 15% (resto) | Imposto 15% | **Imposto** |
|---|--:|--:|--:|--:|--:|
| jan/26 | 27.970,03 | 1.818,05 | 22.675,98 | 3.401,40 | **5.219,45** |
| fev/26 | 40.655,99 | 2.642,64 | 23.359,05 | 3.503,86 | **6.146,50** |
| mar/26 | 21.499,26 | 1.397,45 | 7.582,46 | 1.137,37 | **2.534,82** |
| abr/26 | 11.203,30 | 728,21 | 6.598,83 | 989,82 | **1.718,03** |
| mai/26 | 12.947,47 | 841,59 | 18.253,34 | 2.738,00 | **3.579,59** |
| jun/26 | 18.576,40 | 1.207,47 | 11.048,79 | 1.657,32 | **2.864,79** |
| jul/26 | 24.601,67 | 1.599,11 | 26.580,90 | 3.987,14 | **5.586,25** |
| ago/26 | 26.305,12 | 1.709,83 | 29.633,08 | 4.444,96 | **6.154,79** |
| set/26 | 31.588,43 | 2.053,25 | 27.750,21 | 4.162,53 | **6.215,78** |
| out/26 | 36.488,52 | 2.371,75 | 40.717,68 | 6.107,65 | **8.479,40** |
| nov/26 | 0,00 | 0,00 | 50.672,87 | 7.600,93 | **7.600,93** |
| **Total** | **251.836,19** | **16.369,35** | **264.873,19** | **39.730,98** | **56.100,33** |

#### Mogi — saídas e resultado

| Mês | Gastos dos relatórios (no mês escrito na descrição) | Estimativa (média 3 meses, ainda sem relatório) | Custo operacional | Provisão 13º/férias | Imposto | **Saídas** | **Lucro bruto** | Investido | SMS já no relatório | **Lucro líquido** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| jan/26 | 36.353,78 | — | 2.300,00 | 826,97 | 5.219,45 | **44.700,20** | **5.945,81** | 4.907,06 | 2.369,95 | **3.408,70** |
| fev/26 | 20.136,11 | — | 2.300,00 | 826,97 | 6.146,50 | **29.409,58** | **34.605,46** | 10.202,34 | — | **24.403,12** |
| mar/26 | 30.748,76 | — | 2.300,00 | 826,97 | 2.534,82 | **36.410,55** | **−7.328,83** | 12.139,44 | — | **−19.468,27** |
| abr/26 | 48.803,40 | — | 2.300,00 | 826,97 | 1.718,03 | **53.648,40** | **−35.846,27** | 8.018,16 | — | **−43.864,43** |
| mai/26 | 45.317,90 | — | 2.300,00 | 826,97 | 3.579,59 | **52.024,46** | **−20.823,65** | 5.613,44 | — | **−26.437,09** |
| jun/26 | 44.693,66 | — | 2.300,00 | 826,97 | 2.864,79 | **50.685,42** | **−21.060,23** | 7.186,38 | — | **−28.246,61** |
| jul/26 | 41.144,27 | — | 2.300,00 | 826,97 | 5.586,25 | **49.857,49** | **1.325,08** | 18.612,86 | — | **−17.287,78** |
| ago/26 | 29.077,21 | — | 2.300,00 | 826,97 | 6.154,79 | **38.358,97** | **17.579,23** | 17.119,37 | — | **459,86** |
| set/26 | 10.572,47 | 29.744,64 | 2.300,00 | 826,97 | 6.215,78 | **49.659,86** | **9.678,78** | 1.774,81 | — | **7.903,97** |
| out/26 | 2.947,40 | 29.744,64 | 2.300,00 | 826,97 | 8.479,40 | **44.298,41** | **32.907,79** | 2.352,62 | — | **30.555,17** |
| nov/26 | — | 29.744,64 | 2.300,00 | 826,97 | 7.600,93 | **40.472,54** | **10.200,33** | 0,00 | — | **10.200,33** |
| **Total** | **309.794,96** | **89.233,92** | **25.300,00** | **9.096,67** | **56.100,33** | **489.525,88** | **27.183,50** | **87.926,48** | **2.369,95** | **−58.373,03** |

#### Consolidado (Consolação + Mogi)

| Mês | A receber | Imposto | Saídas | Lucro bruto | Investido | Lucro líquido | Produção (mensalidades vendidas) | Reserva de marketing (15%) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| jan/26 | 74.283,07 | 7.817,87 | 78.604,65 | −4.321,58 | 4.907,06 | −6.858,69 | 33.329,87 | 4.999,48 |
| fev/26 | 118.692,21 | 13.145,60 | 65.414,36 | 53.277,85 | 10.202,34 | 43.075,51 | 56.868,80 | 8.530,32 |
| mar/26 | 82.541,17 | 9.404,10 | 132.732,21 | −50.191,04 | 12.139,44 | −62.330,48 | 49.451,80 | 7.417,77 |
| abr/26 | 23.231,73 | 2.335,59 | 81.795,69 | −58.563,96 | 8.018,16 | −66.582,12 | 71.196,09 | 10.679,41 |
| mai/26 | 145.947,37 | 19.450,48 | 101.786,83 | 44.160,54 | 5.613,44 | 38.547,10 | 71.186,04 | 10.677,90 |
| jun/26 | 61.297,35 | 6.692,37 | 85.954,85 | −24.657,50 | 7.186,38 | −31.843,88 | 47.382,46 | 7.107,37 |
| jul/26 | 88.482,28 | 9.469,14 | 96.955,52 | −8.473,24 | 18.612,86 | −27.086,10 | 58.386,56 | 8.757,98 |
| ago/26 | 77.624,11 | 8.224,23 | 76.332,79 | 1.291,32 | 17.119,37 | −15.828,05 | 50.849,62 | 7.627,45 |
| set/26 | 99.212,30 | 10.626,43 | 85.023,53 | 14.188,77 | 1.774,81 | 12.413,96 | 40.534,98 | 6.080,25 |
| out/26 | 77.206,20 | 8.479,40 | 71.116,72 | 6.089,48 | 2.352,62 | 3.736,86 | 29.134,62 | 4.370,19 |
| nov/26 | 114.847,32 | 15.017,20 | 79.106,37 | 35.740,95 | 0,00 | 35.740,95 | 50.101,05 | 7.515,16 |
| **Total** | **963.365,11** | **110.662,41** | **954.823,52** | **8.541,59** | **87.926,48** | **−77.014,94** | **558.421,89** | **83.763,28** |

#### Relatórios de pagamento usados

| Relatório | Unidade | Gerado em | Previsão | Mês de referência | Comissões (líquido) | Créditos e débitos | **Valor do mês** (= comissões + créditos/débitos) | Acumulado de meses anteriores (não entra) | Líquido final do SisWeb | Entra em 2026? |
|---|---|---|---|---|--:|--:|--:|--:|--:|---|
| 414272 | Consolação | 07/01/2026 | 09/01/2026 | jan/26 | 23.637,06 | −33.097,45 | **−9.460,39** | −23.882,15 | −33.342,54 | sim |
| 417832 | Consolação | 10/02/2026 | 20/02/2026 | fev/26 | 17.084,63 | −116,96 | **16.967,67** | −33.342,54 | −16.374,87 | sim |
| 420722 | Consolação | 12/03/2026 | 05/03/2026 | mar/26 | 23.809,84 | −54.857,36 | **−31.047,52** | −16.374,87 | −47.422,39 | sim |
| 420789 | Consolação | 20/03/2026 | 20/03/2026 | mar/26 | 27.515,73 | −30.412,82 | **−2.897,09** | −47.422,39 | −50.319,48 | sim |
| 424785 | Consolação | 10/08/2026 | 06/04/2026 | abr/26 | 5.429,60 | −16.230,34 | **−10.800,74** | −50.319,48 | −61.120,22 | sim |
| 424786 | Consolação | 10/08/2026 | 05/05/2026 | mai/26 | 27.012,12 | 61.064,49 | **88.076,61** | −61.120,22 | 26.956,39 | sim |
| 424787 | Consolação | 10/08/2026 | 05/06/2026 | jun/26 | 30.186,40 | −33.402,55 | **−3.216,15** | 26.956,39 | 23.740,24 | sim |
| 424792 | Consolação | 10/08/2026 | 07/07/2026 | jul/26 | 37.299,71 | −42.199,05 | **−4.899,34** | 23.740,24 | 18.840,90 | sim |
| 424793 | Consolação | 10/08/2026 | 05/08/2026 | ago/26 | 20.469,76 | −30.411,02 | **−9.941,26** | 18.840,90 | 8.899,64 | sim |
| 425632 | Consolação | 31/08/2026 | 04/09/2026 | set/26 | 27.765,65 | −18.282,67 | **9.482,98** | 8.899,64 | 18.382,62 | sim |
| 427670 | Consolação | 28/10/2026 | 05/11/2026 | nov/26 | 60.424,41 | −55.716,16 | **4.708,25** | 18.382,62 | 23.090,87 | sim |
| 422414 | Mogi | 04/05/2026 | 05/11/2025 | nov/25 | 30.949,49 | −32.159,61 | **−1.210,12** | 9.495,82 | 8.285,70 | não (2025) |
| 422415 | Mogi | 04/05/2026 | 05/12/2025 | 12/25 | 48.664,56 | −32.682,99 | **15.981,57** | 8.285,70 | 24.267,27 | não (2025) |
| 422416 | Mogi | 04/05/2026 | 09/01/2026 | jan/26 | 40.746,01 | −43.313,85 | **−2.567,84** | 24.267,27 | 21.699,43 | sim |
| 422418 | Mogi | 04/05/2026 | 05/02/2026 | fev/26 | 61.165,04 | −21.098,52 | **40.066,52** | 21.699,43 | 61.765,95 | sim |
| 422421 | Mogi | 04/05/2026 | 05/03/2026 | mar/26 | 27.502,27 | −22.000,43 | **5.501,84** | 61.765,95 | 67.267,79 | sim |
| 422422 | Mogi | 04/05/2026 | 06/04/2026 | abr/26 | 16.390,89 | −14.610,94 | **1.779,95** | 67.267,79 | 69.047,74 | sim |
| 423291 | Mogi | 03/06/2026 | 06/05/2026 | mai/26 | 30.070,81 | −25.125,87 | **4.944,94** | 69.047,74 | 73.992,68 | sim |
| 423292 | Mogi | 03/06/2026 | 05/06/2026 | jun/26 | 29.625,19 | −51.695,52 | **−22.070,33** | 73.992,68 | 51.922,35 | sim |
| 424781 | Mogi | 10/08/2026 | 06/07/2026 | jul/26 | 46.132,57 | −39.181,74 | **6.950,83** | 51.922,35 | 58.873,18 | sim |
| 424782 | Mogi | 10/08/2026 | 05/08/2026 | ago/26 | 52.936,49 | −66.013,61 | **−13.077,12** | 58.873,18 | 45.796,06 | sim |
| 425400 | Mogi | 26/08/2026 | 04/09/2026 | set/26 | 56.077,66 | −46.635,34 | **9.442,32** | 45.796,06 | 55.238,38 | sim |
| 426505 | Mogi | 01/10/2026 | 05/10/2026 | out/26 | 67.524,19 | 6.734,61 | **74.258,80** | 55.238,38 | 129.497,18 | sim |

## 17. Pontos de atenção para a auditoria

1. **Acumulado do SisWeb.** O "Líquido final" de cada relatório inclui o acumulado dos meses anteriores. O painel usa o valor do mês (comissões + créditos/débitos), porque o acumulado já entrou no mês de origem. Somar o Líquido final contaria esses meses duas vezes.
2. **Relatório gerado depois do mês.** Vários relatórios foram gerados meses depois, por exemplo os da Consolação de abr–ago, gerados em 10/08/2026. Vale a **previsão**, não a geração.
3. **Consolação, outubro/2026.** Não há relatório com previsão em outubro. O de novembro (427670) traz o que seria de outubro, como salários de setembro e de outubro. Outubro fica com a receber 0 e saídas = provisão.
4. **Mogi, novembro/2026.** Ainda não há relatório. É estimativa (seção 5) e muda quando o relatório chegar.
5. **SMS de fevereiro em Mogi.** Sai pelo relatório e não sai de novo no lucro líquido (seção 10).
6. **Provisão em mês com relatório.** A provisão de 13º e férias entra todo mês, mesmo quando o relatório já traz férias ou 13º pagos. É uma decisão da Optas. Ex.: Mogi, jan/26, férias e 13º no relatório: R$ 7.394,41.
7. **Comissão do Valdecir (40%, Mogi).** Vem como débito no relatório e entra como saída. O sistema avisa se aparecer depois de julho/2026, quando foi encerrada.
8. **Projeto Hapvida no mês atual.** A produção vem do painel gerencial (instantâneo de 23/11/2026) e não do SisWeb.
9. **7 linhas com Líquido R$ 0,00.** São 1ª parcela de adesão retida e não contam como recebidas.

---

## 18. Como reproduzir

1. Gerar o sistema: `python3 build.py`. Ele junta o código (`src/painel.html`) com os dados do SisWeb (`data/erp/`) e gera `index.html`.
2. Conferir: `node testes/auditoria-centavos.js` deve mostrar `"falhas": []`.
3. Abrir `index.html` no navegador:
   - aba **Ano**: os meses e o detalhe dos custos;
   - **Entradas e saídas**: as categorias;
   - **A receber**: parcela a parcela.
