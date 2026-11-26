# OPTAS — DOCUMENTO-MESTRE DE GESTÃO, FINANCEIRO, COMERCIAL E ROI

**Versão:** 4.2  
**Data de referência:** 23/11/2026  
**Finalidade:** Consolidar as regras de negócio, informações financeiras, cálculos, indicadores, integrações e pendências para desenvolvimento do painel gerencial da Optas.

> Implementação: as regras confirmadas estão no objeto `REGRAS` de `src/painel.html`. Qualquer alteração deste documento deve ser refletida ali e a versão (`REGRAS.versao`) atualizada.

---

# 1. OBJETIVO DO PROJETO

Desenvolver um painel gerencial inteligente para a Optas, capaz de acompanhar a operação comercial e financeira, calcular comissões, identificar custos, apurar resultados e orientar decisões de investimento.

O sistema deverá responder principalmente:

1. Quanto a Optas está produzindo?
2. Quanto a empresa tem a receber das operadoras?
3. Quanto está pagando aos vendedores?
4. Quanto custa manter a operação?
5. Quanto sobra efetivamente para a empresa?
6. Quanto pode investir em geração de negócios?
7. Quanto está investindo diariamente?
8. Qual é o retorno desses investimentos?
9. O investimento está adequado, baixo ou elevado?
10. Quanto a empresa pode aumentar ou reduzir seu investimento?

**Princípio fundamental:** o painel não deve apenas apresentar números. Deve interpretar os dados disponíveis, identificar inconsistências, apontar informações ausentes e recomendar decisões com justificativas financeiras.

Não inventar dados, regras ou percentuais. Quando faltar informação, o sistema deverá sinalizar a pendência.

# 2. ESTRUTURA DA OPERAÇÃO

- Empresa: Optas.
- Gestão: W3G Consultoria.
- Unidades: Consolação e Mogi.
- Funcionários CLT: 9.
- Consolação: 5 funcionários.
- Mogi: 4 funcionários.
- Existem duas sócias, cada uma responsável por uma unidade.

O painel deverá apresentar:
- Resultado consolidado da Optas.
- Resultado individual de Consolação.
- Resultado individual de Mogi.
- Comparação entre as unidades.
- Produção comercial por vendedor.
- Custos e comissões por unidade.

A distribuição posterior dos resultados entre W3G e as sócias não faz parte do escopo deste painel.

# 3. CUSTOS FIXOS E ESTRUTURA FINANCEIRA

## 3.1. Custo mensal consolidado

**Custo mensal informado: R$ 39.185,43.**

Esse valor já inclui:
- Salários CLT.
- Pagamentos PJ das duas sócias.
- Vale-refeição.
- Vale-transporte.
- Custos operacionais informados.
- Encargos de FGTS e INSS, conforme composição geral anteriormente informada.

Atenção: os pagamentos PJ não devem ser somados novamente.

## 3.2. Composição dos salários por unidade

Os valores originalmente informados como salários brutos já incluem CLT e PJ.

| Descrição | Consolação | Mogi | Total |
|---|---:|---:|---:|
| Salários brutos informados (CLT + PJ) | R$ 15.315,76 | R$ 10.521,33 | R$ 25.837,09 |
| Pagamento PJ da sócia | R$ 10.000,00 | R$ 5.000,00 | R$ 15.000,00 |
| Salários CLT (diferença) | R$ 5.315,76 | R$ 5.521,33 | R$ 10.837,09 |

Pagamentos PJ:
- Sócia de Consolação: R$ 10.000,00 por mês.
- Sócia de Mogi: R$ 5.000,00 por mês.
- Total PJ: R$ 15.000,00.
- Não há encargos ou tributos adicionais sobre esses pagamentos, conforme informado.

**Regra obrigatória:** os R$ 15.000,00 de PJ já estão dentro dos R$ 25.837,09 da rubrica de salários brutos. Não adicionar novamente ao custo consolidado.

## 3.3. Benefícios e custos operacionais

| Descrição | Consolação | Mogi | Total |
|---|---:|---:|---:|
| Vale-refeição | R$ 4.140,40 | R$ 3.640,40 | R$ 7.780,80 |
| Vale-transporte | R$ 1.576,24 | R$ 1.691,30 | R$ 3.267,54 |
| Custos operacionais | R$ 0,00 | R$ 2.300,00 | R$ 2.300,00 |

Os R$ 2.300,00 de Mogi correspondem a aluguel, energia, internet e água.

Consolação não possui despesas operacionais adicionais informadas.

Não existem outras despesas administrativas, conforme confirmação do usuário.

## 3.4. Fechamento mensal

| Categoria | Valor |
|---|---:|
| Salários brutos CLT + PJ | R$ 25.837,09 |
| Vale-refeição | R$ 7.780,80 |
| Vale-transporte | R$ 3.267,54 |
| Custos operacionais | R$ 2.300,00 |
| **CUSTO MENSAL TOTAL** | **R$ 39.185,43** |

O sistema deverá utilizar esse total como referência mensal, sem duplicar pagamentos PJ ou encargos já contemplados.

# 4. PROVISÕES TRABALHISTAS

O custo mensal de R$ 39.185,43 não contempla as provisões anuais de 13º salário e férias.

A base de cálculo é exclusivamente o salário CLT de R$ 10.837,09. Os pagamentos PJ não entram nessa base.

## 4.1. Provisões básicas

| Descrição | Valor anual | Provisão mensal |
|---|---:|---:|
| 13º salário | R$ 10.837,09 | R$ 903,09 |
| 1/3 de férias | R$ 3.612,36 | R$ 301,03 |
| **Total** | **R$ 14.449,45** | **R$ 1.204,12** |

## 4.2. Encargos utilizados na estimativa

Enquadramento informado:
- Regime tributário: Lucro Presumido.
- CNAE: 6622-3/00 — Corretores e agentes de seguros, de planos de previdência complementar e de saúde.
- Referência adotada: FAP desconsiderado, utilizando RAT de 1%.

| Encargo | Alíquota |
|---|---:|
| INSS patronal | 20% |
| RAT | 1% |
| Terceiros | 5,8% |
| FGTS | 8% |
| **Total estimado** | **34,8%** |

## 4.3. Provisão mensal com encargos

| Descrição | Valor mensal |
|---|---:|
| 13º salário | R$ 903,09 |
| 1/3 de férias | R$ 301,03 |
| Encargos estimados de 34,8% | R$ 419,03 |
| **Total mensal estimado** | **R$ 1.623,15** |

**Valor gerencial de referência:** R$ 1.623,15 por mês.

O sistema deverá provisionar esse valor separadamente do custo mensal de R$ 39.185,43.

**Atenção técnica:** a composição dos encargos e o enquadramento de terceiros precisam ser validados pela contabilidade antes de serem tratados como definitivos. Não duplicar FGTS ou INSS que já estejam incluídos no cálculo geral. O INSS descontado do funcionário na segunda parcela do 13º é retenção do trabalhador, não uma nova despesa patronal.

# 5. COMISSÕES PAGAS AOS VENDEDORES

O cálculo será realizado individualmente, de acordo com a produção mensal de cada vendedor.

A produção considerada é o valor mensal dos planos vendidos, e não a comissão que a operadora paga à Optas.

O custo salarial fixo deverá ser acompanhado por unidade/equipe, sem exigir média de comissões individuais para provisionamento da folha.

## 5.1. Consolação

Meta individual mensal: R$ 5.000,00.

| Produção mensal | Percentual |
|---|---:|
| Abaixo de R$ 5.000,00 | 30% |
| A partir de R$ 5.000,00 | 50% |

Regra confirmada: quando o vendedor alcança R$ 5.000,00, recebe 50% sobre toda a produção do mês. Exemplo: produção de R$ 6.000,00 → 50% → comissão de R$ 3.000,00.

## 5.2. Mogi

| Produção mensal | Percentual |
|---|---:|
| De R$ 1,00 a R$ 2.999,99 | 20% |
| De R$ 3.000,00 a R$ 5.999,99 | 25% |
| De R$ 6.000,00 a R$ 8.999,99 | 30% |
| De R$ 9.000,00 a R$ 11.999,99 | 40% |
| A partir de R$ 12.000,00 | 50% |

Regra confirmada: o percentual alcançado incide sobre toda a produção mensal. Exemplos: R$ 10.000,00 → 40% → R$ 4.000,00; R$ 12.000,00 → 50% → R$ 6.000,00.

## 5.3. Regras de cálculo

1. Identificar o vendedor.
2. Identificar a unidade.
3. Somar a produção mensal daquele vendedor.
4. Aplicar a faixa correspondente.
5. Aplicar o percentual sobre toda a produção mensal.
6. Apresentar a comissão calculada.

Não utilizar média histórica de comissões para estimar esse pagamento.

