import json, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter as L

OUT='/home/user/paineloptas/planilhas/OPTAS-dados-2026.xlsx'
F='Arial'
OR=PatternFill('solid',fgColor='FF811B'); YEL=PatternFill('solid',fgColor='FFF2A8'); GRAY=PatternFill('solid',fgColor='EEEEEE'); PEACH=PatternFill('solid',fgColor='FFE3CC'); EX=PatternFill('solid',fgColor='F4ECE4')
thin=Side(style='thin',color='E0D4C8'); BD=Border(left=thin,right=thin,top=thin,bottom=thin)
H=Font(name=F,bold=True,color='FFFFFF',size=10); T=Font(name=F,bold=True,size=14,color='A84A0A'); N=Font(name=F,size=10); B=Font(name=F,bold=True,size=10)
BLUE=Font(name=F,size=10,color='0000FF'); EXF=Font(name=F,size=10,italic=True,color='6E625A'); NOTE=Font(name=F,size=9,italic=True,color='6E625A')
BRL='"R$" #,##0.00;-"R$" #,##0.00;"-"'; PCT='0.0%;-0.0%;"-"'; DATE='DD/MM/YYYY'
MESES=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
snap=json.load(open('/home/user/paineloptas/data/snapshot.json'))

wb=Workbook()
def titulo(ws,t,sub):
    ws['A1']=t; ws['A1'].font=T
    ws['A2']=sub; ws['A2'].font=NOTE
    ws.sheet_view.showGridLines=False
def cab(ws,row,cols,widths):
    for i,(c,w) in enumerate(zip(cols,widths),1):
        x=ws.cell(row=row,column=i,value=c); x.font=H; x.fill=OR; x.alignment=Alignment(wrap_text=True,vertical='center'); x.border=BD
        ws.column_dimensions[L(i)].width=w
    ws.row_dimensions[row].height=32
def entrada(ws,r1,r2,c1,c2,fmt=None):
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            x=ws.cell(row=r,column=c); x.fill=YEL; x.border=BD; x.font=N
            if fmt and fmt.get(c): x.number_format=fmt[c]
def lista(ws,rng,opts,msg=None):
    dv=DataValidation(type='list',formula1='"'+','.join(opts)+'"',allow_blank=True)
    if msg: dv.prompt=msg; dv.showInputMessage=True
    ws.add_data_validation(dv); dv.add(rng)

# ---------- 1. Como preencher
ws=wb.active; ws.title='Como preencher'
titulo(ws,'OPTAS · Dados para o painel 2026','Preencha e devolva este arquivo. O painel usa estes dados para calcular o ano de 2026 com valores reais.')
linhas=[('LEGENDA',''),
 ('Célula amarela','Você preenche.'),('Texto azul','Valor que já recebi de você, preenchido por mim. Corrija se estiver errado.'),('Linha bege em itálico','Exemplo de preenchimento. Pode apagar ou deixar (não entra nos cálculos).'),('Célula branca/cinza','Fórmula ou referência. Não precisa mexer.'),
 ('',''),('ABAS','O que preencher'),
 ('1. Vendas 2026','Uma linha por venda de jan a dez/2026: data, unidade, vendedor, se é do Projeto Hapvida, operadora, modalidade, valor mensal, situação. É a base de tudo.'),
 ('2. Operadoras','Comissão de cada operadora por modalidade (PF/PME) e a comissão do Projeto Hapvida.'),
 ('3. Custos mensais','Custos reais de cada mês por unidade. Se o VR/VT do mês ficar em branco, o painel calcula pelos dias úteis (base outubro).'),
 ('4. Equipe','Vendedores e sócias, com entrada e saída, para saber quantas pessoas havia em cada mês.'),
 ('5. Feriados e recessos','Diga em quais dias a Optas NÃO trabalha (reduz VR/VT). Feriados nacionais já estão listados.'),
 ('6. Investimentos mkt','Cada investimento em marketing: data, campanha e valor.'),
 ('7. Carteira ativa','Todos os contratos rodando (de qualquer ano), para calcular o vitalício.'),
 ('8. Vitalício recebido','Quanto de vitalício entrou por operadora em cada mês (dos relatórios).'),
 ('9. Decisões','Respostas rápidas para regras que ainda estão em aberto.'),
 ('10. Resumo (automático)','Confere o que foi preenchido mês a mês e mostra o que falta. Não precisa editar.'),
 ('',''),('IMPORTANTE','Só contratos efetivos contam no painel (Em contrato ou Implantado). Valores em reais, sem fórmulas. Datas no formato dd/mm/aaaa.')]
