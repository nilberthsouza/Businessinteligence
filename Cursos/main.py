import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#define size of graphics
fig = plt.figure(figsize=(20,6))

##define datafram column name and product dataframe columns
dados_names = ['Data','Valor','Vendedor','LinkImage','ID Produto','Quantidade']
dproduto_names = ['ID Produto','Produto','Tipo']

#loads datasets into memory, header arrow as null and assigns the names assigned in dados_names and dproduto_names
dados = pd.read_excel('Dados_Excel.xlsx',header=None,names=dados_names)
dproduto = pd.read_table('dProduto.txt',encoding="ISO-8859-1")


#delete first line of dataset
dados = dados.drop(0)

#removes unwanted characters from the seller column fields
dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('#$_',''))
dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('_##',''))

#relates products to data by ID
df_merged = pd.merge(dados,dproduto,on="ID Produto",how="right")


#sales number, counting occurrence of Product ID
print(len(dados['ID Produto']))

#number of sales per seller and build chart
plt.subplot2grid((3,3),(0,0))
dados['Vendedor'].value_counts(normalize=True).plot(kind="bar")
plt.title('Vendas por Vendedor')

#calculating revenue
dados['Valor venda'] = dados['Valor']*dados['Quantidade']


#card with total revenue value in the chart
Receita = "R$"+str(dados['Valor venda'].sum())
plt.subplot2grid((3,3),(0,1))
plt.text(0.0,0.1,Receita,size =43)
plt.title("Receita Total")


#chart that prints sales number by product
plt.subplot2grid((3,3),(0,2))
df_merged['Produto'].value_counts(normalize=True).plot(kind="bar")
plt.title("Numero de vendas por produto")

#Graph of total sales of product 1 by salesperson
plt.subplot2grid((3,3),(0,2))
df_merged.Vendedor[df_merged['ID Produto'] == 1].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 1 por Vendedor")


#Graph of total sales of product 2 by salesperson
plt.subplot2grid((3,3),(1,1))
df_merged.Vendedor[df_merged['ID Produto'] == 2].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 2 por Vendedor")

#Graph of total sales of product 3 by salesperson
plt.subplot2grid((3,3),(1,0))
df_merged.Vendedor[df_merged['ID Produto'] == 3].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 3 por Vendedor")

#Graph of total sales of Trovato
plt.subplot2grid((3,3),(1,2))
df_merged.Produto[df_merged['Vendedor'] == 'Trovato'].value_counts(normalize=True).plot(kind='bar')
plt.title("Produtos Vendidos por Trovato")

#show chart's in a window
plt.show()
