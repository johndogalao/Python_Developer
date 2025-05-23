# Crie um programa que receba do usuário dois números reais, e uma das 4 operações básicas da matemática, e faça o cálculo

while True:
    try:

        print('-'*20, "Calculadora", '-'*20)
        print("0 - Sair do Programa")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        print('-'*53)

        operador = int(input("Digite a Opção desejada: "))

        match operador:
            case 0:
                print("Até a Próxima!")
                break
            case 1:
                n1 = int(input("Digite o valor de X: "))
                n2 = int(input("Digite o valor de Y: "))
                print(f"A Soma entre {n1} e {n2} é {n1 + n2}")
            case 2:
                n1 = int(input("Digite o valor de X: "))
                n2 = int(input("Digite o valor de Y: "))
                print(f"A Subtração entre {n1} e {n2} é {n1 - n2}")
            case 3:
                n1 = int(input("Digite o valor de X: "))
                n2 = int(input("Digite o valor de Y: "))
                print(f"A Miltiplicação entre {n1} e {n2} é {n1 * n2}")
            case 4:
                n1 = int(input("Digite o valor de X: "))
                n2 = int(input("Digite o valor de Y: "))
                print(f"A Divisão entre {n1} e {n2} é {n1 / n2}")
            case _:
                print("Impossível concluir a operação")

        voltar = input("Deseja Fazer outra operação? (s/n) ").lower().strip()
        if voltar != "s":
            print("Até a Próxima")
            break

    except Exception as e:
        print(f"Erro inesperado. error: {e}")