for i,(a,b) in enumerate(linhas,4):
    ws.cell(row=i,column=1,value=a).font=B if a.isupper() or a.startswith(('1','2','3','4','5','6','7','8','9')) else N
    ws.cell(row=i,column=2,value=b).font=N
    ws.cell(row=i,column=2).alignment=Alignment(wrap_text=True,vertical='top')
ws['A5'].fill=YEL; ws['A6'].font=BLUE; ws['A7'].fill=EX; ws['A7'].font=EXF; ws['A8'].fill=GRAY
ws.column_dimensions['A'].width=26; ws.column_dimensions['B'].width=110

# ---------- 2. Vendas
ws=wb.create_sheet('Vendas 2026')
titulo(ws,'Vendas 2026','Uma linha por venda. Linha 4 é exemplo. Preencha a partir da linha 5. "Mês" é calculado sozinho.')
cols=['Data da venda','Unidade','Vendedor(a)','Projeto Hapvida?','Operadora','Modalidade','Valor mensal do plano (R$)','Situação','Nº contrato / proposta','Campanha / origem','Observações','Mês (auto)','Cliente (titular PF / empresa PME)','CPF (PF) / CNPJ (PME)','Vidas']
cab(ws,3,cols,[14,13,20,12,18,11,16,14,18,22,26,9,30,20,8])
ex=[dt.date(2026,1,15),'Mogi','Wanderleia G.','Não','Bradesco','PME',1800.00,'Implantado','PRP-000123','Meta Ads Bradesco PME','Exemplo — pode apagar']
for c,v in {13:'Empresa Exemplo Ltda',14:'11.222.333/0001-81',15:6}.items():
    x=ws.cell(row=4,column=c,value=v); x.font=EXF; x.fill=EX; x.border=BD
for c,v in enumerate(ex,1):
    x=ws.cell(row=4,column=c,value=v); x.font=EXF; x.fill=EX; x.border=BD
ws['A4'].number_format=DATE; ws['G4'].number_format=BRL
NV=2000; R1,R2=5,5+NV-1
entrada(ws,R1,R2,1,11,{1:DATE,7:BRL})
entrada(ws,R1,R2,13,15)
for r in range(4,R2+1):
    x=ws.cell(row=r,column=12,value=f'=IF(A{r}="","",MONTH(A{r}))'); x.font=N; x.fill=GRAY; x.border=BD; x.alignment=Alignment(horizontal='center')
oper=['Hapvida','Bradesco','Amil','SulAmérica','Seguros Unimed','Porto','Alice','MedSênior','Prevent','Santa Helena','Sobam','Supermed','Qualicorp','Ana Costa','São Cristóvão','Trasmontano']
lista(ws,f'B{R1}:B{R2}',['Consolação','Mogi'])
lista(ws,f'D{R1}:D{R2}',['Sim','Não'],'Sim = venda do Projeto Hapvida (comissão própria)')
lista(ws,f'E{R1}:E{R2}',oper)
lista(ws,f'F{R1}:F{R2}',['PF','PME'])
lista(ws,f'H{R1}:H{R2}',['Em contrato','Implantado','Em andamento','Cancelado'],'Só Em contrato e Implantado contam no painel')
dvd=DataValidation(type='date',operator='between',formula1='DATE(2026,1,1)',formula2='DATE(2026,12,31)',allow_blank=True); dvd.error='Use uma data de 2026'; ws.add_data_validation(dvd); dvd.add(f'A{R1}:A{R2}')
dvn=DataValidation(type='decimal',operator='greaterThan',formula1='0',allow_blank=True); ws.add_data_validation(dvn); dvn.add(f'G{R1}:G{R2}')
ws.freeze_panes='A5'

