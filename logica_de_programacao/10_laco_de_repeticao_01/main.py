# o usuário deve informar um número inteiro positivo
# o programa imprime uma contagem de números até chegar a 0
# o programa é interrompido

# Declaração de Variáveis

try:
    n = int(input("Digite um número inteiro positivo: "))

    while n >= 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"Não Foi possível fazer a Contagem. Erro: {e}")
finally:
    print("Programa encerrado.")
