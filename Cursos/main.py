import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20,6))

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

print(df_merged.head())

#numero de vendas, contando ocorrencia de ID Produtos
print(len(dados['ID Produto']))

#numero de vendas por vendendor e contruir grafico
plt.subplot2grid((3,3),(0,0))
dados['Vendedor'].value_counts(normalize=True).plot(kind="bar")
plt.title('Vendas por Vendedor')

#calculando receita
dados['Valor venda'] = dados['Valor']*dados['Quantidade']

Receita = "R$"+str(dados['Valor venda'].sum())
plt.subplot2grid((3,3),(0,1))
plt.text(0.0,0.1,Receita,size =43)
plt.title("Receita Total")

plt.subplot2grid((3,3),(0,2))
df_merged['Produto'].value_counts(normalize=True).plot(kind="bar")
plt.title("Numero de vendas por produto")

plt.subplot2grid((3,3),(0,2))
df_merged.Vendedor[df_merged['ID Produto'] == 1].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 1 por Vendedor")


plt.subplot2grid((3,3),(1,1))
df_merged.Vendedor[df_merged['ID Produto'] == 2].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 2 por Vendedor")


plt.subplot2grid((3,3),(1,0))
df_merged.Vendedor[df_merged['ID Produto'] == 3].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 3 por Vendedor")

plt.subplot2grid((3,3),(1,2))
df_merged.Produto[df_merged['Vendedor'] == 'Trovato'].value_counts(normalize=True).plot(kind='bar')
plt.title("Produtos Vendidos por Trovato")

plt.show()