# 6. COMISSÕES RECEBIDAS DAS OPERADORAS

A Optas recebe comissões de agenciamento e vitalício conforme as regras de cada operadora.

| Operadora | Agenciamento | Vitalício |
|---|---:|---:|
| Bradesco | 400% | 4% |
| Amil | 300% | 2% |
| SulAmérica | 300% | 2% |
| Seguros Unimed | 300% | 2% |
| Porto | 300% | 2% |
| Hapvida | 350% | 2% |
| Alice | 300% | 2% |

Exemplos (mensalidade de R$ 5.000,00): Bradesco 400% → R$ 20.000,00; Amil 300% → R$ 15.000,00; Hapvida 350% → R$ 17.500,00.

O cálculo de agenciamento utiliza o percentual da operadora sobre a mensalidade do plano.

## 6.0. Projeto Hapvida (v1.1)

- Vendas do **Projeto Hapvida** têm comissão própria, bem inferior à da Hapvida comum. Percentuais ainda não informados (Pendência 8).
- Vendas **Hapvida fora do projeto** usam a tabela da operadora: 350% de agenciamento + 2% de vitalício.
- Demais operadoras usam a tabela armazenada (seção 6).
- Ordem de aplicação para cada venda: tabela gravada na época da venda → regra do projeto → tabela da operadora.

## 6.1. Operadoras com percentuais pendentes

MedSênior, Prevent, Santa Helena, Sobam, Supermed, Qualicorp, Ana Costa, São Cristóvão, Trasmontano.

## 6.2. Distinção entre PF e PME

As comissões variam conforme a modalidade. O usuário informará, para cada operadora, se possui somente PF, somente PME ou ambas, e os percentuais de cada modalidade quando forem diferentes.

**Regra:** sempre que receber uma nova operadora ou percentual, verificar se a modalidade PF/PME foi informada. Se não foi, solicitar essa informação. Não presumir que a mesma comissão vale para as duas modalidades.

As sete operadoras já informadas também precisam ter sua aplicabilidade PF/PME identificada antes da configuração definitiva.

# 7. VITALÍCIO

- Início a partir da quarta parcela.
- Pagamento enquanto o contrato permanecer ativo.
- Percentual conforme a operadora.

Exemplos (mensalidade de R$ 5.000,00): Bradesco 4% → R$ 200,00/parcela; Amil 2% → R$ 100,00; Hapvida 2% → R$ 100,00.

Ainda é necessário confirmar: se a quarta parcela é a regra de todas as operadoras e modalidades; qual valor será a base do vitalício; se as condições de continuidade são iguais para todas as modalidades.

# 8. IMPOSTOS

- Alíquota: 15%. **Substituído em 26/11/2026:** ver "Imposto — regra definitiva" (15% só nas linhas com % Adm. 0,00%; nas de 8,50%, 8,5% sobre o que sobrou).
- Incide sobre comissões de todas as operadoras, sobre agenciamento e sobre vitalício.
- Não é descontada da comissão paga ao funcionário.
- Não criar alíquotas diferentes por operadora.

# 9. RESERVA DE MARKETING

> **Substituído na v1.6:** a reserva passou a ser 15% da produção mensal (ver 12.7). O texto abaixo fica como histórico.

Reservar 15% do lucro bruto operacional para reinvestimento em marketing e geração de leads.

## 9.1. Fórmula

Lucro bruto operacional = comissões efetivamente recebidas pela Optas − comissões pagas aos funcionários CLT.

Reserva de marketing = lucro bruto operacional × 15%.

| Descrição | Valor |
|---|---:|
| Comissões efetivamente recebidas | R$ 100.000,00 |
| Comissões pagas aos CLT | R$ 30.000,00 |
| Lucro bruto operacional | R$ 70.000,00 |
| Reserva de marketing (15%) | R$ 10.500,00 |

## 9.2. Regras

- O cálculo usa comissões efetivamente recebidas; não utilizar comissões apenas previstas.
- A reserva é uma destinação do resultado, não uma despesa operacional.
- Não contabilizar a reserva duas vezes.
- O dinheiro é destinado à geração de leads e oportunidades.
- Não subtrair impostos, custos fixos ou outras categorias dessa base sem decisão adicional do usuário.

# 10. INTEGRAÇÃO COM O PAINEL GERENCIAL

O sistema não receberá propostas diretamente. A fonte será o painel gerencial integrado, que deverá fornecer, quando aplicável: identificação da venda, operadora, modalidade PF/PME, valor mensal do plano, vendedor, unidade, data da venda, origem ou campanha, identificação do contrato e informações para agenciamento e vitalício.

## 10.1. Responsabilidade da inteligência

Se faltar qualquer dado necessário: identificar o campo ausente; identificar a venda ou registro afetado; explicar qual cálculo fica comprometido; alertar o usuário; não inventar nem completar informações sem fonte; permitir que o usuário solicite a correção à equipe responsável.

O sistema deverá preservar a tabela de comissão aplicada na época de cada venda.

# 11. MÓDULO DE ROI E INVESTIMENTOS

Prioridade do projeto. Acompanhamento diário e fechamento mensal.

## 11.1. Orçamento disponível

Mostrar: lucro bruto operacional, reserva formada, investimento realizado, saldo disponível (reserva acumulada disponível − investimentos registrados) e percentual da reserva consumido. O acúmulo entre meses ainda precisa ser definido.

## 11.2. Registro diário de investimento

O usuário informa diariamente quanto investiu. O sistema atualiza automaticamente: investimento diário, acumulado no mês, média diária, reserva disponível, percentual consumido e projeção de gasto até o fechamento.

## 11.3. Relacionamento entre investimentos e contratos

Cada contrato deverá ter, quando disponível: origem, campanha, data, operadora, modalidade, vendedor, unidade, valor mensal, agenciamento, vitalício, comissão do vendedor e impostos. Sem origem/campanha, alertar que o contrato não pode ser atribuído a um investimento.

## 11.4. ROI projetado

Considera agenciamento previsto, vitalício previsto, impostos e comissões dos vendedores. Deve ficar explícito que é projeção.

## 11.5. ROI realizado

ROI = [(retorno líquido atribuído − investimento) ÷ investimento] × 100. Distinguir receita gerada, retorno líquido atribuído, valor investido, resultado após investimento e percentual de ROI.

## 11.6. Inteligência para recomendar investimentos — REMOVIDO (v1.4)

> Decisão do usuário (v1.4): o sistema não exibe recomendações nem justificativas ("por quê"). Mostra apenas os dados. O texto abaixo fica só como histórico.

Analisar reserva, investimento realizado, contratos gerados, retorno projetado e recebido, evolução do ROI e capacidade financeira. Recomendar se o investimento está baixo, adequado ou elevado, se há oportunidade de expansão, se o retorno está negativo ou se é necessário reduzir/suspender. Toda recomendação deve ter justificativa e indicadores. Não recomendar aumento apenas porque existe saldo.

# 12. FECHAMENTO MENSAL E INDICADORES EXECUTIVOS

- **Financeiro:** comissões previstas e recebidas, impostos, comissões dos vendedores, custos fixos, provisão, resultado operacional, reserva de marketing, resultado financeiro.
- **Comercial:** produção total, por unidade, vendedor, operadora, PF/PME; agenciamento e vitalício gerados; comissões dos vendedores.
- **Investimentos:** reserva, investimento diário e acumulado, saldo, contratos gerados, retorno projetado e realizado, ROI, recomendação para o próximo período.

## 12.4. Lucro ou prejuízo por unidade (v1.2)

Exibido de forma direta, sem sugestões: uma aba para Consolação, uma para Mogi e o consolidado no topo da visão geral.

- Resultado operacional = comissões efetivamente recebidas − 15% de imposto − comissões dos vendedores − custo fixo − provisão 13º/férias. Positivo = LUCRO; negativo = PREJUÍZO.
- Mínimo para não fechar no vermelho = (comissões dos vendedores + custo fixo + provisão) ÷ 0,85.
- Mínimo sustentável: ver 12.7 (v1.6).
- Resultado financeiro = resultado operacional − reserva de marketing.
- Custo total da Optas no mês = comissões dos vendedores + custo fixo + provisão 13º/férias (sem impostos e sem reserva de marketing).

## 12.5. Somente valores efetivos (v1.3)

- Este painel ignora qualquer projeção (Ag. doc., Standby, pipeline, cenários, gasto projetado, ROI projetado). Projeção é usada apenas no painel TV, como norte para os gestores.
- Produção e comissão dos vendedores: apenas contratos efetivos (em contrato + implantado).
- Agenciamento e vitalício "a receber": valor que a Optas receberá das operadoras pelos contratos efetivos, conforme a comissão de cada operadora. Não é chamado de "previsto".
- ROI: somente com valor efetivamente recebido.
- Indicadores da visão geral exibem apenas título e número, sem textos explicativos.

