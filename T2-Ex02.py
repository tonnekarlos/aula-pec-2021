# Processamento de dados
def verifica(caractere):
    # ord retorna um número inteiro representa o código Unicode desse caractere.
    digito = ord(caractere)
    # 65 a 90 corresponde (A a Z) e 97 a 122 corresponde a (a ate z)
    return 65 <= digito <= 90 or 97 <= digito <= 122


# Entrada e saida de dados
print(verifica(input("Digite um caractere: ".strip())))


#print(chr(65, 90))
# 97 122
