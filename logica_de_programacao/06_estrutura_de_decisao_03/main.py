# um programa que calcula se o aluno está reprovado, aprovado ou de recuperação, com base na média.

# Declaração de Variáveis

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: ").replace(",","."))

# Verificação

if media >= 0 and media <= 10:
    if media >= 7:
        print(f"O aluno {nome} está aprovado")
    elif media >= 5:
        print(f"O alno {nome} está de recuperação")
    else:
        print(f"O aluno {nome} está reprovado")
else:
    print("Valor inválido")
