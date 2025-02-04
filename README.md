# Gerenciamento de Inventário

## Visão Geral do Projeto

Este projeto tem como objetivo gerenciar um inventário de produtos, permitindo adicionar, listar, buscar, atualizar, excluir e ordenar produtos. Os dados são armazenados em um arquivo JSON, garantindo persistência entre execuções.

## Demandas Encontradas no Estabelecimento

As principais necessidades identificadas para o desenvolvimento deste projeto foram:

Falta de um controle eficiente de estoque.

Dificuldade em localizar produtos rapidamente.

Necessidade de categorizar produtos.

Falta de um histórico atualizado dos produtos.

Necessidade de ordenação e filtragem para melhor gestão.

## Objetivos do Projeto

Criar um sistema simples e funcional para gestão de inventário.

Permitir a adição e remoção de produtos.

Implementar busca eficiente por ID e nome.

Possibilitar a organização dos produtos por categoria, quantidade e preço.

Garantir a persistência dos dados utilizando arquivos JSON.

Criar uma interface de terminal amigável para o usuário.

## Requisitos Desenvolvidos

Cadastro de produtos: O sistema permite a inserção de novos produtos, exigindo informações como nome, categoria, quantidade e preço.

Listagem de produtos: Exibe os produtos em formato de tabela.

Busca de produtos: Permite buscar um produto por ID ou nome.

Filtragem por categoria: Usuários podem visualizar produtos de uma categoria específica.

Ordenação: Os produtos podem ser ordenados por nome, quantidade ou preço.

Atualização de produtos: O sistema permite a edição dos atributos de um produto.

Exclusão de produtos: O usuário pode remover um produto com base em seu ID.

Persistência de dados: Os produtos são armazenados em um arquivo JSON para garantir que os dados não sejam perdidos após o encerramento do programa.

## Funcionalidades Atendidas

O sistema atendeu aos seguintes requisitos:

Controle eficiente de estoque.

Facilidade na busca por produtos.

Possibilidade de organizar e filtrar produtos de maneira intuitiva.

Persistência de dados por meio de armazenamento em JSON.

Interface amigável via terminal.

## Estruturas Utilizadas no Código

Classe Produto: Representa cada item no inventário.

Listas: Armazena os produtos carregados do JSON e manipula os mesmos.

Dicionários: Usados para armazenar as informações dos produtos no formato JSON.

### Funções:

carregar_produtos(): Lê e carrega os produtos do arquivo JSON.

salvar_produtos(): Salva os produtos no arquivo JSON.

adicionar_produto(): Solicita ao usuário informações e adiciona um novo produto.

listar_produtos(): Exibe os produtos cadastrados.

buscar_produto(): Realiza busca por ID ou nome.

filtrar_por_categoria(): Permite visualizar apenas os produtos de uma categoria.

ordenar_produtos(): Ordena os produtos por critérios escolhidos pelo usuário.

atualizar_produto(): Permite alterar informações de um produto.

excluir_produto(): Remove um produto com base em seu ID.

gerenciar_inventario(): Função principal que executa o sistema e gerencia as opções do usuário.

## Formato de Armazenamento

Os produtos são armazenados em um arquivo JSON chamado inventario.json. O formato de cada produto no arquivo é o seguinte:

~~~[
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
~~~

## Como Executar o Projeto

Certifique-se de ter o Python instalado em seu sistema.

Salve o arquivo do código como inventario.py.

Execute o comando no terminal:
~~~
python inventario.py
~~~
Navegue pelas opções do menu interativo para gerenciar seu inventário.

## Conclusão

Este projeto oferece um sistema funcional para controle de inventário utilizando Python e arquivos JSON. Ele é fácil de usar, escalável e pode ser adaptado para diferentes necessidades de gestão de estoque.