## 12.6. Resultado financeiro do mês (v1.6)

Indicador da visão geral, definido pelo usuário:

- Custo total da Optas no mês = comissões dos vendedores + custo fixo + provisão 13º/férias.
- Impostos = 15% × a receber das operadoras.
- Reserva de marketing = 15% × produção mensal (soma das mensalidades dos contratos efetivos).
- **Resultado financeiro = a receber das operadoras − impostos − custo total da Optas no mês − reserva de marketing.**
- Para fechar no verde, o valor a receber precisa cobrir impostos, custo total e reserva de marketing.

## 12.7. Mudança da base da reserva de marketing (v1.6)

Decisão do usuário: a reserva de marketing passa a ser **15% da produção mensal**, substituindo a regra anterior (15% do lucro bruto operacional, seção 9). Vale para todo o painel: resultado das unidades, consolidado, mínimo sustentável e saldo de investimento.

- Mínimo sustentável = (comissões dos vendedores + custo fixo + provisão + reserva de marketing) ÷ 0,85.

## 12.8. Investimentos e ROI (v1.7)

- O usuário registra os investimentos escrevendo em português (ex.: "gastei 1.500 em tráfego pago no Facebook dia 10", "investimos 3 mil em leads em novembro"). O sistema identifica valor, data (ou mês), tipo e campanha, mostra como entendeu e só registra após confirmação.
- Limite de investimento = 15% da produção do mês (reserva de marketing). O painel mostra **dentro dos 15%** ou **passou dos 15%**, quanto foi usado e quanto sobra ou excedeu.
- **ROI sobre as vendas = (vendido no mês − investido no mês) ÷ investido no mês**, em que vendido = produção dos contratos efetivos. Também mostra o valor vendido para cada R$ 1,00 investido.
- A tabela de retorno por campanha só aparece quando houver contratos com campanha informada.

## 12.9. Base única: a receber das operadoras (v1.9)

- Não há mais lançamento manual de comissões recebidas nem importação de CSV.
- Todo o painel (visão geral, unidades, ano, financeiro) usa o **valor a receber das operadoras**: contratos efetivos × comissão de cada operadora (tabela gravada na época da venda → regra do projeto → tabela da operadora).
- Imposto = 15% do a receber. Reserva de marketing = 15% da produção.
- Registro de investimento: o usuário escreve nome da campanha, valor e data; o sistema identifica a data sozinho (hoje, ontem, dia 10, 10/11, mês) e mostra numa linha do tempo, mais recente primeiro, com total por campanha.

## 12.10. Memória mensal, sustentação anual e balanço (v1.8)

- O mês corrente é gravado automaticamente enquanto está aberto; "Fechar mês" trava os números.
- Aba Ano: a receber no ano − custos no ano = resultado do ano. **Se sustentando no ano** se o resultado acumulado ≥ 0.
- Provisão de 13º e férias: provisionado até agora × obrigação do ano (R$ 1.623,15 × 12) e se o resultado do ano cobriu a provisão.
- Resultado mês a mês, tabela dos meses, melhor e pior mês, resultado por unidade.
- Em dezembro, "Fechar o ano" grava o balanço geral, fecha todos os meses e leva o saldo (depois da reserva) para o ano seguinte. O balanço pode ser impresso ou salvo em PDF.

## Pendências resolvidas pelas decisões acima

- Pendência 4 (base do ROI): ROI sobre as vendas.
- Pendência 5 (categorias de investimento): registro por nome de campanha.
- Pendência 6 (origem dos contratos): não é mais necessária para o ROI.

## 12.11. VR e VT por dia útil (v2.0)

- Os valores de VR e VT informados (seção 3.3) são os totais de **outubro/2026**, que teve **21 dias úteis** (22 dias de segunda a sexta − 12/10).
- Valor por dia útil: Consolação VR R$ 197,16 e VT R$ 75,06 (por pessoa, 5 CLT: VR R$ 39,43 e VT R$ 15,01); Mogi VR R$ 173,35 e VT R$ 80,54 (por pessoa, 4 CLT: VR R$ 43,34 e VT R$ 20,13).
- **VR/VT do mês = valor por dia útil × dias úteis do mês.** Dias úteis = segunda a sexta − feriados nacionais (inclui Sexta-feira Santa).
- O custo fixo de cada mês passa a variar com os dias úteis; outubro reproduz exatamente R$ 39.185,43.
- Pendência 10: feriados municipais (São Paulo e Mogi das Cruzes), Carnaval, Corpus Christi e recesso de fim de ano.

## 12.12. Cálculo do a receber, proposta a proposta (v2.1)

- **A receber de cada proposta = valor mensal da proposta × % de agenciamento da operadora** (ou do Projeto Hapvida). O total do mês é a soma de todas as propostas efetivas.
- Exemplo: R$ 54.886,64 de propostas, todas Amil (300%) → R$ 164.659,92 a receber.
- Depois saem os descontos, nesta ordem: imposto 15% do a receber → comissões dos vendedores → custos fixos → provisão = lucro ou prejuízo; e então a reserva de marketing (15% da produção).
- A visão geral mostra "De onde vem o a receber" (por operadora: mensalidades × % = a receber) e a aba Comercial lista cada proposta com %, a receber, imposto e líquido.
- Proposta sem regra de comissão (ex.: Projeto Hapvida pendente) aparece como "fora da conta" e o valor de mensalidade excluído é mostrado.

## 12.13. Arredondamento em centavos (v2.2)

- Todo valor é arredondado em centavos no momento do cálculo (meio centavo para cima), e cada total é a soma exata das linhas exibidas.
- Comissão do vendedor: arredondada por vendedor (ex.: 30% × R$ 3.590,75 = R$ 1.077,225 → R$ 1.077,23).
- A receber: arredondado por proposta.
- Imposto: 15% do total a receber da unidade, rateado entre as propostas pelo método dos maiores restos (a soma das propostas bate com o total).
- Reserva de marketing: 15% da produção de cada unidade; consolidado = soma das unidades.
- Consolidado = soma das unidades, campo a campo.

## 12.14. Tabelas das operadoras recebidas em 24/11/2026 (v2.3)

| Operadora | PF | PME | Observação |
|---|---|---|---|
| Hapvida (fora do projeto) | a confirmar | 350% + 2% | o valor já registrado era de PME |
| MedSênior | 200% + 2% | a confirmar | |
| Prevent | 200% (vitalício a confirmar) | não vende | só PF |
| Santa Helena | 300% + 2% | 300% + 2% | informado sem modalidade (provisório) |
| Sobam | 300% + 2% | 300% + 2% | informado sem modalidade (provisório) |
| Ana Costa | 300% + 2% | 300% + 2% | informado sem modalidade (provisório) |
| Supermed | 30% efetivo | 30% efetivo | 130% − 100% de taxa de angariação (não vem para a Optas); vitalício a confirmar; sem modalidade |
| Qualicorp | 50% efetivo | 50% efetivo | 150% − 100% de taxa de angariação; vitalício a confirmar; sem modalidade |
| Trasmontano | a confirmar | 300% + 5% | |
| São Cristóvão | a confirmar | a confirmar | |

Regra de aplicação por venda: percentual da modalidade da venda; se a operadora só tem percentual sem modalidade, ele é usado como provisório; se a operadora não vende a modalidade (ex.: Prevent PME) ou a modalidade está pendente, a venda fica fora da conta e gera alerta.

## 12.15. Nome "Lucro líquido" (v2.3)

O valor final (lucro do mês − reserva de marketing), antes chamado "Resultado financeiro" / "Depois de separar a reserva", passa a se chamar **Lucro líquido** em todo o painel.

## 12.16. A receber · vitalício (v2.4)

- Separado do agenciamento. **Vitalício previsto do mês = Σ (valor mensal × % de vitalício da operadora/modalidade)** de todos os contratos ativos da carteira (de qualquer ano) que estão na 4ª parcela ou depois. Parcela = meses desde o início do contrato + 1. Cancelados saem a partir do mês do cancelamento.
- Vitalício recebido: relatórios das operadoras, lançados por operadora e mês. O painel mostra previsto × recebido × diferença, por operadora e mês a mês (aba Vitalício). Imposto de 15% e líquido previsto exibidos.
- O vitalício ainda **não** entra no lucro bruto/líquido (decisão pendente).
- Planilha: novas abas "Carteira ativa" e "Vitalício recebido".
- Removidos por decisão do usuário: "% atingido" nas metas e a tabela "Fechamento do mês" da aba Financeiro.

## 12.17. Revisão geral (v3.0 · 24/11/2026)

