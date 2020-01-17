import pandas as pd
import numpy as np



dados_names = ['Data','Valor','Vendedor','LinkImage','ID Produto','Quantidade']
dproduto = ['ID Produto','Produto','Tipo']

dados = pd.read_excel('Dados_Excel.xlsx',header=None,names=dados_names)
dproduto = pd.read_table('dProduto.txt',encoding="ISO-8859-1")

dados = dados.drop(0)

#we dont need the column link, so we gonna just delete 

#dados = dados.drop('Link',axis=1)

dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('#$_',''))
dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('_##',''))

#dproduto['ID Produto'] = dproduto['ID Produto'].apply(str)


#print(type(dproduto['ID Produto'][2]))


df_merged = pd.merge(dados,dproduto,on="ID Produto",how="right")
print(dados.head())
print(dproduto.head())
print(df_merged.head())
