import os

# Palavra secreta que o jogador precisa adivinhar
palavra_secreta = "perfume"

# Variáveis para armazenar as letras acertadas e o número de tentativas
letras_acertadas = ""
tentativas = 0

# Conjunto para armazenar as letras que já foram tentadas
letras_tentadas = set()


# Função para limpar a tela de forma compatível com o sistema operacional
def limpar_tela():
    """
    Limpa a tela de comando com base no sistema operacional.
    - Para Windows: usa o comando 'cls'.
    - Para sistemas Unix (Linux, macOS): usa o comando 'clear'.
    """
    sistema = os.name  # Detecta o sistema operacional
    if sistema == "nt":  # Para Windows
        os.system("cls")
    else:  # Para sistemas Unix (Linux, macOS)
        os.system("clear")


# Laço principal do jogo
while True:
    # Solicita que o jogador digite uma letra
    letra = input("Digite uma letra: ").lower()  # Converte a entrada para minúscula

    # Verifica se o jogador digitou mais de uma letra
    if len(letra) > 1:
        print("Digite apenas uma letra!")
        continue  # Solicita a entrada novamente

    # Verifica se a letra já foi tentada anteriormente
    if letra in letras_tentadas:
        print(f"Você já tentou a letra '{letra}'. Tente outra!")
        continue  # Solicita a entrada novamente

    # Adiciona a letra tentada ao conjunto de letras tentadas
    letras_tentadas.add(letra)
    tentativas += 1  # Incrementa o número de tentativas

    # Se a letra estiver na palavra secreta, adiciona à lista de letras acertadas
    if letra in palavra_secreta:
        letras_acertadas += letra

    # Cria a palavra formada até o momento, com '*' nas letras não acertadas
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    # Exibe a palavra formada
    print(palavra_formada)

    # Verifica se o jogador acertou a palavra inteira
    if palavra_formada == palavra_secreta:
        limpar_tela()  # Limpa a tela ao final
        print("Você Ganhou! Parabéns!")
        print(f"A palavra era: {palavra_secreta}")
        print(f"Tentativas: {tentativas}")
        break  # Encerra o jogo
