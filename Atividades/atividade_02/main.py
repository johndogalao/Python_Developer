# crie um prgrama que receba o nome do usuário e informe o menu abaixo:
# Sala 1 - A Roda Quadrada - Livre
# Sala 2 - A Volta dos que não foram - 12 Anos
# Sala 3 - Poeira em Alto mar - 14 Anos
# Sala 4 - As tranças do rei Careca - 16 Anos
# Sala 5 - A Vingança do Frango Assado - 18 Anos

# O usuário usuario vai escolher a sala do filme que deseja assistir, e o programa deverá:
# - Liberar a entrada do usuário e encerrar, caso o usuario tenha a idade mínima ou maior.
# - Bloquear a entrada se o usuário não possuir a idade mínima da sala escolhida

try:
    while True:
        nome = input("Digite seu Nome: ")
        idade = int(input("Digite sua Idade: "))



        print(f'-'*20, "CINEMA DO JÃO", '-'*20)
        print("1 - A Roda Quadrada (Idade min. Livre)")
        print("2 - A Volta dos que não foram (Idade min. 12+ anos)")
        print("3 - Poeira em Alto mar (Idade min. 14+ anos)")
        print("4 - As tranças do rei Careca (Idade min. 16+ anos)")
        print("5 - A Vingança do Frango Assado (Idade min. 18+ anos)")
        print(f'-'*53)

        escolha = int(input("Escolha o Núumero da Sala Desejada: "))
        print('-'*53)

        if idade >= 18 and escolha > 0 and escolha < 5:
             print(f"Compra Realizada com sucesso! aproveite")
        elif escolha == 5 and idade < 18:
             print("Idade Mínima Negada!")
        elif escolha == 4 and idade >= 16:
             print("Compra Realizada com sucesso!")
        elif escolha == 4 and idade < 16:
             print("Idade Mínima Negada!")
        elif escolha == 3 and idade >= 14:
             print("Compra Realizada com sucesso!")
        elif escolha == 3 and idade < 14:
             print("Idade Mínima Negada!")
        elif escolha == 2 and idade >= 12:
             print("Compra Realizada com sucesso!")
        elif escolha == 2 and idade < 12:
             print("Idade Mínima Negada!")
        elif escolha == 1:
             print("Compra Realizada com Sucesso!")
        else:
             print("Número de Sala Inválido")
          
        print('-'*53)

        voltar = input("Deseja Realizar outra Compra? (s/n) ").lower().strip()

        print('-'*53)

        if voltar != "s":
             print(f"Obrigado pela Preferência {nome}!")
             break
        else:
             print("Ok, reiniciando")
        
except Exception as e:
        print(f"error: {e}")
