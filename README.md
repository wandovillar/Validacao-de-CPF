# Lista de Compras Interativa 🛒

Este é um projeto simples em Python que permite ao usuário gerenciar uma **lista de compras** de forma interativa pelo terminal. O programa apresenta um menu com opções para **inserir**, **apagar** e **listar** itens.

---

## Funcionalidades

1. **Inserir Itens**: Adicione itens à sua lista de compras.
2. **Listar Itens**: Exiba todos os itens atualmente na lista.
3. **Apagar Itens**: Remova itens da lista utilizando o índice correspondente.

---

## Como Funciona

- O programa apresenta um menu com três opções principais:
  - `[i]nserir`: Adicionar um item à lista.
  - `[a]pagar`: Apagar um item da lista pelo índice.
  - `[l]istar`: Exibir todos os itens da lista com seus índices.

- O programa valida as entradas do usuário e exibe mensagens de erro amigáveis para ações inválidas, como apagar itens em listas vazias ou fornecer índices inexistentes.

---

## Exemplo de Uso

1. Ao iniciar o programa, será exibido o menu:
Selecione uma opção! [i]nserir [a]pagar [l]istar:

2. Digite `i` para inserir um novo item. Exemplo:
Digite o item para sua Compra: Banana Item Adicionado a Lista

3. Digite `l` para listar os itens da sua lista. Exemplo:
Lista de Itens: 0 Banana

4. Digite `a` para apagar um item pelo índice. Exemplo:
Qual item deseja apagar: 0 Item removido da lista de Compras

5. Caso tente listar ou apagar itens de uma lista vazia, o programa exibirá mensagens apropriadas:
Nenhuma lista encontrada
ou
Nenhum Índice encontrado para remover

---

## Como Usar

1. **Pré-requisitos**:
- Instale o Python 3.x no seu computador. [Baixe aqui](https://www.python.org/).

2. **Clone o repositório**:
```
git clone https://github.com/wandovillar/Lista-De-Compras-Python

Execute o programa:


python Lista-de-Compras.py
Siga as instruções exibidas no terminal para gerenciar sua lista de compras.

Requisitos Técnicos
Sistema Operacional: O comando de limpeza do terminal (cls) funciona apenas no Windows.
Em sistemas baseados em Unix (Linux/MacOS), substitua os.system('cls') por os.system('clear').
Melhorias Futuras
Adicionar a funcionalidade de salvar e carregar a lista em um arquivo.
Implementar suporte para múltiplas listas.
Criar uma interface gráfica simples com bibliotecas como tkinter ou PyQt.
Licença
Este projeto está sob a licença MIT License.

Autor
Desenvolvido por Wando Villar.