**Cálculos (todos em centavos, consolidado = soma das unidades):**
- Custo da operação = custos fixos + provisão 13º/férias.
- **Custo de operação total = custo da operação + impostos** (ex.: 39.756,36 + 24.698,99 = 64.455,35).
- Custos do mês = custo de operação total + comissões dos vendedores.
- **Lucro bruto = a receber − comissões − custo de operação total.** Margem bruta = lucro bruto ÷ a receber.
- **Lucro líquido = lucro bruto − investimento REAL em marketing** (não a reserva). Margem líquida = lucro líquido ÷ a receber.
- Investido em marketing (%) = investido ÷ a receber.
- Investimento por unidade: lançado com a unidade (texto com "Mogi"/"Consolação") fica nela; o resto é rateado pela produção.
- Mínimos: "não fechar no vermelho" (lucro bruto ≥ 0) e "não fechar no vermelho e investir" (lucro bruto ≥ reserva de marketing).
- **ROI = (retorno − investido) ÷ investido**; retorno = a receber das vendas ligadas a cada campanha (nome da campanha/origem do CRM, planilha ou sistemas). Venda sem campanha de marketing fica fora do ROI.
- Ano: mês "se pagou" quando lucro bruto ≥ 0; reserva e investido lado a lado; lucro líquido do mês = lucro bruto − investido; acumulado = saldo anterior + lucros líquidos.

**Cores:** verde = dinheiro que entra; vermelho = dinheiro que sai; amarelo = investimento.

**Novas funções:** gráficos de vendas por operadora (valor e vidas); exportação Excel das comissões por vendedor com as propostas; barra de conversa (perguntas e registros em português, resposta só com dados); tudo recalcula sozinho a cada mudança.

**Publicação:** a versão publicada (Apps Script) não exibe as abas Pendências e Regras.

**Na fila:**
- Projeto Hapvida · pagamento ao vendedor: 15% + R$ 20,00/vida (25 a 34 vidas), R$ 25,00/vida (35 a 49), R$ 35,00/vida (50 ou mais) — aguardando confirmação da base e da aplicação.
- Projeto Hapvida · quanto a Optas recebe — aguardando o usuário.
- Integração com CRM, planilha e sistemas internos para ligar cada venda à campanha.

## 12.18. Identificação da proposta e gráficos (v3.1)

- Toda proposta é identificada pelo **nome do titular (PF) ou da empresa (PME)** e pelo **CPF (PF) ou CNPJ (PME)**. O sistema valida os dígitos verificadores e se o documento combina com a modalidade; falhas viram alerta.
- Lista de propostas (Comercial) com cliente, CPF/CNPJ, modalidade, operadora, vidas, vendedor, mensalidade, %, a receber, imposto e líquido; a exportação de comissões inclui cliente e documento.
- Gráficos de pizza no fim da aba Comercial, da operadora que mais vendeu para a que menos vendeu, com lista ao lado: um por valor e outro por vidas. Passar o mouse destaca; clicar filtra as propostas.
- Planilha: colunas Cliente, CPF/CNPJ e Vidas na aba Vendas.

## 12.19. Operadoras só PME (v3.2 · 24/11/2026)

Confirmado pelo usuário: **Alice, Porto, SulAmérica, Bradesco, Amil e Seguros Unimed vendem só PME**, com os percentuais já informados (Bradesco 400% + 4%; demais 300% + 2%). Venda PF dessas operadoras gera alerta e fica fora da conta.

## 12.20. MedSênior, operadoras só PME e Adesão (v3.3 · 24/11/2026)

- **MedSênior:** PME 200% + 2% (valor que já estava registrado era PME); **PF 200% sem vitalício**.
- **Santa Helena, Sobam e Ana Costa:** só PME, 300% + 2%.
- **Supermed e Qualicorp:** venda de **Adesão** (nem PF nem PME). Têm taxa de 100% da primeira parcela que não vem para a Optas: Supermed 130% → 30% efetivo; Qualicorp 150% → 50% efetivo. Vitalício a confirmar. Titular da adesão é pessoa física → identificação por CPF.
- Modalidades do sistema: **PF, PME e Adesão**.

## 12.21. Grade de Comissão V3 e caixa por parcelas (v4.0 · 24/11/2026)

**Fonte das comissões:** Grade de Comissão V3 (W3G), atualizada em 02/10/2026 — substitui todos os percentuais anteriores (que estavam errados, segundo o usuário). Contém Saúde Adesão, PF e PME, Odontológico PF e PME e Pet, com percentual de cada parcela, faixa de vidas, produto/condição e vitalício. Arquivo: `data/grade-comissao.json`.

**Projeto Hapvida:** 100% em parcela única, sem vitalício, para PF e PME.

**Modelo de caixa (regra do usuário):**
- A 1ª parcela de cada venda entra no mês da venda; a 2ª no mês seguinte, e assim por diante, conforme a grade.
- **A receber no mês = 1ª parcela das vendas do mês + parcelas das vendas dos meses anteriores.**
- ~~A meta é o mês se pagar só com a 1ª parcela~~ → **substituído em 12.24 item 8**: o mês se paga com o a receber total do mês.
- O painel mostra o que já está garantido para os próximos 6 meses (parcelas das vendas já feitas).
- ROI: retorno = comissão total contratada (todas as parcelas) das vendas da campanha.

**Escolha da linha da grade para cada venda:** operadora + modalidade + produto/condição (se informado) + faixa de vidas. Venda fora da faixa de vidas ou em modalidade que a operadora não vende fica fora da conta e gera alerta.

**Adesão:** a 1ª parcela é a taxa de angariação cobrada do cliente; por informação anterior do usuário, não entra no a receber da Optas (a confirmar).

- **Amil PME: vitalício de 1%** (confirmado pelo usuário em 25/11/2026; a grade V3 omitiu — é o único erro da grade).

**Dúvidas em aberto:** Hapvida PME e NotreDame PME têm total 290% na grade, mas as parcelas somam 310% (100/90/80/40); início do vitalício; taxa da adesão; Prevent Senior 0 a 18 anos (0%) depende da idade do titular.

## 12.22. Respostas de 25/11/2026 (v4.1)

1. **Hapvida PME e NotreDame PME: 290%** — parcelas 100/90/80/20.
2. **Adesão:** a 1ª parcela (taxa de angariação) **não vem para a Optas**.
3. **Vitalício começa depois da última parcela de agenciamento** (ex.: Bradesco PME a partir da 5ª; Amil PME a partir da 4ª).
4. **Prevent Senior não comissiona titulares de 0 a 18 anos**; a idade vem da data de nascimento do cliente (documentação). Sem data: usa 19+ e gera alerta.
5. **Vendedor no Projeto Hapvida:** 15% da mensalidade + valor por vida sobre todas as vidas do mês quando atinge 25 (25 a 34 → R$ 20; 35 a 49 → R$ 25; 50+ → R$ 35); abaixo de 25 vidas não paga por vida. Vendas fora do projeto seguem a faixa da unidade (ver 12.23).

## 12.23. Respostas de 25/11/2026, segunda rodada (v4.2)

1. **Faixa do vendedor:** a produção do Projeto Hapvida **conta para a meta toda**. A faixa da unidade é atingida com a produção total (projeto + fora); o percentual incide sobre as vendas fora do projeto. O projeto continua pagando 15% + valor por vida.
2. **Vitalício entra no lucro:** o vitalício do mês soma no a receber (com 15% de imposto). Usa o **recebido** quando o relatório do mês foi lançado; antes disso, o previsto da carteira. Por unidade: pela unidade do contrato; sem unidade, rateado pelo vitalício previsto de cada unidade.
3. **Reserva de marketing não usada passa para o mês seguinte** (fôlego). Limite do mês = 15% da produção + Σ (reserva − investido) dos meses anteriores do ano com produção conhecida. O que passou do limite reduz o saldo.
4. **Feriados:** a Optas segue São Paulo capital: nacionais + Sexta-feira Santa + Aniversário de SP (25/1) + Revolução Constitucionalista (9/7) + Corpus Christi. **Carnaval (segunda e terça) não é dia útil** — a Optas não trabalha.
5. **Sócios não recebem VR nem VT** (o valor por pessoa já é dividido só pelos CLT).
6. **Custos de janeiro a setembro:** replicam a estrutura atual (outubro), com VR/VT pelos dias úteis de cada mês.
7. **Investimento em marketing de 2026:** só os envios de SMS (Kolmeya) do centro de custos **NOVO OPTAS MOGI**, campanha "SMS", unidade Mogi. 37 envios de janeiro a outubro, conferidos envio × R$ 0,0530; arredondamento por mês para o total bater com o relatório. Novembro sem investimento; de dezembro em diante o usuário lança no painel. Outubro confirmado pelo usuário (envio de 07/10). Centros de custo 4.0 CONSULTORIA, CONSÓRCIO e NOVO OPTAS CONSOLAÇÃO ficam fora.

