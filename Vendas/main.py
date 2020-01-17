import numpy as np
import pandas as pd

xls = pd.ExcelFile('Vendas.xlsx')
dfone = pd.read_excel(xls, 'Vendas')
dftwo = pd.read_excel(xls, 'Produtos')
dfthre = pd.read_excel(xls, 'Fabricante')
dffour = pd.read_excel(xls,'Canal')
dffive = pd.read_excel(xls,'Geografia_1')
dfsix = pd.read_excel(xls, 'Geografia_2')
dfseven = pd.read_excel(xls, 'Geografia_3')
dfeig = pd.read_excel(xls, 'Promocao')

col_names = ['Data','IndicedoMes','IndiceAcumuladonoAno','IndiceAcumUlt12','numeroindiceacumulado']

ipca = pd.read_csv('ipca.csv',header=None,names=col_names)

ipca = ipca.drop('IndiceAcumuladonoAno',axis=1)
ipca = ipca.drop('numeroindiceacumulado',axis=1)

ipca.Data = ipca.Data.map(lambda a: a.replace('/','-'))

month = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
i = 1

for i in range(len(month)+1):
    ipca.Data = ipca.Data.map(lambda mon: mon.replace(str(month[i-1]),str('1-'+str(i))))
    i+=1

ipca.Data = pd.to_datetime(ipca['Data'],format='%d-%m-%Y',errors='coerce')

def get_year(dt):
    return dt.year

ipca['Year'] = ipca['Data'].map(get_year)


ipca_rem = ipca.loc[(ipca['Year'] <2011) & (ipca['Year'] > 2013)]

ipca = ipca_rem.drop(ipca_rem.index)

print(ipca.head())














