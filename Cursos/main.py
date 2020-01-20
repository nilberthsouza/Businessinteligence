import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#define tamanho dos graficos
fig = plt.figure(figsize=(20,6))

#define nome das colunas do datafram dados e do dataframe dprodutos
dados_names = ['Data','Valor','Vendedor','LinkImage','ID Produto','Quantidade']
dproduto = ['ID Produto','Produto','Tipo']

#carrega datasets pra memoria, seta cabeçario como nulo e atribui os nomes definidos na coluna 11 
dados = pd.read_excel('Dados_Excel.xlsx',header=None,names=dados_names)
dproduto = pd.read_table('dProduto.txt',encoding="ISO-8859-1")


#deleta primeira linha do dataset
dados = dados.drop(0)

#retira caracteres indesejados dos campos da coluna vendedor
dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('#$_',''))
dados['Vendedor']= dados['Vendedor'].map(lambda a: a.replace('_##',''))

#relaciona dprodutos com dados pelo ID
df_merged = pd.merge(dados,dproduto,on="ID Produto",how="right")


#numero de vendas, contando ocorrencia de ID Produtos
print(len(dados['ID Produto']))

#numero de vendas por vendendor e contruir grafico
plt.subplot2grid((3,3),(0,0))
dados['Vendedor'].value_counts(normalize=True).plot(kind="bar")
plt.title('Vendas por Vendedor')

#calculando receita
dados['Valor venda'] = dados['Valor']*dados['Quantidade']


#card com valor total da receita no grafico
Receita = "R$"+str(dados['Valor venda'].sum())
plt.subplot2grid((3,3),(0,1))
plt.text(0.0,0.1,Receita,size =43)
plt.title("Receita Total")


#grafico que imprime numero de vendas por produto
plt.subplot2grid((3,3),(0,2))
df_merged['Produto'].value_counts(normalize=True).plot(kind="bar")
plt.title("Numero de vendas por produto")

#Grafico de total de vendas do produto 1 por vendedor
plt.subplot2grid((3,3),(0,2))
df_merged.Vendedor[df_merged['ID Produto'] == 1].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 1 por Vendedor")


#Grafico de total de vendas do produto 2 por vendedor
plt.subplot2grid((3,3),(1,1))
df_merged.Vendedor[df_merged['ID Produto'] == 2].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 2 por Vendedor")

#Grafico de total de vendas do produto 3 por vendedor
plt.subplot2grid((3,3),(1,0))
df_merged.Vendedor[df_merged['ID Produto'] == 3].value_counts(normalize=True).plot(kind='bar')
plt.title("Produto 3 por Vendedor")

#Grafico de total de vendas do Trovato
plt.subplot2grid((3,3),(1,2))
df_merged.Produto[df_merged['Vendedor'] == 'Trovato'].value_counts(normalize=True).plot(kind='bar')
plt.title("Produtos Vendidos por Trovato")

#imprime grafico em uma janela
plt.show()