| Mês | Investido (SMS Mogi) |
|---|---:|
| Jan | 4.907,06 |
| Fev | 10.202,34 |
| Mar | 12.139,44 |
| Abr | 8.018,16 |
| Mai | 5.613,44 |
| Jun | 7.186,38 |
| Jul | 18.612,86 |
| Ago | 17.119,37 |
| Set | 1.774,81 |
| Out | 2.352,62 |
| **Total** | **87.926,48** |

8. **ROI:** até novembro/2026, **ROI geral** = (comissão contratada de todas as vendas do mês − investido no mês) ÷ investido, por unidade e consolidado, sem rastrear venda a venda. A partir de dezembro/2026, ROI por campanha (cada venda ligada à campanha de origem).
9. **Planilha "Leads GNDI" (operação do Projeto Hapvida):** fonte das vidas do projeto por vendedor (aba Painel de Implantação). **O valor por vida conta só as vidas implantadas no mês** (data da Hapvida). **A equipe Gileade não conta para a Optas.** Lida ao vivo pelo Apps Script (`optasVidasProjeto_`). Também tem: leads por campanha, funil do PipeRun por card, propostas PJ do Planium (CNPJ, vidas, vigência, data implantada), datas de implantação, fora do projeto por vendedor.
10. **ERP (propostas, parcelas e beneficiários de Mogi e Consolação), 25/11/2026:**
   - Data da venda = **data de cadastro** (DtProducao).
   - Comissão da Optas = parcelas de **Ordem 1** do ERP (corretora Optas Mogi / Verus Consolação), valor = parcela × %; substitui a grade nessas propostas. Vitalício = linhas marcadas como vitalício.
   - Adesão (GeraComissaoPrimeira = Falso): 1ª parcela é a taxa, não entra. Na adesão as parcelas vêm com a administradora (Qualicorp, Supermed, TECGROUP).
   - Situação: cancelada (inclusive na operadora) registra e sai da conta; cancelada sem confirmação da 1ª com 90 dias ou mais desde o cancelamento = cancelada; com menos de 90 dias = válida em aberto; inadimplente = válida e implantada; implantado = implantado; o resto = válida em aberto. **A exportação recebida não tem a coluna de situação** — até chegar, todas são válidas.
   - Conferência: Σ parcelas da Optas no CSV R$ 1.141.906,29 − taxas de adesão R$ 50.098,65 = R$ 1.091.807,64 importados.
   - Os dados do ERP (com clientes) ficam fora do repositório (`data/erp/`, gitignored); `python3 -I data/importar_erp.py <pasta>` gera o arquivo.
11. **Extratos de comissão (SisWeb W3G → Optas), 25/11/2026:** 23 extratos (Mogi nov/25–out/26; Consolação jan–nov/26), 3.816 linhas, 231 créditos/débitos.
   - Conferência por extrato (todas batem): Σ líquido das linhas = Ato da venda + Parcelas; saldo anterior + comissões + créditos/débitos = líquido do extrato.
   - De-para com o ERP: 613 linhas casadas, todas com o valor do ERP no centavo (Unihosp e Med-Tour: 1ª parcela com líquido zero, como no ERP). Nenhuma parcela paga duas vezes. Pagamento costuma vir 2 a 3 meses depois do vencimento.
   - 231 parcelas do ERP vencidas há 3+ meses do último extrato e não pagas (R$ 326.419,64); 82 propostas sem nenhum pagamento — dependem da situação das propostas.
   - Desconto administrativo de 8,5% nas parcelas a partir da 2ª (Mogi em todas; Consolação nas novas; vitalício antigo de Consolação sem desconto).
   - Vitalício do mês = vitalício recebido nos extratos da unidade (bruto); sem extrato no mês, o previsto do ERP.
   - Créditos/débitos = salários, benefícios, férias/13º, rescisões, comissão do gestor (Valdecir 40%), adiantamentos de parcela, estornos, boletos de clientes, campanhas/premiações e SMS.
   - Médias por mês: unidades pelo ERP (data de cadastro); vendedores pelos meses gravados no painel.
12. **Respostas sobre os extratos (25/11/2026):**
   - Desconto administrativo de 8,5% **faz parte dos 15%** (metade desconta do corretor final, metade a W3G paga): o painel não desconta à parte; o a receber segue bruto e o imposto de 15% cobre.
   - "AD nª PARC" = adiantamento da 1ª parcela para o corretor Optas (equipe Valdecir em Mogi, Joana em Consolação).
   - SMS descontado no extrato ("LEADS – 44.716 SMS") é o mesmo custo do investimento já lançado: não duplica.
   - Créditos/débitos por tipo (mês = mês do extrato): **soma no a receber** — campanhas, acertos, devoluções e diferenças de desconto da 1ª parcela, premiações de operadora, comissões do Departamento de Seguros; **custo da unidade** — vales, adiantamentos (AD), estornos, rescisões, 10% sobre parcela, taxa de implantação, premiação para vendedor (R$ 100/vida); **custo de operação** — boletos de clientes e comissão do Valdecir 40% (Mogi, no mês do desconto; encerrada em julho/2026 — se aparecer depois, o painel alerta); **ignorado** — SMS (já é investimento).
   - **Folha (salários, benefícios, férias, 13º):** em **qualquer mês**, se o extrato da unidade trouxer salário para o mês, a folha **sobrepõe** a estrutura (**no mês devido**, sem provisão, comissões dos vendedores já dentro da folha → comissão à parte = 0 no resultado). Sem folha no extrato, vale a estrutura informada pelo usuário. Nunca soma as duas.
   - **Mês devido (25/11/2026):** salário, benefícios, férias, 13º, rescisão e vale entram no mês a que se referem, lido na descrição ("SALÁRIOS - SETEMBRO 2026" → setembro; "SALÁRIO - JOANA 07/09" → setembro; "RESCISÃO ... 02/10" → outubro), e não no mês em que o extrato descontou. Sem ano na descrição → o mês mais recente até o do desconto. Sem mês na descrição → mês do desconto. Boletos, estornos, AD, Valdecir e receitas continuam no mês do desconto. Mês sem salário lançado (ainda não descontado) → vale a estrutura.
   - **Empréstimos (fora do resultado):** "Retiradas Joana e boleto apartamento" (+R$ 64.773,05, maio/2026) = empréstimo a abater da operação; aluguel Verus −R$ 22.744,32 (março, empréstimo) e +R$ 22.744,32 (maio, quitado).
   - **Explicação do usuário (26/11/2026):** os R$ 64.773,05 (extrato 424786, Consolação, previsão 05/05/2026) são ~R$ 50 mil de salário da Joana (ela recebeu nos meses anteriores sem desconto no relatório; o salário dela só aparece descontado a partir de 08/04) + ~R$ 14 mil emprestados para o apartamento dela. Apesar de positivo, é empréstimo → fora da conta. Os +R$ 22.744,32 do aluguel Verus no mesmo relatório são reembolso do aluguel que a Joana pagou do próprio bolso → correto; com o débito de março, soma zero. **Regra:** lançamento fora do padrão (retirada, empréstimo, reembolso pessoal) → perguntar ao usuário se desconta ou não antes de decidir.
   - **Decisões de 26/11/2026 (perguntas sobre casos parecidos):**
     - Os 5 "VALE" da Consolação, de jan a mar/2026, somam R$ 46.000,00: jan 5.000, fev 17.000, mar 7.500 + 15.000 + 1.500 ("10% - VALE").
     - O "BOLETO CONSTHRUIR ENGENHARIA – JOANA" (mar, −R$ 15.273,05) é do apartamento.
     - Esses vales e o boleto são a mesma retirada da Joana devolvida em maio. Saem da conta, como a devolução. Total tirado do custo: R$ 61.273,05.
     - Os gastos com nome Verus (rescisões, estágio, R$ 100 por vida) continuam como custo.
     - "ACERTO FOLHA" (+R$ 33.342,54, fev) agora entra no a receber, com imposto de 15%.
     - "AD COMISSÃO ... FOLHA NEGATIVA" (−R$ 14.587,60, jan) continua no custo. Os dois contam.
13. **Fonte dos dados reais:** fechamento de folha mensal (vendas e vitalícios recebidos), relatórios de recebimento (o que entrou, atrasou e falta receber), acesso ao Apps Script e ao ERP.


## 12.24. Decisões de 25/11/2026, terceira rodada (v4.3)

0. **Nome do sistema:** o ERP da operação se chama **SisWeb** (propostas, parcelas, beneficiários e extratos de comissão). No painel aparece sempre como SisWeb; neste documento, "ERP" = SisWeb.

