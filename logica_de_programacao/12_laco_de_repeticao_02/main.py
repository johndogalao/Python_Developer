# laço de repetição

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Diite sua idade: "))

    result = "é maior de idade." if idade >= 18 else "é menor de idade."

    print(nome, result)

    repetir = input("Deseja verificar de novo? (s/n) ").lower().strip()
    match repetir:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Operação Inválida")
            break
