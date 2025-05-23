# O sistema deve verificar a altura e idade do indivíduo e libera-lo se tiver a idade e altura mínima, ou, bloquea-lo se não se enquadrar na altura e idade mínima.

# Declaração de variáveis

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
altura = float(input("Digite sua Altura: ").replace(",",".")) # o replace vê se o usuário usou virgula e troca para um ponto.

# Verificação

if idade >= 12 and altura >= 1.10:
    print(f"A entrada de {nome} foi autorizada!")
else:
    print(f"A entrada de {nome} foi negada!")