1. **A receber com ajuste de 90 dias:** valor e data vêm do SisWeb (sem simulação quando o SisWeb tem o dado): data prevista = **vencimento da parcela no SisWeb**; só sem vencimento usa 30 dias depois do último pagamento. Recebida (achada no extrato) → entra no mês dela pelo valor que veio no extrato. Não recebida: em dia até a data prevista; atrasada até 90 dias depois; **passados 90 dias sem receber, sai da conta** e o mês fica com o que realmente entrou.
2. **Atrasado vai para o próximo recebimento:** na aba **A receber**, toda parcela atrasada aparece no mês atual, proposta a proposta, com data prevista e dias de atraso. O lucro de cada mês continua contando a parcela no mês dela enquanto está dentro dos 90 dias (sem duplicar).
3. **Projeto Hapvida:** entra como a receber no mês (100% da 1ª mensalidade), ainda sem fonte de recebimento; previsto 30 dias depois do fim do mês da venda. Passa pela mesma regra de atrasado e 90 dias.
4. **Salários sem mês na descrição:** ficam no mês do desconto (sem retroativo).
5. **Vendas fora do projeto no mês atual:** só as cadastradas no ERP (produção, 1ª parcela, contratado e reserva). O PipeRun fica só para a comissão de cada vendedor até a integração completa.
7. **ROI = (1ª parcela das vendas do mês − investido no mês) ÷ investido**, com o valor da 1ª parcela do SisWeb (o recebido, quando já veio no extrato). Geral até novembro/2026; por campanha a partir de dezembro/2026 (1ª parcela das vendas de cada campanha).
8. **Metas do mês ("não fechar no vermelho" e "não fechar no vermelho e investir"):** medidas pelo **a receber total do mês** (1ª parcela + parcelas anteriores + vitalício + outras receitas), não só pela 1ª parcela. O ROI continua pela 1ª parcela (item 7).
9. **Comissões dos vendedores:** não é preciso folha. Os relatórios de pagamento (extratos SisWeb) já mostram o que foi pago de comissão aos vendedores; no resultado de cada mês fechado a comissão à parte é zero, com ou sem salário lançado no extrato (janeiro, setembro e outubro passam a ter resultado). No mês corrente, enquanto o extrato não chega, fica a estimativa pela faixa do vendedor.
10. **Vendedor de cada venda:** vendas até novembro/2026 não são atribuídas a nenhum corretor. A partir de dezembro/2026 a Optas informa o vendedor responsável de cada venda.
11. **Vitalício: só o recebido.** Sai o previsto. O vitalício do mês (no a receber, nas metas, no ano e na aba Vitalício) é só o que os relatórios de pagamento mostram como pago. A aba mostra, por operadora e mês a mês, parcelas pagas, mensalidades, % de vitalício recebido (recebido ÷ mensalidades), recebido bruto e líquido. Unidade sem relatório no mês = vitalício zero até o relatório chegar.
12. **Relatório de todo dia 5:** a Optas recebe um novo relatório de pagamento todo dia 5 e o envia para atualizar o painel; ele vale para o mês que está começando (mês do pagamento).
13. **Custos detalhados:** na aba Ano, clicar nos custos de um mês abre o detalhe por unidade (imposto, comissões, folha ou estrutura + provisão, lançamentos dos relatórios), somando no centavo os custos do mês.
14. **Cancelar proposta atrasada:** na aba A receber, parcela atrasada tem o botão "Cancelada". Marcada, a proposta tem as parcelas não recebidas tiradas do a receber de todos os meses (o já recebido continua). Lista "Propostas canceladas" com Desfazer. Fica salvo no estado do painel.
6. **Empréstimo (retiradas da Joana, boleto do apartamento, aluguel Verus):** fora do sistema, pago por fora; o painel ignora esses lançamentos.

# 13. ESCOPO FORA DA PRIMEIRA ETAPA

Distribuição de lucros entre W3G e sócias; média de comissões para provisionamento da folha; controle individual de salários fixos; CPL e ROI avançado sem atribuição confiável; conciliação detalhada de cada pagamento das operadoras; controle avançado de estornos, cancelamentos, descontos e recebimentos parciais.

# 14. PENDÊNCIAS PARA FINALIZAR A MODELAGEM

1. **Tabelas das operadoras:** percentuais de MedSênior, Prevent, Santa Helena, Sobam, Supermed, Qualicorp, Ana Costa, São Cristóvão e Trasmontano (agenciamento, vitalício, PF/PME, diferenças por modalidade) e modalidade das sete já informadas.
2. **Vitalício:** início na 4ª parcela para todas? Base: valor original ou atualizado? Continuidade igual para todas as modalidades?
3. ~~Acúmulo da reserva de marketing~~ — resolvido em 12.23 (passa para o mês seguinte).
4. **Base definitiva do ROI:** componentes do retorno líquido atribuído.
5. **Categorias de investimento diário:** tráfego pago, compra de leads, campanhas comerciais, outras ações de captação (a validar).
6. **Origem dos contratos:** a integração disponibilizará origem, campanha e investimento correspondente?
7. **Validação contábil dos encargos:** FPAS/terceiros, RAT, incidências, encargos já incluídos nos R$ 39.185,43.

8. **Comissão do Projeto Hapvida:** agenciamento e vitalício do projeto.
9. **Vínculo com planilha e CRM:** link da planilha e campos do PipeRun com as vendas linha a linha, incluindo a marcação de projeto.

# 15. INSTRUÇÕES PARA CONTINUAR O PROJETO

1. Tratar todas as informações confirmadas como regras atuais da Optas.
2. Manter os valores financeiros exatamente como registrados.
3. Não somar os R$ 15.000,00 de PJ novamente aos custos.
4. Não misturar salários CLT com pagamentos PJ.
5. Não utilizar médias de comissão dos vendedores.
6. Aplicar as faixas de comissão conforme as regras de cada unidade.
7. Não misturar as comissões da Optas com as comissões pagas aos vendedores.
8. Aplicar os 15% de imposto sobre agenciamento e vitalício, independentemente da operadora.
9. Calcular a reserva de marketing pela fórmula expressamente definida.
10. Distinguir comissões previstas de comissões efetivamente recebidas.
11. Não tratar reserva de marketing como despesa operacional.
12. Não inventar informações ausentes.
13. Alertar quando os dados integrados forem insuficientes.
14. Manter as pendências separadas das regras já confirmadas.
15. Atualizar este documento sempre que o usuário fornecer novas regras ou percentuais.
16. Não reabrir questões já resolvidas.
17. Fazer uma pergunta por vez quando faltar uma decisão indispensável.
18. Não ampliar o escopo sem autorização.

**Prioridade de continuidade:** fechar as tabelas de comissão das operadoras, as regras do vitalício e as decisões do módulo de ROI e orçamento de marketing.

**Cada custo no mês a que se refere (25/11/2026):** os relatórios de Mogi chegam com atraso (o de janeiro/2026 traz salário e benefícios de nov–dez/2025, comissão do Valdecir de novembro/2025 e o 13º/2025). Além de salário, benefícios, férias, 13º, rescisão e vale, também a **comissão do Valdecir** ("COMISSÃO NOVEMBRO 2025") e o **adiantamento/folha negativa com data** ("AD COMISSÃO 13/08 …") vão para o mês da descrição. **13º sem mês pago em janeiro ou fevereiro → dezembro do ano anterior.** Sinal: valor com "-" é saída; sem sinal é entrada. **Regra do sinal (decisão do usuário):** em todo crédito/débito que entra na conta, valor com "-" é **custo** e valor sem sinal é **a receber**, qualquer que seja o tipo (ex.: campanha +2.250 entra no a receber e a mesma campanha −2.250 entra nos custos; estorno positivo vai para o a receber). Folha segue como folha; SMS e empréstimos seguem fora. O mês de cada relatório é o da **previsão de pagamento**.

**A receber detalhado (25/11/2026):** na aba Ano, clicar no a receber de um mês (verde) mostra, por unidade, de onde vem cada valor: 1ª parcela das vendas do mês (proposta a proposta), parcelas de vendas anteriores, vitalício recebido por operadora e créditos dos relatórios de pagamento (sem sinal). O detalhe dos custos não lista mais o que vai para o a receber. Clicáveis seguem as cores: verde = entrando, vermelho = saindo, amarelo = investimento (sem azul de link).

**Entradas e saídas do mês (25/11/2026):** na aba Ano, o mês selecionado mostra um quadro único: linhas = categorias, colunas = Consolação · Mogi · Total. Entradas: agenciamento 1ª parcela, parcelas seguintes, vitalício, campanhas, premiações, Depto. de Seguros, acertos, desconto devolvido, estornos devolvidos. Saídas: imposto, salários, benefícios, férias, 13º, rescisões, vales, estrutura informada, provisão, adiantamentos de comissão, estornos, boletos, Valdecir, premiação de vendedor, taxa de implantação, campanhas estornadas. Cada categoria abre os itens. Fecha com total de entradas, total de saídas e resultado (lucro bruto); a auditoria confere centavo a centavo.

