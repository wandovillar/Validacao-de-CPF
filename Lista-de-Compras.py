import os  # Biblioteca para executar comandos do sistema, como limpar o terminal

# Inicializando uma lista vazia para armazenar os itens
lista = []

# Loop infinito para o menu interativo
while True:
    print("Selecione uma opção!")  # Exibe as opções disponíveis para o usuário
    menu = input(
        "[i]nserir [a]pagar [l]istar: "
    ).lower()  # Solicita ao usuário que escolha uma opção

    # Verifica se o usuário digitou uma opção inválida
    if menu not in ["i", "a", "l"]:  # Aqui foi corrigida a condição de validação
        print("Digite uma opção válida")  # Alerta ao usuário que a opção é inválida
        continue  # Volta para o início do loop sem executar mais nada

    # Opção para inserir itens na lista
    if menu == "i":
        os.system("cls")  # Limpa o terminal (no Windows)
        item = input(
            "Digite o item para sua Compra: "
        ).upper()  # Solicita o nome do item e o converte para maiúsculas
        lista.append(item)  # Adiciona o item à lista
        print("Item Adicionado a Lista")  # Confirma a adição do item

    # Opção para apagar itens da lista pelo índice
    elif menu == "a":
        if lista:  # Verifica se a lista não está vazia
            try:
                # Solicita o índice do item a ser apagado e converte para inteiro
                indice = int(input("Qual item deseja apagar: "))
                # Verifica se o índice está dentro do intervalo válido
                if (
                    0 <= indice < len(lista)
                ):  # Alterado para incluir o índice 0 como válido
                    lista.pop(
                        indice
                    )  # Remove o item correspondente ao índice fornecido
                    print("Item removido da lista de Compras")  # Confirma a remoção

                else:
                    print(
                        "Índice da Lista não Existe"
                    )  # Mensagem de erro para índices inválidos
            except ValueError:
                # Mensagem de erro caso o usuário digite algo que não seja um número
                print("Digite um Índice da lista válido")

        else:
            print(
                "Nenhum Índice encontrado para remover"
            )  # Mensagem caso a lista esteja vazia

    # Opção para listar todos os itens na lista
    elif menu == "l":
        os.system("cls")  # Limpa o terminal (no Windows)
        if lista:  # Verifica se a lista não está vazia
            print("\n Lista de Itens:")  # Exibe o título da lista
            # Exibe cada item da lista com seu índice correspondente
            for indice, nome in enumerate(lista):
                print(indice, nome)

        else:
            print("Nenhuma lista encontrada")  # Mensagem caso a lista esteja vazia
