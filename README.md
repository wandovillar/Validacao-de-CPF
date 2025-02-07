
# 📝 **Validação de CPF** 🧾

Este projeto tem como objetivo validar números de CPF, um documento utilizado no Brasil para identificar cidadãos. O script realiza cálculos para determinar se o número do CPF é válido ou não, com base nos dois dígitos verificadores.

## 🚀 **Funcionalidades**:

1. **Validação de CPF**: 
   - O código recebe o CPF como entrada do usuário.
   - Verifica se o CPF possui caracteres não numéricos e os remove automaticamente.
   - Checa se o CPF não é uma sequência numérica (como 111.111.111-11, que é inválido).
   - Calcula os dois últimos dígitos verificadores e compara com os fornecidos.

2. **Cálculos**:
   - O primeiro e segundo dígitos verificadores são gerados com base em cálculos específicos, utilizando os nove primeiros números do CPF.
   
3. **Saída**:
   - Caso o CPF seja válido, o sistema retorna "CPF Válido!".
   - Caso contrário, informa "CPF Inválido!".

## ⚙️ **Como usar**:

### 1️⃣ **Clone o repositório**:

```bash
git clone https://github.com/wandovillar/Validacao-de-CPF.git
```

### 2️⃣ **Navegue até o diretório do projeto**:

```bash
cd Validacao-de-CPF
```

### 3️⃣ **Execute o script Python**:

```bash
python validacao-de-cpf.py
```

O script irá pedir para digitar um CPF e, em seguida, mostrar se ele é válido ou não. 😎

---

## 📂 **Estrutura do Projeto**:

```
Validacao-de-CPF/
│
├── validacao-de-cpf.py     # Arquivo principal contendo o script de validação
├── README.md               # Este arquivo README
└── .git/                   # Diretório de configuração do Git
```

---

## 🔨 **Como funciona o código?**:

O código segue a lógica padrão de validação de CPF. O fluxo principal é:

1. O CPF é limpo de caracteres não numéricos.
2. Verifica-se se o CPF é uma sequência de números repetidos (exemplo: 111.111.111-11).
3. São feitos os cálculos para verificar os dois últimos dígitos do CPF.
4. Caso os cálculos confiram com os dígitos fornecidos, o CPF é considerado válido.

Veja o exemplo do código para o cálculo do primeiro dígito:

```python
resultado_digito_1 = 0
contador_regressivo_1 = 10
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
```

Neste exemplo, o CPF é validado de forma que o primeiro dígito seja calculado e comparado com o dado pelo usuário. O mesmo processo é repetido para o segundo dígito.

---

## 💡 **Melhorias Futuras**:

- Adicionar validação para formatos diferentes de entrada (com ou sem pontuação).
- Implementar uma interface gráfica simples (GUI) para maior interação.
- Adicionar testes automatizados para garantir a precisão do algoritmo.

---

## 🔧 **Tecnologias utilizadas**:

- **Python**: Linguagem utilizada para o desenvolvimento do script.
- **Regex**: Para limpar o CPF de caracteres não numéricos.

---

## 🎉 **Contribuições**:

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork e enviar um pull request. 🛠️

---

## 📬 **Contato**:

Para dúvidas ou sugestões, entre em contato comigo:
- **E-mail**: [wandovilar@outlook.com](mailto:wandovilar@outlook.com)

---

## 🎯 **Objetivo do Projeto**:

Esse projeto é um exercício simples, mas eficiente, de validação de dados. Ele foi feito como aprendizado para aprofundar os conhecimentos em Python e em como realizar manipulação de strings, cálculos e validações.