**Ano: unidades batem com o total (25/11/2026):** a sustentação do ano é o **lucro líquido** = a receber − custos − investido. Cada unidade mostra a mesma conta linha a linha (a receber − custos = lucro bruto − investido = lucro líquido), e Consolação + Mogi = total, centavo a centavo (auditoria confere bruto, investido e líquido). O investimento SMS Kolmeya é todo de Mogi.

### Salário sem relatório: média de 3 meses (25/11/2026)
- O salário de cada mês vem do relatório de pagamento do dia 5 (no mês a que se refere).
- Mês sem salário no relatório → salário = média dos últimos 3 meses com salário registrado na unidade. Benefícios sem registro no mês seguem a mesma regra.
- Sem 3 meses anteriores (Consolação, janeiro/2026), completa com os meses registrados mais próximos.
- Vale a partir do primeiro relatório de cada unidade; antes disso continua a estrutura informada.
- Como a folha dos relatórios já inclui as comissões dos vendedores, no mês pela média não se soma comissão à parte nem provisão (igual aos meses com relatório).
- Quando chega o relatório do mês, o valor real substitui a média.

### Vitalício: auditoria de 2026 (25/11/2026)
- Mês = data de previsão do extrato. Valor = líquido de cada linha (o "acumulado" é saldo transferido, não entra).
- Conferência: os 23 extratos do CSV são os mesmos 23 do PDF (12 Mogi, 11 Consolação), e a soma das linhas bate com o total de cada extrato.
- Vitalício = parcela além da grade de agenciamento do ERP. A parcela de 1% que ainda está dentro da grade (Bradesco Seguros parcelas 5 e 6, Porto Seguro parcelas 1 e 2) entra no a receber como parcela, não como vitalício.
- Sem proposta no ERP: percentual de transição não é vitalício (ADC Benefícios 5% nas parcelas 6–7, depois 1%).
- Recorrentes diferentes de 1%: Unimed CNU 2%, Prudential 5% e 10%, Unicor 2,5%.
- Mogi não tem extrato com previsão em novembro/2026, e Consolação não tem em outubro/2026.
- Total de 2026: Mogi 20.394,97 · Consolação 53.881,67 · total 74.276,64.

### Botões, rolagem e aba Ano (25/11/2026)
- Botões sem código dentro das tags (delegação por `data-a`): funcionam também em visualizadores que bloqueiam `onclick`.
- Tabelas largas: barra de rolagem maior, arrastar com o mouse e Shift + roda.
- Aba Ano: lucro bruto, lucro líquido, reserva de marketing e investimento em marketing também em % do a receber. "Investido" passa a se chamar "Investimento em marketing".

### Imposto — regra definitiva (confirmada pelo usuário em 26/11/2026)
Substitui o imposto de 15% sobre tudo (seção 8 e demais menções a "15% de imposto").

Vale linha a linha, pela coluna **"% Adm."** do relatório de comissões da W3G:

| % Adm. na linha | O que acontece | Imposto que a Optas paga |
|---|---|---|
| **8,50%** | A W3G já descontou 8,5% (Desp. Adm.) no recebimento | **8,5% sobre o valor que sobrou** (bruto − desconto da W3G) |
| **0,00%** | Nada foi descontado | **15% sobre o valor** |

- **Mês sem relatório:** 15% sobre tudo.
- **Como o painel aplica:** o a receber do mês vem da tabela de parcelas do SisWeb. A parte com desconto é o bruto das linhas com 8,50% nos relatórios daquele mês e unidade (no máximo o a receber), e o desconto da W3G entra na mesma proporção. O resto paga 15%. Cada valor é arredondado em centavos.
- **Nas saídas do mês aparecem três linhas:** Desconto W3G 8,5% · Imposto 8,5% sobre o que sobrou · Imposto 15% sem desconto W3G.
- **Vale para o sistema inteiro:** resultado do mês e do ano, unidades, consolidado, mínimo para não fechar no vermelho, vitalício e entradas/saídas.
- **Conferência:** `testes/auditoria-centavos.js` recalcula esse imposto em cada unidade e em cada mês.
- **2026:** desconto W3G 34.103,50 · imposto 8,5% 31.204,75 · imposto 15% 79.970,78 · total 145.279,03 (antes, com 15% em tudo: 140.153,52).

### Aba Vitalício: carteira, composição e pagamentos (26/11/2026)
- A tabela "mês a mês" do vitalício mostra só a carteira de vitalício, não as vendas novas. Diferença para "só as linhas de 1%": vitalício com outro percentual (Unimed 2%, Prudential 5% e 10%, Unicor 2,5%) entra; as linhas de 1% que ainda estão na grade de agenciamento (Bradesco parcelas 5 e 6, Porto parcelas 1 e 2) saem.
- **Carteira por unidade:** cada contrato conta uma vez no mês. "Parcelas acumuladas" = parcelas a mais do mesmo contrato no mesmo relatório. Mês sem relatório da unidade aparece como "sem relatório".
- **Carteira recorrente × vendas novas:** todas as linhas dos relatórios do ano, separadas em 1ª, 2ª, 3ª, 4ª parcela em diante e vitalício, com mensalidades e comissão líquida. Em 2026, o vitalício é 88,2% das mensalidades e 10,2% da comissão.
- **Situação dos pagamentos:** último relatório de cada unidade, com saldo acumulado e a observação (nota fiscal não recebida / transferido).
- A oscilação mensal vem de: unidades com relatórios em meses diferentes (outubro só Mogi, novembro só Consolação), Consolação aparecendo de fato só a partir de março, e parcelas acumuladas (março 168, novembro 139).

## Visual mais limpo — desfeito (26/11/2026)

- A limpeza visual foi desfeita a pedido do usuário: tirou informação importante. As telas voltaram a ser como antes. Rever a visualização mais tarde, com o sistema mais maduro.

## ROI — regra definitiva (26/11/2026)

Base: apostila "Aula Completa — Cálculo de ROI" (receita não é lucro; investimento entra uma vez só; não atribuir venda que não veio da iniciativa).

- **ROI = (contribuição − investido) ÷ investido.**
- **Contribuição** = 1ª parcela gerada pelas vendas **fora do Projeto Hapvida** (valor da proposta no SisWeb, não o a receber) − **imposto 15%** (a 1ª parcela vem com % Adm. 0,00% no relatório da W3G) − **comissão do vendedor** sobre essas vendas (faixa da unidade × produção fora do projeto).
- **Vendas do Projeto Hapvida não entram no ROI.**
- Cada unidade é medida só com o **próprio investimento**. Unidade sem investimento não tem ROI (hoje Consolação).
- **ROI geral** = média do ROI das unidades com investimento. Hoje é só Mogi; quando Consolação tiver investimento, vira a média das duas.
- Comissão do vendedor: mês com vendedores registrados usa o % real do mês; mês sem registro (até outubro/2026) usa o % médio dos meses registrados da unidade (Mogi 37,59%), marcado como "% estimado".
- A partir de dezembro/2026, a mesma contribuição é calculada venda a venda, por campanha.

Mogi 2026 (jan–out): investido R$ 87.926,48 · 1ª parcela R$ 172.406,43 · imposto R$ 25.860,97 · comissão R$ 111.101,88 · contribuição R$ 35.443,58 · **ROI do ano −59,7%** (antes: 224%).
- **Decisão (26/11/2026):** o ROI fica sobre a **1ª parcela gerada** ("é o que gera"). As parcelas seguintes não entram e não há ROI projetado ao lado.
- **Correção (26/11/2026): o ROI é sobre a 1ª parcela gerada, não sobre o que sobra.** ROI = (1ª parcela gerada pelas vendas fora do Projeto Hapvida − investido) ÷ investido. Imposto 15%, comissão dos vendedores e "o que sobra" continuam aparecendo na aba ROI só como informação. Mogi jan–out/2026: (172.406,43 − 87.926,48) ÷ 87.926,48 = **96,1%**.

## ROI fica "—" até chegar a lista das vendas do SMS (26/11/2026)

