import sqlite3
import colorama

# Criando banco de dados ou abrindo caso exista
conn = sqlite3.connect("estoque.db")
# Cursor para executar os métodos do obj
cur = conn.cursor()

class GerenciarEstoque:
    def __init__(self):
        self.objProduto = None

    def criar_tabelas():
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(20) NOT NULL
                        )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(20) NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL,
                categorias_id INTEGER,
                FOREIGN KEY (categorias_id) REFERENCES categorias(id)
                    )
        """)

    def inserir_item(self, objProduto):
        self.objProduto = objProduto

        varProduto = [(objProduto.nome,
                        objProduto.preco,
                        objProduto.quantidade,
                        objProduto.categorias_id)]


        cur.executemany("""
                INSERT INTO produtos('nome', 'preco', 'quantidade', 'categorias_id')
                VALUES (?,?,?,?)
            """, varProduto)

        conn.commit()

        return f"\nDADOS PRODUTO CADASTRADO\n\n" + "NOME: {}\nPREÇO: {}\nQNTD: {}\nCAT ID: {}".format(objProduto.nome, objProduto.preco, objProduto.quantidade, objProduto.categorias_id)



    def mostrar_item(self, id_produto):
        item = cur.execute("""
            SELECT * FROM produtos
            WHERE id = ? 
        """, (id_produto,)).fetchone()

        return "\nDADOS PRODUTO\n\n" + "NOME: {}\nPREÇO: {}\nQNTD: {}\nCAT ID: {}".format(item[1], item[2], item[3], item[4])

    def editar_item(self, id_produto, campo, novo_valor):
        #ANTI SQL Injection
        campos_permitidos = ["nome", "preco", "quantidade", "categorias_id"]
        if campo not in campos_permitidos:
            raise ValueError(f"Campo inválido: {campo}")

        sql = f"UPDATE produtos SET {campo} = ? WHERE id = ?"

        cur.execute(sql, (novo_valor, id_produto))
        conn.commit()

        return cur.rowcount  # número de linhas alteradas
    
    def deletar_item(self, id_produto):

        sql = f"SELECT * FROM produtos WHERE id = ?"

        deletado = cur.execute(sql, (id_produto,)).fetchone()

        sql = f"DELETE FROM produtos WHERE id = ?"

        cur.execute(sql, (id_produto,))
        conn.commit()

        return f"Produto '{deletado}' deletado."