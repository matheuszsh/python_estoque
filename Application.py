import Produto
import GerenciarEstoque

from colorama import init as colorama_init, Fore

colorama_init()

db = GerenciarEstoque.GerenciarEstoque()

# CATEGORIAS
# 1 - geral

def main():
    print(Fore.RED + "|---|CADASTRO-DE-PRODUTOS|---|")
    print(Fore.GREEN + "\n1 - Cadastrar Produto") # Create
    print(Fore.GREEN + "2 - Mostrar Produto") # Read
    print(Fore.GREEN + "3 - Alterar Produto") # Update
    print(Fore.GREEN + "4 - Deletar Produto\n\n") # Delete
    print(Fore.RED + "0 - sair\n")
    option_menu = int(input(">>>:"))

    # CADASTRAR
    if option_menu == 1:
        print(Fore.RED+"Informe os dados:\n")
        nome = input(Fore.GREEN+"Nome:")
        preco = float(input(Fore.GREEN+"Preço:"))
        qntd = int(input(Fore.GREEN+"quantidade: "))
        cat = int(1)

        objProduto = Produto.Produto(nome,preco, qntd, cat)

        resp = db.inserir_item(objProduto)

        print(resp)

    # MOSTRAR
    elif option_menu == 2:
        id_produto = informe_id()

        resp = db.mostrar_item(id_produto)

        print(Fore.GREEN + resp)
    
    # ALTERAR
    elif option_menu == 3:
        id_produto = informe_id()

        print("\nInforme Opção De Edição:\n\n")
        print("1 - nome")
        print("2 - preço")
        print("3 - quantidade")
        print("4 - categoria")

        option_edit = int(input(">>>:"))

        option_edit_list = {
            1:"nome",
            2:"preço",
            3:"quantidade",
            4:"categorias_id"
        }

        edit = input(f"Edite {option_edit_list[option_edit]}:")
    
        resp = db.editar_item(id_produto, option_edit_list[option_edit], edit)
        
        print(resp)

    # DELETAR
    elif option_menu == 4:
        id_produto = informe_id()
        
        resp = db.deletar_item(id_produto)

        print(resp)
    
    else:
        print("Programa encerrado.")

def informe_id():
    print(Fore.RED+"Informe ID do produto:")
    id_produto = int(input(Fore.GREEN + ">>>:"))

    return id_produto


if __name__ == "__main__":
    main()