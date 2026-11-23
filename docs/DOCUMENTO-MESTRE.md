# OPTAS — DOCUMENTO-MESTRE DE GESTÃO, FINANCEIRO, COMERCIAL E ROI

**Versão:** 1.6  
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

- Alíquota: 15%.
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

# 13. ESCOPO FORA DA PRIMEIRA ETAPA

Distribuição de lucros entre W3G e sócias; média de comissões para provisionamento da folha; controle individual de salários fixos; CPL e ROI avançado sem atribuição confiável; conciliação detalhada de cada pagamento das operadoras; controle avançado de estornos, cancelamentos, descontos e recebimentos parciais.

# 14. PENDÊNCIAS PARA FINALIZAR A MODELAGEM

1. **Tabelas das operadoras:** percentuais de MedSênior, Prevent, Santa Helena, Sobam, Supermed, Qualicorp, Ana Costa, São Cristóvão e Trasmontano (agenciamento, vitalício, PF/PME, diferenças por modalidade) e modalidade das sete já informadas.
2. **Vitalício:** início na 4ª parcela para todas? Base: valor original ou atualizado? Continuidade igual para todas as modalidades?
3. **Acúmulo da reserva de marketing:** acumula para o mês seguinte ou expira no fechamento?
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
