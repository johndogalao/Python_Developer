# O programa tem o objetivo de verificar a idade do usuário

# Declaração de 2 Variáveis

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# Verificação da idade

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

# Para receber um número inteiro em um input, deve-se ser colocado o "int()" antes do "input()".

''' Exemplo: 
        idade = int(input("Digite sua idade: "))'''