- Sem saber quais vendas vieram do SMS, o ROI **não é real** e o painel mostra **"—"** (Visão geral, aba Ano, aba ROI). A conta já está pronta e liga sozinha quando a lista entrar (`VENDAS_SMS` no código).
- **Próximo passo:** Mogi envia a lista das vendas que vieram do SMS do Kolmeya (proposta ou cliente, data e campanha). Com ela: ROI = (1ª parcela gerada pelas vendas do SMS − investido) ÷ investido, por mês e no ano.
- **Alternativa combinada (quando houver os dados):** cruzar pelo celular.
  - Kolmeya: exportação dos envios (celular, data do envio, campanha; se tiver, respostas/cliques).
  - SisWeb ou PipeRun: propostas com o celular do cliente.
  - Números padronizados em DDD + 9 dígitos (sem +55, espaços ou traços).
  - Venda conta como "veio do SMS" se o celular recebeu SMS **antes** da venda, numa janela de até 90 dias (ajustável). Vários envios: vale a última campanha antes da venda.
  - Por campanha: números disparados, clientes que fecharam, conversão (vendas ÷ envios), custo por venda e ROI.
  - Telefones ficam fora do GitHub (pasta `data/erp/`); o painel mostra só totais.
- Referência dos números anteriores (não são reais, só para comparação): todas as vendas fora do projeto de Mogi davam ROI de 96,1% em jan–out/2026; com Consolação e Projeto Hapvida juntos, 224%.
- Pendência 10 criada: "Vendas que vieram do SMS (Mogi)".

## Respostas de 26/11/2026: dados e dúvidas (v4.4)

**Dados**
1. **Vendas que vieram do SMS (Mogi):** continua pendente. O ROI fica "—" até a lista chegar.
2. **Planilha / PipeRun linha a linha:** não é mais fonte. **Daqui em diante vale o SisWeb.** Os alertas que dependiam da planilha (produção agregada por vendedor e contratos sem origem) saíram do painel real.
3. **Relatório da W3G:** traz operadoras, parcelas e a **data de previsão, que é a data do pagamento**. Junto com a exportação do SisWeb (situação e cancelamento das propostas), não falta nada para o mês.
4. **Atualização do dia 5:** manual, com o Claude. As vendas chegam antes pelo **Movimenta** (antes de entrar no SisWeb); no relatório é normal faltar proposta.
5. **Confirmação de pagamento:** não precisa. Todo relatório é pago na data de previsão, sem nota fiscal nem recibo. O painel mostra "pago na previsão" (ou "cai em dd/mm").
6. **Comissão dos vendedores jan–out:** fica a média dos meses com vendedores registrados (novembro, 37,59% em Mogi), dizendo claramente que **não existe relatório** de comissão dos vendedores de jan–out. Só serve para o painel funcionar (informativo do ROI).
7. **Investimentos:** 100% lançados até hoje; novos gastos o usuário lança.
8. **Kolmeya:** o usuário manda o relatório de gastos à mão. **Não há cruzamento de telefones**: o sistema já sabe de onde veio o cliente.

**Dúvidas**
1. **Operacional de Mogi R$ 2.300,00:** correto (aluguel da sala, água, luz, internet). Consolação não tem. Como não vem no relatório, passa a somar **todo mês**, também quando a folha vem do relatório (antes só somava sem relatório).
2. **Salário:** vale o do relatório. Mês sem salário no relatório → **média dos últimos 3 relatórios** (em qualquer mês, não só depois do primeiro relatório). A estrutura informada (salários, VR, VT) só é usada se não houver nenhum relatório. Na aba Financeiro, o custo mensal mostra folha (relatório ou média) + operacional + outros custos do relatório.
3. **Custo:** vale o relatório. O alerta "soma das rubricas difere do custo mensal informado" saiu.
4. **Agenciamento fora do SisWeb:** conta. Todo agenciamento pago no relatório de propostas que não estão no SisWeb (vendas antigas, quase todas de 2025) entra no a receber do **mês do pagamento**, como "parcelas de vendas anteriores · fora do SisWeb", pelo valor bruto (como as parcelas do SisWeb). Em 2026 isso soma **R$ 215.025,09** (não só os R$ 56,50 da ADC, como foi dito antes).
5. **Grade:** Trasmontano PF, São Cristóvão (PF e PME) e MedSênior PME já estão na grade (PF = individual; PME = coletivo empresarial). Operadora sem vitalício informado = não tem vitalício.
6. **Encargos:** segue a estimativa (o relatório não mostra quem é CLT).
7. **Feriados:** tiram VR e VT. Dias úteis por unidade: nacionais + Sexta-feira Santa, estadual (9/7), Corpus Christi, Carnaval e o municipal de cada unidade (Consolação: 25/1 aniversário de São Paulo; Mogi: 1/9 aniversário de Mogi das Cruzes).
8. **Automação:** não. A atualização é manual (o relatório chega num sistema interno com senha).

**Efeito no ano de 2026 (jan–nov):** a receber R$ 934.356,82 → R$ 1.149.381,91 (+ agenciamento fora do SisWeb); custos R$ 942.971,42 → R$ 1.000.958,46 (+ operacional de Mogi e imposto sobre o a receber maior); lucro bruto −R$ 8.614,60 → R$ 148.423,45; lucro líquido −R$ 96.541,08 → R$ 60.496,97.

**Decisões complementares (26/11/2026):**
- Proposta do SisWeb sem comissão da Optas e operadora na grade → usa a grade (Select PME, Biovida PME). Select PME com 1 vida usa a faixa mais próxima da grade (2 a 29 vidas; o produto é "01 a 29 vidas"). "Biovida Saúde" = Biovida.
- Operadora fora da grade (Onmed ×2, Unimed Santos) → fica sem comissão e aparece como "sem comissão" (aviso informativo e linha com R$ 0,00 no detalhe do a receber).
- Feriados: o 25/1 (aniversário de São Paulo) vale nas duas unidades; Mogi tem também o 1/9. A padroeira de Mogi não é feriado.
- Linha do relatório com líquido R$ 0,00 (1ª parcela de adesão retida) não conta como recebida: 7 linhas, R$ 4.896,81 (R$ 3.518,06 em 2026).
- Provisão de 13º e férias vale todo mês, sobre os salários CLT informados (Consolação R$ 796,18 · Mogi R$ 826,97 · total R$ 1.623,15), mesmo nos meses com folha do relatório.

**Efeito final no ano de 2026 (jan–nov):** a receber R$ 1.160.386,49 (+ R$ 11.004,58 de Select e Biovida pela grade); a receber R$ 1.156.868,43 depois de tirar as linhas com líquido zero; custos R$ 1.019.936,08 (com a provisão de R$ 1.623,15 × 11); lucro bruto R$ 136.932,35; lucro líquido R$ 49.005,87.

**REGRA DO RELATÓRIO (26/11/2026, substitui as regras de mês devido, tipos de crédito/débito, AD, acerto e empréstimo):** no mês que tem relatório de pagamento vale só o relatório, pelo Líquido (última coluna): positivo = a receber, com "-" = custo, seja o que for. Mês de referência = previsão. Fora do relatório entram só o custo operacional de Mogi (R$ 2.300,00), a provisão (R$ 1.623,15) e o imposto (8,5% sobre o líquido das linhas com % Adm. 8,50%; 15% sobre o resto). Mês sem relatório entre dois relatórios (Consolação, outubro/2026) = lacuna: só operacional e provisão. Mês depois do último relatório (Mogi, novembro/2026) = estimativa até o relatório chegar.
- Exceções à regra (decididas pelo usuário em 26/11/2026): SMS no relatório (já é investimento), adiantamento devolvido (AD nª PARC / AD COMISSÃO), retiradas/vales da Joana, boleto do apartamento e aluguel pagos por fora não entram.
- Resultado 2026 (jan–nov): a receber R$ 842.505,20; custos R$ 878.847,74; lucro bruto −R$ 36.342,54; lucro líquido −R$ 124.269,02. Jan–out conferido mês a mês contra conta independente feita direto dos relatórios: bate ao centavo.

**Conferência linha a linha (26/11/2026):** PDF = CSV campo a campo nas 3.816 linhas e nos 231 créditos/débitos; a conta de cada linha (parcela × % = bruto; bruto − Desp. Adm. = líquido) bate em todas, menos nas 7 com líquido R$ 0,00 (não contam).
- Adiantamento devolvido (AD nª PARC / AD COMISSÃO): a Optas já recebeu antes; não é custo, a comissão conta pela linha (R$ 29.922,90 em 2026). O "10% sobre parcela" continua custo.
- "ACERTO FOLHA" (+R$ 33.342,54, Consolação, fev/2026): revisto em 26/11/2026 → entra no a receber (o débito da folha negativa de janeiro continua no custo).
- Resultado 2026 (jan–nov): a receber R$ 1.123.525,89; custos R$ 985.011,79; lucro bruto R$ 138.514,10; lucro líquido R$ 50.587,62.

**Levantamento dos relatórios (26/11/2026):** 23 relatórios (PDF = CSV ao centavo: 3.816 linhas, 231 créditos/débitos); toda linha e todo crédito/débito entra no painel. Faltam o relatório de Consolação com previsão em outubro/2026 e o de Mogi de novembro/2026.