# ---------- 3. Operadoras
ws=wb.create_sheet('Operadoras')
titulo(ws,'Comissões das operadoras','Percentuais como 350% = 3,5 vezes a mensalidade. Azul = o que você já me passou (sem modalidade). Amarelo = falta preencher.')
cols=['Operadora','Informado (sem modalidade) · Agenciamento','Informado · Vitalício','Tem PF?','Agenciamento PF','Vitalício PF','Tem PME?','Agenciamento PME','Vitalício PME','Vitalício começa na parcela','Observações']
cab(ws,3,cols,[20,18,13,9,14,12,9,14,12,14,30])
conhecido={'Bradesco':(4,.04),'Amil':(3,.02),'SulAmérica':(3,.02),'Seguros Unimed':(3,.02),'Porto':(3,.02),'Alice':(3,.02),'Santa Helena':(3,.02),'Sobam':(3,.02),'Ana Costa':(3,.02),'Supermed':(.30,None),'Qualicorp':(.50,None)}
rows=[('Projeto Hapvida',None,None)]+[(o+(' (fora do projeto)' if o=='Hapvida' else ''),)+conhecido.get(o,(None,None)) for o in oper]
for i,rw in enumerate(rows,4):
    ws.cell(row=i,column=1,value=rw[0]).font=B; ws.cell(row=i,column=1).border=BD
    for c,v in ((2,rw[1]),(3,rw[2])):
        x=ws.cell(row=i,column=c,value=v); x.border=BD; x.number_format=PCT
        if v is not None: x.font=BLUE; x.fill=PatternFill(None)
        else: x.fill=GRAY
    entrada(ws,i,i,4,11,{5:PCT,6:PCT,8:PCT,9:PCT})
ws.cell(row=4,column=11,value='Comissão própria, inferior à Hapvida comum').font=N
# Valores por modalidade informados em 24/11/2026 (azul)
porMod={'Hapvida (fora do projeto)':{'H':3.5,'I':.02,'G':'Sim','K':'PME confirmado; PF a confirmar'},
 'MedSênior':{'D':'Sim','E':2,'F':.02,'K':'PF confirmado; PME a confirmar'},
 'Prevent':{'D':'Sim','E':2,'G':'Não','K':'Só PF; vitalício a confirmar'},
 'Trasmontano':{'G':'Sim','H':3,'I':.05,'K':'PME confirmado; PF a confirmar'},
 'Supermed':{'K':'130% − 100% taxa de angariação = 30% efetivo; vitalício a confirmar'},
 'Qualicorp':{'K':'150% − 100% taxa de angariação = 50% efetivo; vitalício a confirmar'},
 'São Cristóvão':{'K':'Tudo a confirmar'}}
for rr in range(4,4+len(rows)):
    nm=ws.cell(row=rr,column=1).value
    for col,val in porMod.get(nm,{}).items():
        x=ws[f'{col}{rr}']; x.value=val; x.font=BLUE
ws['B5'].comment=Comment('Valor informado por você no documento-mestre (v1.0, 23/11/2026).','Painel OPTAS')
n=len(rows)+3
lista(ws,f'D4:D{n}',['Sim','Não']); lista(ws,f'G4:G{n}',['Sim','Não'])
ws.cell(row=n+2,column=1,value='Exemplo: Bradesco · Tem PF? Sim · Agenciamento PF 400% · Vitalício PF 4% · Tem PME? Sim · Agenciamento PME 300% · Vitalício PME 2% · começa na 4ª parcela.').font=NOTE
ws.freeze_panes='B4'

