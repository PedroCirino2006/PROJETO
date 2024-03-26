# funcoes.py
from database import categorias, produtos

# Função para exibir todos os produtos
def exibir_todos_produtos():
    for id_produto, produto in produtos.items():
        print(f"ID: {id_produto}, Nome: {produto['nome']}, Categoria ID: {produto['categoria_id']}")

# Função para exibir todas as categorias
def exibir_todas_categorias():
    for id_categoria, nome_categoria in categorias.items():
        print(f"ID: {id_categoria}, Nome: {nome_categoria}")

# Função para cadastrar uma nova categoria
def cadastrar_categoria(id_categoria, nome_categoria):
    categorias[id_categoria] = nome_categoria

# Função para cadastrar um novo produto
def cadastrar_produto(id_produto, nome_produto, categoria_id):
    produto = {"nome": nome_produto, "categoria_id": categoria_id}
    produtos[id_produto] = produto

# Função para consultar um produto
def consultar_produto(id_produto):
    return produtos.get(id_produto)

# Função para excluir um produto
def excluir_produto(id_produto):
    if id_produto in produtos:
        del produtos[id_produto]
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")

# Função para atualizar um produto
def atualizar_produto(id_produto, nome_produto, categoria_id):
    if id_produto in produtos:
        produtos[id_produto]["nome"] = nome_produto
        produtos[id_produto]["categoria_id"] = categoria_id
        print("Produto atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

# Função para excluir uma categoria
def excluir_categoria(id_categoria):
    if id_categoria in categorias:
        del categorias[id_categoria]
        print("Categoria excluída com sucesso.")
    else:
        print("Categoria não encontrada.")

# Função para editar uma categoria
def editar_categoria(id_categoria, novo_nome_categoria):
    if id_categoria in categorias:
        categorias[id_categoria] = novo_nome_categoria
        print("Categoria atualizada com sucesso.")
    else:
        print("Categoria não encontrada.")
        
def consultar_categoria(id_categoria):
    if id_categoria in categorias:
        nome_categoria = categorias[id_categoria]
        print(f"Nome da Categoria: {nome_categoria}")
        
        print("Produtos nesta categoria:")
        for id_produto, produto in produtos.items():
            if produto['categoria_id'] == id_categoria:
                print(f"ID: {id_produto}, Nome: {produto['nome']}")
    else:
        print("Categoria não encontrada.")