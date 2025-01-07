# AgilStore - Gerenciamento de Inventário

O AgilStore é uma aplicação para gerenciamento de inventário de produtos de uma loja de eletrônicos. Ela permite realizar operações como adicionar, listar, buscar, excluir, atualizar e ordenar produtos, além de manter um controle eficiente do estoque utilizando um arquivo JSON para persistência dos dados.

Funcionalidades
Adicionar Produto: Cadastro de novos produtos com informações como nome, categoria, quantidade e preço.
Listar Produtos: Exibe todos os produtos do inventário com suas informações.
Filtrar por Categoria: Exibe produtos de uma categoria específica.
Ordenar Produtos: Ordena os produtos por nome, quantidade ou preço.
Atualizar Produto: Permite atualizar as informações de um produto existente.
Excluir Produto: Remove um produto do inventário.
Buscar Produto: Pesquisa produtos por ID ou por parte do nome.
Requisitos
Python 3.x
Sistema operacional: Pode ser rodado em qualquer sistema operacional com suporte para Python (Windows, Linux, macOS).
# Instalação e Execução
1. Instalar o Python
Certifique-se de ter o Python 3.x instalado em sua máquina. Caso não tenha, faça o download e instale-o a partir do site oficial do Python.

2. Preparando o Ambiente
Se você estiver usando uma máquina virtual (como o VirtualBox ou VMware) e quiser rodar o código dentro dessa VM, siga os seguintes passos:

a. Instalar o Python na Máquina Virtual
Verifique se o Python está instalado executando o seguinte comando:

python3 --version
Caso não esteja instalado, use o gerenciador de pacotes do seu sistema para instalá-lo.

## Para Ubuntu/Debian:

sudo apt update
sudo apt install python3

## Para CentOS/RHEL:

sudo yum install python3

## Para macOS com Homebrew:

brew install python3

b. Clonando o Repositório
Se você estiver rodando o código em um repositório Git, clone o repositório na máquina virtual:

git clone https://github.com/MauroSantosIf/AgilStore.git

c. Criar um Ambiente Virtual (opcional, mas recomendado)
## Para isolar as dependências, crie um ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows

3. Rodando o Código
Com o ambiente configurado, basta executar o script Python para iniciar o gerenciamento de inventário:

python3 store.py

4. Interação com a Aplicação
Ao rodar o código, o menu principal será exibido.
Você poderá escolher as opções interativas para adicionar, listar, buscar, atualizar, excluir ou ordenar os produtos.
A aplicação lê e escreve em um arquivo inventario.json na mesma pasta, garantindo que os dados sejam persistidos.

## Formato de Armazenamento
Os produtos são armazenados em um arquivo JSON chamado inventario.json. O formato de cada produto no arquivo é o seguinte:

[
  {
    "id": "1",
    "nome": "Smartphone XYZ",
    "categoria": "Smartphones",
    "quantidade": 50,
    "preco": 999.99
  },
  {
    "id": "2",
    "nome": "Laptop ABC",
    "categoria": "Laptops",
    "quantidade": 20,
    "preco": 2999.99
  }
]

# Exemplo de Uso
Adicionar Produto: O usuário pode cadastrar novos produtos inserindo os dados como nome, categoria, quantidade e preço.

1-Listar Produtos: Exibe todos os produtos cadastrados no inventário.

2-Filtrar por Categoria: Mostra todos os produtos de uma categoria específica.

3-Ordenar Produtos: Permite ordenar os produtos por nome, quantidade ou preço.

4-Buscar Produto: O usuário pode buscar produtos por ID ou nome, exibindo informações detalhadas.

5-Atualizar Produto: Permite alterar informações como nome, categoria, quantidade ou preço de um produto.

6-Excluir Produto: Remove um produto do inventário, após confirmação.

Contribuição
Sinta-se à vontade para contribuir com melhorias no código. Você pode enviar pull requests ou abrir issues para discutir novos recursos ou corrigir problemas.
