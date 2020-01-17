import sqlite3

class Database:
    def __init__(self,db):
        //todo: colocar tipos em variaveis do db
        self.conn = sqlite3.connect(db)
        self.cur  = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS vendas (id_venda, valor_do_desconto, quantidade_vendida,valor_do_retorno,Quantidadade_de_devolução, total_venda, custo_unitario, preco_unitario,data,id_canal,id_historico,id_produto,id_promocao)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS historicos(id_historico, id_geografia,nome_da_loja,status,tipo_venda,quantidade_de_funcionarios)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS produtos(id_produto,nome_produto,grupo)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS fabricantes(id_produto,nome_produto,fabricante)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS canais(id_canal,descricao)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS geografias(id_geografia,continente,pais)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS promocao(id_promocao, descricao_promocao,percentual)")

    def fetchVendas(self):
        self.cur.execute("SELECT * FROM vendas")
        rows = self.cur.fetchall()
        return rows
    
    def fetchHistoricos(self):
        self.cur.execute("SELECT * FROM historicos")
        rows = self.cur.fetchall()
        return rows
    
    def fetchProdutos(self):
        self.cur.execute("SELECT * FROM produtos")
        rows = self.cur.fetchall()
        return rows

    def fetchFabricantes(self):
        self.cur.execute("SELECT * FROM fabricantes")
        rows = self.cur.fetchall()
        return rows

    def fetchCanais(self):
        self.cur.execute("SELECT * FROM canais")
        rows = self.cur.fetchall()
        return rows

    def fetchGeografias(self):
        self.cur.execute("SELECT * FROM geografias")
        rows = self.cur.fechall()
        return rows

    def fetchPromocao(self):
        self.cur.execute("SELECT * FROM promocao")
        rows = self.cur.fetchall()
        return rows
    
    def inserVendas (self):
        self.cur.execute('INSERT
    def __del__(self):
        self.conn.close()


