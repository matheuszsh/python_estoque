import sqlite3

conn = sqlite3.connect("estoque.db")
cur = conn.cursor()

class GerenciarEstoque:
    def __init__(self):
        self.objProduto = None

    def inserir_item(self, objProduto):
        self.objProduto = objProduto

        buffer_codigo = 6

        if len(objProduto.codigo) > buffer_codigo:
            raise ValueError(f"O código deve possuir {buffer_codigo} digitos.")


        varProduto = [(objProduto.codigo,
                        objProduto.nome,
                        objProduto.preco,
                        objProduto.quantidade,
                        objProduto.categorias_id)]


        cur.executemany("""
                INSERT INTO produtos('codigo','nome', 'preco', 'quantidade', 'categorias_id')
                VALUES (?,?,?,?,?)
            """, varProduto)
        
        logs_gen = "CRIADO"

        self.gerar_logs(logs_gen, codigo=objProduto.codigo)

        conn.commit()

        return f"\nDADOS PRODUTO CADASTRADO\n\n" + "CÓDIGO: {}\nNOME: {}\nPREÇO: {}\nQNTD: {}\nCAT ID: {}".format(objProduto.codigo, objProduto.nome, objProduto.preco, objProduto.quantidade, objProduto.categorias_id)



    def mostrar_item(self, codigo_produto):
        item = cur.execute("""
            SELECT * FROM produtos
            WHERE codigo = ? 
        """, (codigo_produto,)).fetchone()

        return "\nDADOS PRODUTO\n\n" + "CÓDIGO: {}\nNOME: {}\nPREÇO: {}\nQNTD: {}\nCAT ID: {}".format(item[0],item[1], item[2], item[3], item[4])
    
    def entradas_saidas(self,codigo_produto, opcao_fluxo, qntd):
        
        if opcao_fluxo == 0:
            sql = "UPDATE produtos " \
            "SET quantidade = quantidade + ? " \
            "WHERE codigo = ?"

            msg = "Entrada: "

        elif opcao_fluxo == 1:

            sql = "UPDATE produtos " \
            "SET quantidade = quantidade - ? " \
            "WHERE codigo = ?"

            msg = "Saída: "

        cur.execute(sql, (qntd, codigo_produto))
        conn.commit()

        return msg + str(qntd)

    def editar_item(self, codigo_produto, campo, novo_valor):
        #ANTI SQL Injection
        campos_permitidos = ["codigo","nome", "preco", "quantidade", "categorias_id"]
        if campo not in campos_permitidos:
            raise ValueError(f"Campo inválido: {campo}")

        backup_valor_antigo = cur.execute(f"SELECT {campo} FROM produtos WHERE codigo = ?", (codigo_produto,)).fetchone()
        backup_valor_antigo = backup_valor_antigo[0]

        sql = f"UPDATE produtos SET {campo} = ? WHERE codigo = ?"

        cur.execute(sql, (novo_valor, codigo_produto))

        logs_gen = "ALTERADO"

        self.gerar_logs(logs_gen,codigo=codigo_produto, valor_antigo=backup_valor_antigo, valor_novo=novo_valor, campo=campo)

        conn.commit()

        return "Produto alterado com sucesso."
    
    def deletar_item(self, codigo_produto):

        sql = f"SELECT * FROM produtos WHERE codigo = ?"

        deletado = cur.execute(sql, (codigo_produto,)).fetchone()

        sql = f"DELETE FROM produtos WHERE codigo = ?"

        cur.execute(sql, (codigo_produto,))
        conn.commit()

        return f"Produto '{deletado}' deletado."
    
    def verificar_existencia_codigo(self, codigo):

        sql = """
            SELECT 1 FROM produtos WHERE codigo = ?
        """

        resp = cur.execute(sql, (codigo,)).fetchone()

        if resp:
            return True
        else:
            return False

    def gerar_logs(self, evento=None ,codigo=None, valor_antigo=None, valor_novo=None, campo=None):
        
        tipos_log = {
            0 : "CRIADO",
            1 : "ALTERADO",
        }

        if evento == None and codigo == None:
            return

        if evento == tipos_log[0]:
            sql = "INSERT INTO log_produtos('tipo_evento', 'codigo_produto', 'instancia')" \
            "VALUES(?,?,?)"

            cur.execute(sql, (evento, codigo, 0))

        elif evento == tipos_log[1]:
            
            cur.execute("SELECT COUNT(*) FROM log_produtos WHERE codigo_produto = ?", (codigo,))
            count = cur.fetchone()[0]

            sql = "INSERT INTO log_produtos('tipo_evento', 'valor_anterior', 'novo_valor', 'codigo_produto', 'campo', 'instancia')" \
            "VALUES(?,?,?,?,?,?)"

            cur.execute(sql, (evento, valor_antigo, valor_novo, codigo, campo, count))

        conn.commit()

    def importar_arquivo(self, path=None):

        lista_produtos = []
        lista_codigo = []

        with open("arquivos_csv/arquivo.csv") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')

                tupla = (
                    str(partes[0]),
                    str(partes[1]),
                    float(partes[2]),
                    int(partes[3]),
                    int(partes[4])
                )
                if not(self.verificar_existencia_codigo(partes[0])):
                    lista_produtos.append(tupla)
                    lista_codigo.append(tupla[0])
                else:
                    print("Código já existe. Item não cadastrado.")

        sql = "INSERT INTO produtos('codigo','nome', 'preco', 'quantidade', 'categorias_id')" \
            "VALUES (?,?,?,?,?)"
        
        cur.executemany(sql, lista_produtos)

        logs_gen = "CRIADO"

        for codigo in lista_codigo:
            self.gerar_logs(evento=logs_gen,codigo=codigo)

        conn.commit()