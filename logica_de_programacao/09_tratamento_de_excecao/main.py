# O tratamento de exceção tenta com certeza executar o primeiro código, mas se der errado ele faz outra coisa.

try:
    numero = int(input("Informe um número interiro:")) # pede para o usuário informar um número

    print(f"o número é {numero}") # imprime o número

except Exception as e: # se o programa der erro
    print(f"Não foi possível concluir a operação, erro: {e}") # exibe essa mensagem, com o erro (e)

finally:
    print('Programa Encerrado') # Mostra uma mensagem de encerramento do programa, indepedente do programa der certo ou não.
