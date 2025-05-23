'''
Crie um programa que receba um nome, o peso e a altura do usuário e informe seu IMC, e informe seu diagnóstico de acordo com seu IMC -Magro demais
- Peso normal
- Obeso
- Obesidade nivel II
- Obesidade mórbida
'''

try:
    while True:
        print('-'*20, "Calculadora de IMC", '-'*20)
        peso = float(input("Digite seu Peso: ").replace(',','.'))
        print('-'*20)
        altura = float(input("Digite sua Altura: ").replace(',','.'))
        print('-'*20)

        calculo = round(peso / (altura * altura), 1)

        if calculo < 18.5:
            print(f"Seu IMC é de {calculo}, portanto, seu diagnóstico é Magreaza Escessiva")

        elif calculo >= 18.5 and calculo <= 24.9:
            print(f"Seu IMC é de {calculo}, portanto, seu diagnóstico é Pessoa Saudável")

        elif calculo >= 25 and calculo <= 29.9:
            print(f"Seu IMC é de {calculo}, portanto, seu diagnóstico é Obesidade")

        elif calculo >= 30 and calculo <= 34.9:
            print(f"Seu IMC é de {calculo}, portanto, seu diagnóstico é Obesidade II")

        elif calculo > 35:
            print(f"Seu IMC é de {calculo}, portanto, seu diagnóstico é Obesidade Mórbida")
            
        else:
            print("Valor Inválido")

        voltar = input("Deseja Fazer outro Cálculo? (s/n) ").lower().strip()
        if voltar != "s":
            print("Até a Próxima!")
            break

except Exception as e:
    print(f"error: {e}")
