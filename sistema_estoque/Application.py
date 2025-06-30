from Produto import Produto
from GerenciarEstoque import GerenciarEstoque

from colorama import init as colorama_init, Fore

colorama_init()

db = GerenciarEstoque()

def main():
    try:
        print(Fore.RED + "|---|CADASTRO-DE-PRODUTOS|---|")
        print(Fore.GREEN + "\n1 - Cadastrar Produto") # Create
        print(Fore.GREEN + "2 - Mostrar Produto") # Read
        print(Fore.GREEN + "3 - Entradas e Saídas")
        print(Fore.GREEN + "4 - Alterar Produto") # Update
        print(Fore.GREEN + "5 - Deletar Produto\n") # Delete
        print(Fore.GREEN + "6 - importar arquivo\n")
        print(Fore.RED + "0 - sair\n")
        option_menu = int(input(">>>:"))

        # CADASTRAR
        if option_menu == 1:
            func_cadastrar_produto()

        # MOSTRAR
        elif option_menu == 2:
            func_mostrar_produto()
        
        # ALTERAR
        elif option_menu == 3:
            func_entradas_saidas()

        # DELETAR
        elif option_menu == 4:
            func_alterar_produto()
        
        # IMPORTAR
        elif option_menu == 5:
            fun_deletar_produto()

        
        elif option_menu == 6:
            fun_importar_arquivo()
        
        elif option_menu == 0:
            print("Programa encerrado.")
        else:
            print("Esta opção não existe.")
            main()
    except ValueError:
        print("ERRO: Entrada inválida.")

# FUNÇÃO: CADASTRAR
def func_cadastrar_produto():
    print(Fore.RED+"Informe os dados:\n")
            
    buffer_codigo = 6
    codigo = ""

    trava_loop = True
    while trava_loop:
        codigo = input(Fore.GREEN+"Código: ")

        if len(codigo) > buffer_codigo:
            print("Código não pode ter mais de 6 digitos")
        else:
            if db.verificar_existencia_codigo(codigo=codigo):
                print("Código do produto digitado já existe.")
                trava_loop = True
            else:
                trava_loop = False

    nome = input(Fore.GREEN+"Nome: ")
    preco = float(input(Fore.GREEN+"Preço: "))
    qntd = int(input(Fore.GREEN+"Quantidade: "))
    cat = int(1)

    objProduto = Produto(codigo, nome, preco, qntd, cat)

    resp = db.inserir_item(objProduto)

    print(resp)
    main()

# FUNçÃO: MOSTRAR
def func_mostrar_produto():
    codigo_produto = informe_codigo()

    if db.verificar_existencia_codigo(codigo=codigo_produto):

        resp = db.mostrar_item(codigo_produto)

        print(Fore.GREEN + resp)
    else:
        print("Código do produto não foi cadastrado.")

    main()         

# FUNÇÃO: ENTRADAS E SAÍDAS
def func_entradas_saidas():
    codigo_produto = informe_codigo()

    if db.verificar_existencia_codigo(codigo=codigo_produto):
        print("\nInforme a Opção de ENTRADA ou SAÍDA\n\n")
        print("0 - Entrada")
        print("1 - Saída\n")
        opcao_fluxo = int(input(">>>:"))

        if opcao_fluxo >= 0 and opcao_fluxo <= 1:
            qntd = int(input("Insira Quantidade:"))

            resp = db.entradas_saidas(codigo_produto, opcao_fluxo, qntd)

            print(resp)
        else:
            print("Opção inválida")

        main()
        
# FUNÇÃO: ALTERAR
def func_alterar_produto():
    codigo_produto = informe_codigo()

    if db.verificar_existencia_codigo(codigo=codigo_produto):
        print("\nInforme Opção De Edição:\n\n")
        print("0 - Código")
        print("1 - Nome")
        print("2 - Preço")
        print("3 - Quantidade")
        print("4 - Categoria")

        option_edit = int(input(">>>:"))

        option_edit_list = {
            0:"codigo",
            1:"nome",
            2:"preco",
            3:"quantidade",
            4:"categorias_id"
        }

        print(f"Alterar {option_edit_list[option_edit]}:")
        edit = input(">>>:")
            
        resp = db.editar_item(codigo_produto, option_edit_list[option_edit], edit)
                
        print(resp)

    else:
        print("Código do produto não foi cadastrado.")

    main

# FUNÇÃO: DELETAR
def fun_deletar_produto():
    codigo_produto = informe_codigo()
            
    resp = db.deletar_item(codigo_produto)

    print(resp)

    main()

# FUNÇÃO: IMPORTAR
def fun_importar_arquivo():
    db.importar_arquivo()

# FUNÇÃO: BUSCAR CODIGO NO BANCO DE DADOS
def informe_codigo():
    print(Fore.RED+"Informe CODIGO do produto:")
    codigo_produto = str(input(Fore.GREEN + ">>>:"))

    return codigo_produto

if __name__ == "__main__":
    main()