# ---------- 4. Custos mensais
ws=wb.create_sheet('Custos mensais')
titulo(ws,'Custos mensais 2026 por unidade','Valores pagos em cada mês. Outubro já preenchido com o que você me passou. VR/VT em branco = o painel calcula pelos dias úteis.')
grp=['Salários brutos (CLT + PJ)','dos quais PJ sócia','VR pago','VT pago','Custos operacionais','Outros custos','Nº de CLT','Total (auto)']
ws.cell(row=3,column=1,value='').fill=OR
ws.merge_cells('B3:I3'); ws['B3']='CONSOLAÇÃO'; ws.merge_cells('J3:Q3'); ws['J3']='MOGI'
for c in ('B3','J3'): ws[c].font=H; ws[c].fill=OR; ws[c].alignment=Alignment(horizontal='center')
ws['R3']='OPTAS'; ws['R3'].font=H; ws['R3'].fill=OR
cab(ws,4,['Mês']+grp+grp+['Total geral (auto)'],[12]+[14]*16+[16])
base={'Consolação':[15315.76,10000,4140.40,1576.24,0,0,5],'Mogi':[10521.33,5000,3640.40,1691.30,2300,0,4]}
for m in range(12):
    r=5+m; ws.cell(row=r,column=1,value=MESES[m]).font=B; ws.cell(row=r,column=1).border=BD
    for k,(u,c0) in enumerate((('Consolação',2),('Mogi',10))):
        entrada(ws,r,r,c0,c0+6,{c0+i:BRL for i in range(6)})
        if m==9:
            for i,v in enumerate(base[u]):
                x=ws.cell(row=r,column=c0+i,value=v); x.font=BLUE
        cl=L(c0); tot=ws.cell(row=r,column=c0+7,value=f'=IF(COUNT({cl}{r}:{L(c0+5)}{r})=0,"",{cl}{r}+{L(c0+2)}{r}+{L(c0+3)}{r}+{L(c0+4)}{r}+{L(c0+5)}{r})')
        tot.number_format=BRL; tot.fill=GRAY; tot.font=B; tot.border=BD
    g=ws.cell(row=r,column=18,value=f'=IF(AND(I{r}="",Q{r}=""),"",N(I{r})+N(Q{r}))'); g.number_format=BRL; g.fill=GRAY; g.font=B; g.border=BD
ws['B14'].comment=Comment('Outubro/2026: valores informados por você (documento-mestre, seção 3). Total = R$ 39.185,43. PJ já está dentro dos salários brutos.','Painel OPTAS')
ws.cell(row=18,column=1,value='"dos quais PJ sócia" é só informativo: já está dentro dos salários brutos e não é somado de novo no total.').font=NOTE
ws.cell(row=19,column=1,value='Outubro (azul) bate com o custo informado de R$ 39.185,43. Se algum mês teve custo diferente (aumento, contratação, desligamento), preencha o valor real.').font=NOTE
ws.freeze_panes='B5'

# ---------- 5. Equipe
ws=wb.create_sheet('Equipe')
titulo(ws,'Equipe 2026','Quem trabalhou em cada unidade. Nomes em azul vêm do painel atual. Preencha admissão e saída (se saiu em 2026).')
cab(ws,3,['Nome','Unidade','Vínculo','Função','Admissão','Saída (se saiu)','Observações'],[22,13,10,14,13,15,30])
r=4
for v in snap['vendedores']:
    for c,val in enumerate([v['nome'],v['equipe'],'CLT','Vendedor(a)'],1):
        x=ws.cell(row=r,column=c,value=val); x.font=BLUE; x.border=BD
    entrada(ws,r,r,5,7,{5:DATE,6:DATE}); r+=1
for u in ('Consolação','Mogi'):
    for c,val in enumerate(['Sócia '+u,u,'PJ','Sócia'],1):
        x=ws.cell(row=r,column=c,value=val); x.font=BLUE; x.border=BD
    entrada(ws,r,r,5,7,{5:DATE,6:DATE}); r+=1
entrada(ws,r,r+11,1,7,{5:DATE,6:DATE})
lista(ws,f'B4:B{r+11}',['Consolação','Mogi']); lista(ws,f'C4:C{r+11}',['CLT','PJ'])
ws.cell(row=r+13,column=1,value='Use as linhas amarelas vazias para quem entrou ou saiu ao longo de 2026.').font=NOTE

