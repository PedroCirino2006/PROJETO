# main.py
from lib.funcoes import *

def exibir_menu():
    print("\nMENU:")
    print("1. Cadastrar Categoria")
    print("2. Cadastrar Produto")
    print("3. Consultar Produto")
    print("4. Atualizar Produto")
    print("5. Excluir Produto")
    print("6. Exibir Todos os Produtos")
    print("7. Exibir Todas as Categorias")
    print("8. Excluir Categoria")
    print("9. Editar Categoria")
    print("10. Consultar categoria")
    print("11. Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_categoria = int(input("Digite o ID da nova categoria: "))
            nome_categoria = input("Digite o nome da nova categoria: ")
            cadastrar_categoria(id_categoria, nome_categoria)
        elif escolha == "2":
            id_produto = int(input("Digite o ID do novo produto: "))
            nome_produto = input("Digite o nome do novo produto: ")
            categoria_id = int(input("Digite o ID da categoria do novo produto: "))
            cadastrar_produto(id_produto, nome_produto, categoria_id)
        elif escolha == "3":
            id_produto = int(input("Digite o ID do produto a ser consultado: "))
            print("Consulta de produto:", consultar_produto(id_produto))
        elif escolha == "4":
            id_produto = int(input("Digite o ID do produto a ser atualizado: "))
            nome_produto = input("Digite o novo nome do produto: ")
            categoria_id = int(input("Digite o novo ID da categoria do produto: "))
            atualizar_produto(id_produto, nome_produto, categoria_id)
        elif escolha == "5":
            id_produto = int(input("Digite o ID do produto a ser excluído: "))
            excluir_produto(id_produto)
        elif escolha == "6":
            print("Lista de todos os produtos:")
            exibir_todos_produtos()
        elif escolha == "7":
            print("Lista de todas as categorias:")
            exibir_todas_categorias()
        elif escolha == "8":
            id_categoria = int(input("Digite o ID da categoria a ser excluída: "))
            excluir_categoria(id_categoria)
        elif escolha == "9":
            id_categoria = int(input("Digite o ID da categoria a ser editada: "))
            novo_nome_categoria = input("Digite o novo nome da categoria: ")
            editar_categoria(id_categoria, novo_nome_categoria)
        elif escolha == "10":
            id_categoria = int(input("Digite o ID da categoria a ser consultada: "))
            print("Consulta de categoria:", consultar_categoria(id_categoria))
        elif escolha == "11":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
