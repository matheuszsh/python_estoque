from Produto import Produto
from GerenciarEstoque import GerenciarEstoque

from colorama import init as colorama_init, Fore

colorama_init()

db = GerenciarEstoque()

# FUNÇÃO: CADASTRAR
def func_cadastrar_produto(codigo, nome, preco, qntd):
    try:         
        buffer_codigo = 6
        codigo = str(codigo)
        nome = str(nome)
        preco = float(preco)
        qntd = int(qntd)
        cat = int(1)

        trava_loop = True
        while trava_loop:
            codigo = codigo

            if len(codigo) > buffer_codigo:
                return None
            else:
                if db.verificar_existencia_codigo(codigo=codigo):
                    return None
                else:
                    trava_loop = False

        objProduto = Produto(codigo, nome, preco, qntd, cat)

        resp = db.inserir_item(objProduto)

        return resp
    
    except:
        return False

# FUNçÃO: MOSTRAR
def func_mostrar_produto(codigo_produto):
    if db.verificar_existencia_codigo(codigo=codigo_produto):

        resp = db.mostrar_item(codigo_produto)

        return resp
    else:
        return None

# FUNÇÃO: ENTRADAS E SAÍDAS
def func_entradas_saidas(codigo_produto, opcao, quantidade):

    if db.verificar_existencia_codigo(codigo=codigo_produto):
        opcao_fluxo = opcao

        if opcao_fluxo >= 0 and opcao_fluxo <= 1:

            resp = db.entradas_saidas(codigo_produto, opcao_fluxo, quantidade)

            return f"Código: {codigo_produto}, {resp}"
        else:
            return f"Opção inválida"
    else:
        return "Produto não encontrado"
    
        
# FUNÇÃO: ALTERAR
def func_alterar_produto(codigo_produto, codigo_edit, nome_edit, preco_edit, qntd_edit):

    if db.verificar_existencia_codigo(codigo=codigo_produto, ):
        
        if len(codigo_produto) > 6 or len(codigo_edit) >6:
            return None

        if db.verificar_existencia_codigo(codigo=codigo_edit):
            return "Já existe um produto com esse código"

        status_input = [codigo_edit, nome_edit, preco_edit]
        option_edit = []

        for e in status_input:
            if e != "":
                option_edit.append(status_input.index(e))

        option_edit_list = {
            0:"codigo",
            1:"nome",
            2:"preco",
            #3:"quantidade",
            #4:"categorias_id"
        }

        resp = []

        for e in option_edit:
            resp.append(db.editar_item(codigo_produto, option_edit_list[e], status_input[e]))
                
        return resp

    else:
        if codigo_produto == "":
            return "Informe o código"

        return "Código do produto não foi cadastrado."


# FUNÇÃO: DELETAR
def func_deletar_produto(codigo_produto, confirmacao):
    
    if db.verificar_existencia_codigo(codigo_produto) and confirmacao == 1:
        resp = db.deletar_item(codigo_produto)
        return resp
    elif codigo_produto == '':
        return "informe código"

    elif confirmacao != 1:
        return "Confirme para deletar o produto"
    else:
        return "Código Não Existe."

# FUNÇÃO: IMPORTAR
def func_importar_arquivo():
    resp = db.importar_arquivo()

    return resp

# FUNÇÃO: BUSCAR CODIGO NO BANCO DE DADOS
def informe_codigo():
    print(Fore.RED+"Informe CODIGO do produto:")
    codigo_produto = str(input(Fore.GREEN + ">>>:"))

    return codigo_produto
