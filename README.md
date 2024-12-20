# Jogo da Palavra Secreta

## Descrição

O projeto é um simples jogo da "Palavra Secreta", onde o jogador deve adivinhar a palavra secreta, uma letra por vez. O programa revela as letras corretas conforme o jogador acerta e oculta as letras incorretas com asteriscos ("*").

## Como Funciona

1. O programa começa com uma palavra secreta definida (no caso, "perfume").
2. O jogador digita uma letra de cada vez.
3. Se a letra estiver na palavra secreta, ela é adicionada à lista de letras acertadas e a palavra formada é atualizada.
4. Se o jogador errar, ele deve continuar tentando até que adivinhe a palavra inteira.
5. O número de tentativas é contabilizado e, ao final, o programa exibe a palavra correta e o número de tentativas feitas.

## Requisitos

- Python 3.x

## Como Usar

1. Clone este repositório para o seu computador:
    ```bash
    git clone https://github.com/wandovillar/Palavra-Secreta.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Palavra-Secreta
    ```
3. Execute o script Python:
    ```bash
    python Palavra_Secreta.py
    ```
4. Comece a digitar letras para adivinhar a palavra secreta!

## Exemplo de Execução

```plaintext
Digite uma letra: p
p*****
Digite uma letra: e
pe****
Digite uma letra: r
per***
Digite uma letra: f
perf**
Digite uma letra: u
perfume
Você Ganhou Parabéns!
A palavra era,  perfume
Tentativas:  5
```


## Como Funciona o Código
O código define uma palavra secreta e pede ao usuário para inserir uma letra a cada vez. O programa verifica se a letra faz parte da palavra secreta e atualiza o estado da palavra mostrada para o usuário, substituindo as letras não acertadas por asteriscos. O jogo termina quando o usuário adivinha todas as letras da palavra.

## Licença
Este projeto está licenciado sob a MIT License.



Agora, com esse conteúdo, basta você adicionar o arquivo README.md ao seu repositório e fazer o commit e push:

```bash
git add README.md
git commit -m "Adicionando README explicativo"
git push origin main