# ---------- 6. Feriados
ws=wb.create_sheet('Feriados e recessos')
titulo(ws,'Feriados e recessos 2026','Cinza = feriado nacional (já considerado). Amarelo = diga se a Optas trabalha. Acrescente recessos e pontes nas linhas vazias.')
cab(ws,3,['Data','Dia da semana','Descrição','Tipo','Vale para','A Optas trabalha?'],[13,14,34,18,13,16])
nac=[(dt.date(2026,1,1),'Confraternização Universal'),(dt.date(2026,4,3),'Sexta-feira Santa'),(dt.date(2026,4,21),'Tiradentes'),(dt.date(2026,5,1),'Dia do Trabalho'),(dt.date(2026,9,7),'Independência'),(dt.date(2026,10,12),'Nossa Senhora Aparecida'),(dt.date(2026,11,2),'Finados'),(dt.date(2026,11,15),'Proclamação da República'),(dt.date(2026,11,20),'Consciência Negra'),(dt.date(2026,12,25),'Natal')]
conf=[(dt.date(2026,1,25),'Aniversário de São Paulo','Municipal (a confirmar)','Consolação'),(dt.date(2026,2,16),'Carnaval (segunda)','Ponto facultativo','Ambas'),(dt.date(2026,2,17),'Carnaval (terça)','Ponto facultativo','Ambas'),(dt.date(2026,2,18),'Quarta-feira de Cinzas (manhã)','Ponto facultativo','Ambas'),(dt.date(2026,6,4),'Corpus Christi','Municipal / facultativo (a confirmar)','Ambas'),(dt.date(2026,9,1),'Aniversário de Mogi das Cruzes','Municipal (a confirmar)','Mogi'),(dt.date(2026,12,24),'Véspera de Natal','Recesso? (a confirmar)','Ambas'),(dt.date(2026,12,31),'Véspera de Ano Novo','Recesso? (a confirmar)','Ambas')]
r=4
for d,desc in nac:
    for c,val in enumerate([d,f'='+'CHOOSE(WEEKDAY(A{r}),"domingo","segunda","terça","quarta","quinta","sexta","sábado")'.replace('{r}',str(r)),desc,'Nacional','Ambas','Não'],1):
        x=ws.cell(row=r,column=c,value=val); x.fill=GRAY; x.font=N; x.border=BD
    ws.cell(row=r,column=1).number_format=DATE; r+=1
for d,desc,tipo,u in conf:
    for c,val in enumerate([d,f'='+'CHOOSE(WEEKDAY(A{r}),"domingo","segunda","terça","quarta","quinta","sexta","sábado")'.replace('{r}',str(r)),desc,tipo,u],1):
        x=ws.cell(row=r,column=c,value=val); x.font=N; x.border=BD
    ws.cell(row=r,column=1).number_format=DATE
    entrada(ws,r,r,6,6); r+=1
for k in range(15):
    entrada(ws,r,r,1,6,{1:DATE}); ws.cell(row=r,column=2,value=f'=IF(A{r}="","",'+'CHOOSE(WEEKDAY(A{r}),"domingo","segunda","terça","quarta","quinta","sexta","sábado")'.replace('{r}',str(r))+')').fill=GRAY; r+=1
lista(ws,f'E4:E{r}',['Ambas','Consolação','Mogi']); lista(ws,f'F4:F{r}',['Não','Sim','Meio período'],'Não = sem expediente (não paga VR/VT nesse dia)')
ws.cell(row=r+1,column=1,value='Exemplo de recesso: 28/12/2026 · Recesso de fim de ano · Recesso · Ambas · Não.').font=NOTE

# ---------- 7. Investimentos
ws=wb.create_sheet('Investimentos mkt')
titulo(ws,'Investimentos em marketing 2026','Uma linha por investimento: data, nome da campanha e valor. Linha 4 é exemplo.')
cab(ws,3,['Data','Campanha','Valor (R$)','Unidade (opcional)','Observações','Mês (auto)'],[13,30,14,16,30,9])
for c,v in enumerate([dt.date(2026,1,10),'Meta Ads Hapvida PME',1500.00,'Ambas','Exemplo — pode apagar'],1):
    x=ws.cell(row=4,column=c,value=v); x.font=EXF; x.fill=EX; x.border=BD
