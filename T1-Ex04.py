
def verifica(caractere):
    # ord retorna um número inteiro representa o código Unicode desse caractere.
    digito = ord(caractere)
    # 0 é 48 e 9 é 57
    return 48 <= digito <= 57


print(verifica(input("Digite um caractere: ".strip())))
