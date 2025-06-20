import Produto
import GerenciarEstoque

from colorama import init as colorama_init, Fore

colorama_init()

db = GerenciarEstoque.GerenciarEstoque()

# CATEGORIAS
# 1 - geral

def main():
    try:
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
            
            # Verificar entrada do código > que 6 digitos
            codigo = input(Fore.GREEN+"Código: ")
            nome = input(Fore.GREEN+"Nome: ")
            preco = float(input(Fore.GREEN+"Preço: "))
            qntd = int(input(Fore.GREEN+"Quantidade: "))
            cat = int(1)

            objProduto = Produto.Produto(codigo, nome, preco, qntd, cat)

            resp = db.inserir_item(objProduto)

            print(resp)

            main()

        # MOSTRAR
        elif option_menu == 2:
            codigo_produto = informe_codigo()

            resp = db.mostrar_item(codigo_produto)

            print(Fore.GREEN + resp)

            main()
        
        # ALTERAR
        elif option_menu == 3:
            codigo_produto = informe_codigo()

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
                2:"preço",
                3:"quantidade",
                4:"categorias_id"
            }

            edit = input(f"Edite {option_edit_list[option_edit]}:")
        
            resp = db.editar_item(codigo_produto, option_edit_list[option_edit], edit)
            
            print(resp)

            main()

        # DELETAR
        elif option_menu == 4:
            codigo_produto = informe_codigo()
            
            resp = db.deletar_item(codigo_produto)

            print(resp)

            main()
        
        elif option_menu == 0:
            print("Programa encerrado.")
        else:
            print("Esta opção não existe.")
            main()
    except ValueError:
        print("ERRO: Entrada inválida.")

def informe_codigo():
    print(Fore.RED+"Informe CODIGO do produto:")
    codigo_produto = str(input(Fore.GREEN + ">>>:"))

    return codigo_produto


if __name__ == "__main__":
    main()