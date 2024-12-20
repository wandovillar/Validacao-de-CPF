import os

palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

while True:

    letra = input("Digite uma letra: ")
    tentativas += 1

    if len(letra) > 1:
        print("Digite apenas uma letra !")
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Você Ganhou Parabéns!")
        print("A palavra era, ", palavra_secreta)
        print(" Tentativas: ", tentativas)
