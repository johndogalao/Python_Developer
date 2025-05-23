# um programa que receberá do usuário 2 números reais, e o usuário irá escolher uma das 4 operações básicas da matemática. O programa irá calcular com base na escolha do usuário e formar o resultado.

# Declaração de Variáveis

x = float(input("Informe o valor de x: ").replace(",","."))
y = float(input("Informe o valor de y: ").replace(",","."))

# menu

print(f"{'-'*20} CALCULADORA PYTHON {'-'*20}")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Coleta o tipo de operação que o usuário deseja e armazena na variável

print(f"{'-'*60}") # linha de '-' para separar

operador = input("Informe a opção desejada: ")

print(f"{'-'*60}")

# Faz a conta com base na opção escolhida pelo usuário

match operador:
    case "1":
        print(f"O resultado da soma é: {x + y}")
    case "2":
        print(f"O resultado da Subtração é {x - y}")
    case "3":
        print(f"O resultado da Multiplicação é {x * y}")
    case "4":
        print(f"O resultado da Divisão é {x / y}")
    case _:
        print("Operador inválido")
