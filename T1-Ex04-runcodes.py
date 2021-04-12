# Processamento de dados:
def verifica(caractere):
    digito = ord(caractere)
    # 0 é 48 e 9 é 57
    return 48 <= digito <= 57


# entrada e saída de dados
print(verifica(input()))
