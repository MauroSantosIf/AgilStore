import json
import os

# Classe que representa o produto no inventário
class Produto:
    def __init__(self, nome, categoria, quantidade, preco, id=None):
        self.id = id or self.gerar_id() 
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
    
    def gerar_id(self):
        return str(Produto.id_counter)
    
    # Método para converter o objeto Produto para um formato de dicionário (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "preco": self.preco
        }

Produto.id_counter = 1 

# Função para carregar os produtos do arquivo JSON
def carregar_produtos():
    if os.path.exists('inventario.json'):
        with open('inventario.json', 'r') as arquivo:
            produtos_data = json.load(arquivo)
            if produtos_data:
                Produto.id_counter = max(int(produto["id"]) for produto in produtos_data) + 1
            return [Produto(**produto) for produto in produtos_data]
    else:
        return []

# Função para salvar os produtos no arquivo JSON
def salvar_produtos(produtos):
    with open('inventario.json', 'w') as arquivo:
        produtos_data = [produto.to_dict() for produto in produtos]
        json.dump(produtos_data, arquivo, indent=4)

# Função para adicionar um novo produto ao inventário
def adicionar_produto():
    print("Cadastro de novo produto:")
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: "))
    
    produto = Produto(nome, categoria, quantidade, preco)
    return produto

# Função para excluir um produto do inventário
def excluir_produto(produtos):
    produto_id = input("Digite o ID do produto que deseja excluir: ")
    
    produto = next((p for p in produtos if p.id == produto_id), None)
    
    if produto:
        print(f"\nProduto encontrado: {produto.nome}")
        
        confirmar = input(f"\nTem certeza que deseja excluir o produto '{produto.nome}'? (S/N): ")
        
        if confirmar.lower() == 's':
            produtos.remove(produto)
            salvar_produtos(produtos)
            print(f"\nProduto '{produto.nome}' excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")
    else:
        print("\nProduto não encontrado.")

# Função para buscar um produto por ID ou nome
def buscar_produto(produtos):
    opcao_busca = input("Deseja buscar por (1) ID ou (2) Nome do Produto? Digite 1 ou 2: ")

    if opcao_busca == '1':
        produto_id = input("Digite o ID do produto: ")
        produto = next((p for p in produtos if p.id == produto_id), None)
        
        if produto:
            print(f"\nProduto encontrado: {produto.nome}")
        else:
            print("\nProduto não encontrado com o ID informado.")

    elif opcao_busca == '2':
        nome_produto = input("Digite parte do nome do produto: ").lower()
        produtos_encontrados = [p for p in produtos if nome_produto in p.nome.lower()]
        
        if produtos_encontrados:
            print("\nProdutos encontrados:")
            for p in produtos_encontrados:
                print(p.nome)
        else:
            print("\nNenhum produto encontrado com esse nome.")
    else:
        print("\nOpção inválida. Tente novamente.")


# Função para listar todos os produtos em formato de tabela
def listar_produtos(produtos):
    if produtos:
        print("\n--- Produtos no Inventário ---")
        print(f"{'ID':<6} {'Nome':<30} {'Categoria':<20} {'Quantidade':<15} {'Preço':<10}")
        print("="*91)
        
        for produto in produtos:
            print(f"{produto.id:<6} {produto.nome:<30} {produto.categoria:<20} {produto.quantidade:<15} R${produto.preco:10.2f}")
    else:
        print("\nNão há produtos no inventário.")

# Função para filtrar produtos por categoria
def filtrar_por_categoria(produtos, categoria):
    return [produto for produto in produtos if produto.categoria.lower() == categoria.lower()]

# Função para ordenar produtos
def ordenar_produtos(produtos, criterio):
    if criterio == "nome":
        return sorted(produtos, key=lambda p: p.nome.lower())
    elif criterio == "quantidade":
        return sorted(produtos, key=lambda p: p.quantidade)
    elif criterio == "preco":
        return sorted(produtos, key=lambda p: p.preco)
    else:
        return produtos

# Função para atualizar as informações de um produto
def atualizar_produto(produtos):
    produto_id = input("Digite o ID do produto que deseja atualizar: ")
    
    produto = next((p for p in produtos if p.id == produto_id), None)
    
    if produto:
        print(f"\nProduto encontrado: {produto}")
        print("\nQuais informações deseja atualizar?")
        print("1. Nome")
        print("2. Categoria")
        print("3. Quantidade")
        print("4. Preço")
        print("5. Cancelar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            novo_nome = input(f"Digite o novo nome (atual: {produto.nome}): ")
            produto.nome = novo_nome
        elif opcao == '2':
            nova_categoria = input(f"Digite a nova categoria (atual: {produto.categoria}): ")
            produto.categoria = nova_categoria
        elif opcao == '3':
            nova_quantidade = int(input(f"Digite a nova quantidade (atual: {produto.quantidade}): "))
            if nova_quantidade >= 0:
                produto.quantidade = nova_quantidade
            else:
                print("Quantidade inválida. A quantidade não pode ser negativa.")
                return
        elif opcao == '4':
            novo_preco = float(input(f"Digite o novo preço (atual: R${produto.preco}): "))
            if novo_preco >= 0:
                produto.preco = novo_preco
            else:
                print("Preço inválido. O preço não pode ser negativo.")
                return
        elif opcao == '5':
            print("\nAtualização cancelada.")
            return
        else:
            print("\nOpção inválida.")
            return
        
        print(f"\nProduto atualizado: {produto}")
        salvar_produtos(produtos) 
        print("\nAlterações salvas com sucesso!")
    else:
        print("\nProduto não encontrado.")

# Função principal que gerencia o inventário
def gerenciar_inventario():
    produtos = carregar_produtos() 
    while True:
        print("\n--- Gerenciamento de Inventário ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Filtrar Produtos por Categoria")
        print("4. Ordenar Produtos")
        print("5. Atualizar Produto")
        print("6. Buscar Produto")
        print("7. Excluir Produto")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            produto = adicionar_produto()
            produtos.append(produto) 
            salvar_produtos(produtos)
            print(f"\nProduto '{produto.nome}' adicionado com sucesso!\n")
        
        elif opcao == '2':
            listar_produtos(produtos)
        
        elif opcao == '3':
            categoria = input("Digite a categoria para filtrar: ")
            produtos_filtrados = filtrar_por_categoria(produtos, categoria)
            listar_produtos(produtos_filtrados)
        
        elif opcao == '4':
            print("\nOpções de ordenação: ")
            print("1. Ordenar por Nome")
            print("2. Ordenar por Quantidade")
            print("3. Ordenar por Preço")
            criterio = input("Escolha uma opção: ")
            
            if criterio == '1':
                produtos_ordenados = ordenar_produtos(produtos, "nome")
            elif criterio == '2':
                produtos_ordenados = ordenar_produtos(produtos, "quantidade")
            elif criterio == '3':
                produtos_ordenados = ordenar_produtos(produtos, "preco")
            else:
                print("\nOpção inválida, retornando ao menu.")
                continue
            
            listar_produtos(produtos_ordenados)
        
        elif opcao == '5':
            atualizar_produto(produtos)
        
        elif opcao == '6':
            buscar_produto(produtos)
        
        elif opcao == '7':
            excluir_produto(produtos)
        
        elif opcao == '8':
            print("\nSaindo do sistema.")
            break
        
        else:
            print("\nOpção inválida, tente novamente.")


# Iniciar o gerenciamento de inventário
gerenciar_inventario()