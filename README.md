# OPTAS · Painel gerencial inteligente

Painel financeiro, comercial e de ROI da Optas (unidades Consolação e Mogi), com a identidade visual do painel gerencial atual (logo OPTAS, laranja `#FF811B`, Montserrat + Inter).

As regras de negócio seguem o [documento-mestre](docs/DOCUMENTO-MESTRE.md). Princípio: **nenhum valor é inventado**. O que falta aparece como alerta ou pendência.

## O que o painel faz

| Aba | Conteúdo |
|---|---|
| **Visão geral** | Recomendação de investimento com justificativa, as 10 perguntas da gestão respondidas, comparação Consolação × Mogi |
| **Financeiro** | Lançamento das comissões efetivamente recebidas, fechamento do mês por unidade (impostos, comissões, custos, provisão, resultado operacional, LBO, reserva, resultado financeiro), cenário projetado, ponto de equilíbrio, estrutura de custos e provisões |
| **Comercial** | Produção e comissão por vendedor (faixas por unidade sobre toda a produção), quanto falta para a próxima faixa, produção por operadora, PF × PME, funil Hapvida |
| **ROI & investimentos** | Reserva de marketing, registro diário de investimento, média diária, projeção até o fechamento, teto diário, ROI projetado e realizado por campanha, importação de contratos linha a linha (CSV) |
| **Alertas** | Verificação de integridade: campo ausente, registros afetados, cálculo comprometido, correção. Botão para copiar o texto e enviar à equipe responsável |
| **Pendências** | As 7 pendências do documento-mestre, separadas das regras confirmadas |
| **Regras** | Tabelas vigentes: faixas dos vendedores, operadoras, imposto, reserva, vitalício e critérios do motor de recomendação |

## Estrutura

```
src/painel.html        código-fonte (HTML + CSS + JS, sem dependências)
assets/logo-optas.png  logo extraída do painel atual
data/snapshot.json     snapshot dos dados do painel gerencial (PipeRun + ASI)
build.py               gera index.html e apps-script/Index.html
index.html             painel pronto (abre direto no navegador)
apps-script/Code.gs    backend para publicar no Google Apps Script
apps-script/Index.html página usada pelo Apps Script
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

No Apps Script, os dados vêm de `tvDadosWeb` e são atualizados a cada 5 minutos. Investimentos, comissões recebidas e contratos importados ficam salvos nas propriedades do script, ou seja, são compartilhados entre quem usa o painel. Aberto localmente (`index.html`), o painel usa o snapshot e salva os lançamentos só no navegador.

## Limitação da integração atual

O painel gerencial entrega **totais por vendedor** (Projeto Hapvida / fora do projeto), não vendas individuais. Por isso:
- o agenciamento previsto só é calculado para a parte Hapvida, e fica marcado como **provisório** porque a modalidade PF/PME não foi informada;
- as vendas "fora do projeto" não têm operadora, então não entram no cálculo;
- nenhum contrato tem origem ou campanha, então o ROI não pode ser atribuído.

Até a integração enviar as vendas linha a linha (campos da seção 10), dá para importar um CSV na aba ROI. Cada contrato importado guarda a tabela de comissão vigente no momento da importação.
