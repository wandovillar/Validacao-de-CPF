import re
import sys

# Recebe e limpa a entrada
entrada = re.sub(r"[^0-9]", "", input("Digite número do seu CPF: "))

# Verifica se a entrada é vazia
if not entrada:
    print("Entrada inválida. Por favor, insira apenas números.")
    sys.exit()

# Verifica se todos os caracteres são iguais (sequencial)
entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print("Você mandou dados sequenciais")
    sys.exit()

# Gerando Primeiro Dígito
nove_digitos = entrada[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Gerando Segundo Dígito
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# CPF Gerado
cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"
print(f"CPF gerado: {cpf_gerado_pelo_calculo}")