ws['A4'].number_format=DATE; ws['C4'].number_format=BRL
entrada(ws,5,504,1,5,{1:DATE,3:BRL})
for r in range(4,505):
    x=ws.cell(row=r,column=6,value=f'=IF(A{r}="","",MONTH(A{r}))'); x.fill=GRAY; x.font=N; x.border=BD
lista(ws,'D5:D504',['Ambas','Consolação','Mogi'])
ws.freeze_panes='A5'

# ---------- Carteira ativa
ws=wb.create_sheet('Carteira ativa')
titulo(ws,'Carteira ativa (para o vitalício)','Todos os contratos que ainda estão rodando, de qualquer ano. Linha 4 é exemplo. O vitalício começa na 4ª parcela.')
cab(ws,3,['Nº contrato','Operadora','Modalidade','Projeto Hapvida?','Valor mensal atual (R$)','Data de início','Unidade','Vendedor(a)','Situação','Cancelado em','Observações'],[16,18,11,12,16,13,13,20,12,13,26])
for c,v in enumerate(['CT-004512','Bradesco','PME','Não',1850.00,dt.date(2025,3,10),'Mogi','Wanderleia G.','Ativo',None,'Exemplo — pode apagar'],1):
    x=ws.cell(row=4,column=c,value=v); x.font=EXF; x.fill=EX; x.border=BD
ws['E4'].number_format=BRL; ws['F4'].number_format=DATE
entrada(ws,5,3004,1,11,{5:BRL,6:DATE,10:DATE})
lista(ws,'B5:B3004',oper); lista(ws,'C5:C3004',['PF','PME']); lista(ws,'D5:D3004',['Sim','Não']); lista(ws,'G5:G3004',['Consolação','Mogi']); lista(ws,'I5:I3004',['Ativo','Cancelado'])
ws.freeze_panes='A5'

# ---------- Vitalício recebido
ws=wb.create_sheet('Vitalício recebido')
titulo(ws,'Vitalício recebido','Valores de vitalício que entraram, conforme os relatórios das operadoras. Uma linha por operadora por mês. Linha 4 é exemplo.')
cab(ws,3,['Mês de referência','Operadora','Unidade (opcional)','Valor recebido (R$)','Nº de contratos no relatório','Observações'],[16,18,16,16,16,30])
for c,v in enumerate([dt.date(2026,10,1),'Bradesco','Mogi',556.32,6,'Exemplo — pode apagar'],1):
    x=ws.cell(row=4,column=c,value=v); x.font=EXF; x.fill=EX; x.border=BD
ws['A4'].number_format='MM/YYYY'; ws['D4'].number_format=BRL
entrada(ws,5,604,1,6,{1:'MM/YYYY',4:BRL})
lista(ws,'B5:B604',oper); lista(ws,'C5:C604',['Ambas','Consolação','Mogi'])
ws.freeze_panes='A5'

# ---------- 8. Decisões
ws=wb.create_sheet('Decisões')
titulo(ws,'Decisões em aberto','Escolha a resposta na lista. Se precisar explicar, use a coluna de observação.')
cab(ws,3,['#','Pergunta','Resposta','Observação'],[5,70,26,40])
qs=[('A verba de marketing (15% da produção) não usada no mês passa para o mês seguinte?',['Acumula para o mês seguinte','Zera no fechamento do mês']),
    ('O vitalício começa na 4ª parcela para todas as operadoras e modalidades?',['Sim, todas','Não (detalhar na aba Operadoras)']),
    ('Base do vitalício: valor original do plano ou valor atualizado (reajustes)?',['Valor original','Valor atualizado']),
    ('O vitalício é pago enquanto o contrato estiver ativo, em todas as modalidades?',['Sim','Não (detalhar)']),
    ('Os encargos estimados (34,8%) na provisão de 13º/férias foram validados pela contabilidade?',['Sim, estão corretos','Não, ver observação']),
    ('Sócias recebem VR/VT? (hoje o painel divide VR/VT só pelos CLT)',['Não','Sim'])]
