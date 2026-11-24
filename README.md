# OPTAS · Painel gerencial inteligente

Painel financeiro, comercial e de ROI da Optas (unidades Consolação e Mogi), com a identidade visual do painel gerencial atual (logo OPTAS, laranja `#FF811B`, Montserrat + Inter).

As regras de negócio seguem o [documento-mestre](docs/DOCUMENTO-MESTRE.md). Princípio: **nenhum valor é inventado**. O que falta aparece como alerta ou pendência.

## O que o painel faz

| Aba | Conteúdo |
|---|---|
| **Visão geral** | Lucro ou prejuízo consolidado, mínimo para não fechar no vermelho e mínimo sustentável, resultado de cada unidade, indicadores do mês e comparativo |
| **Consolação / Mogi** | Lucro ou prejuízo da unidade, mínimos, demonstrativo, custos e vendedores |
| **Ano** | Memória de cada mês, sustentação no ano, provisão de 13º/férias, resultado mês a mês, fechamento do mês e do ano, balanço anual para imprimir/PDF |
| **Financeiro** | Fechamento do mês por unidade (impostos, comissões, custos, provisão, resultado operacional, lucro bruto operacional, reserva, resultado financeiro), ponto de equilíbrio, estrutura de custos e provisões |
| **Comercial** | Produção e comissão por vendedor (faixas por unidade sobre toda a produção), quanto falta para a próxima faixa, produção por operadora, PF × PME, funil Hapvida |
| **ROI & investimentos** | Registro de investimentos (campanha, valor e data em texto livre), linha do tempo, investimento × limite de 15% da produção (dentro / passou), ROI sobre as vendas |
| **Alertas** | Verificação de integridade: campo ausente, registros afetados, cálculo comprometido, correção. Botão para copiar o texto e enviar à equipe responsável |
| **Vitalício** | Vitalício previsto da carteira × recebido, por operadora e mês a mês |
| **Pendências** | As 7 pendências do documento-mestre, separadas das regras confirmadas |
| **Regras** | Tabelas vigentes e todas as fórmulas do sistema |

## Estrutura

```
src/painel.html        código-fonte (HTML + CSS + JS, sem dependências)
assets/logo-optas.png  logo extraída do painel atual
data/snapshot.json     snapshot dos dados do painel gerencial (PipeRun + ASI)
build.py               gera index.html e apps-script/Index.html
index.html             painel em modo real para revisão (com Pendências e Regras)
preview.html           painel em modo exemplo (dados fictícios identificados)
apps-script/Code.gs    backend para publicar no Google Apps Script
apps-script/Index.html versão publicada (sem Pendências e Regras)
testes/                auditoria dos cálculos em centavos
planilhas/             planilha de coleta de dados de 2026
docs/DOCUMENTO-MESTRE.md regras de negócio v1.0
```

Depois de alterar `src/painel.html` ou o snapshot:

```bash
python3 build.py
```

## Publicar no Apps Script (dados ao vivo)

1. No **mesmo projeto** do painel TV atual (onde está `tvDadosWeb`), adicione `apps-script/Code.gs` (com outro nome se já houver um `Code.gs`) e `apps-script/Index.html`.
2. Em *Configurações do projeto → Propriedades do script*, crie:
   - `OPTAS_KEY`: chave de acesso exigida na URL.
   - `OPTAS_TV_KEY`: a chave usada hoje em `tvDadosWeb('gerencial', …)`.
3. Faça uma nova implantação como *App da Web* e acesse `…/exec?k=<OPTAS_KEY>`.

No Apps Script, os dados vêm de `tvDadosWeb` e são atualizados a cada 5 minutos. Investimentos e o histórico dos meses ficam salvos nas propriedades do script, ou seja, são compartilhados entre quem usa o painel. Aberto localmente (`index.html`), o painel usa o snapshot e salva os lançamentos só no navegador.

## Limitação da integração atual

O painel considera apenas contratos efetivos (em contrato + implantado); a base de tudo é o valor a receber das operadoras. Não há projeções nem recomendações.

O painel gerencial entrega **totais por vendedor** (Projeto Hapvida / fora do projeto), não vendas individuais. Por isso:
- a produção do Projeto Hapvida aguarda a regra de comissão do projeto para entrar no agenciamento a receber;
- as vendas "fora do projeto" não têm operadora, então não entram no cálculo;
- nenhum contrato tem origem ou campanha, então o ROI não pode ser atribuído.

Quando a integração enviar as vendas linha a linha (campos da seção 10), cada contrato guarda a tabela de comissão vigente na data da venda.