for i,(q,op) in enumerate(qs,4):
    ws.cell(row=i,column=1,value=i-3).font=B; ws.cell(row=i,column=2,value=q).font=N; ws.cell(row=i,column=2).alignment=Alignment(wrap_text=True)
    for c in (1,2): ws.cell(row=i,column=c).border=BD
    entrada(ws,i,i,3,4); lista(ws,f'C{i}',op); ws.row_dimensions[i].height=30

# ---------- 9. Resumo
ws=wb.create_sheet('Resumo (automático)')
titulo(ws,'Resumo do preenchimento 2026','Calculado a partir das outras abas. Só contratos Em contrato ou Implantado entram na produção.')
cols=['Mês','Produção Consolação','Produção Mogi','Produção total','Vendas efetivas','Vendas do Projeto Hapvida','Vendas sem operadora','Vendas sem modalidade','Investido em mkt','Custo informado (sem provisão)','Situação']
cab(ws,3,cols,[12,17,15,15,11,13,12,12,15,17,30])
V="'Vendas 2026'"; I="'Investimentos mkt'"; C="'Custos mensais'"
rng=lambda col:f"{V}!${col}$5:${col}${R2}"
for m in range(12):
    r=4+m; mm=m+1
    ws.cell(row=r,column=1,value=MESES[m]).font=B
    efet=lambda extra='': f'SUMIFS({rng("G")},{rng("L")},{mm},{rng("H")},"Em contrato"{extra})+SUMIFS({rng("G")},{rng("L")},{mm},{rng("H")},"Implantado"{extra})'
    cnt=lambda extra='': f'COUNTIFS({rng("L")},{mm},{rng("H")},"Em contrato"{extra})+COUNTIFS({rng("L")},{mm},{rng("H")},"Implantado"{extra})'
    f={2:'='+efet(f',{rng("B")},"Consolação"'),3:'='+efet(f',{rng("B")},"Mogi"'),4:f'=B{r}+C{r}',5:'='+cnt(),6:'='+cnt(f',{rng("D")},"Sim"'),
       7:'='+cnt(f',{rng("E")},""'),8:'='+cnt(f',{rng("F")},""'),9:f"=SUMIFS({I}!$C$5:$C$504,{I}!$F$5:$F$504,{mm})",10:f"=IF({C}!R{5+m}=\"\",0,{C}!R{5+m})",
       11:f'=IF(E{r}=0,"Sem vendas lançadas",IF(G{r}+H{r}>0,"Faltam operadora/modalidade em "&(G{r}+H{r})&" campo(s)",IF(J{r}=0,"Falta custo do mês","Completo")))'}
    for c,v in f.items():
        x=ws.cell(row=r,column=c,value=v); x.font=N; x.border=BD
        if c in (2,3,4,9,10): x.number_format=BRL
        else: x.number_format='0;-0;"-"'
    ws.cell(row=r,column=1).border=BD
r=16; ws.cell(row=r,column=1,value='Total 2026').font=B
for c in range(2,11):
    x=ws.cell(row=r,column=c,value=f'=SUM({L(c)}4:{L(c)}15)'); x.font=B; x.fill=PEACH; x.border=BD
    x.number_format=BRL if c in (2,3,4,9,10) else '0;-0;"-"'
ws.cell(row=r,column=1).fill=PEACH; ws.cell(row=r,column=11).fill=PEACH
ws.cell(row=18,column=1,value='Linha de exemplo (linha 4 das abas Vendas e Investimentos) não entra no resumo.').font=NOTE
ws.freeze_panes='B4'

for s in wb.worksheets:
    for row in s.iter_rows():
        for c in row:
            if c.font and c.font.name!=F: c.font=Font(name=F,size=c.font.size or 10,bold=c.font.bold,italic=c.font.italic,color=c.font.color)
wb.save(OUT); print('ok')
