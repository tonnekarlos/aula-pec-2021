# Processamento de dados:
def e_vogal(c):
    return c.lower() in 'aeiou'


def e_letra(c):
    return c.lower() in 'aeioubcdfghklmnpqrstwxyz'


def e_consoante(c):
    return e_letra(c) and (not e_vogal(c))


def e_numero(c):
    return c in '0123456789'


def e_letra_ou_numero(c):
    return e_letra(c) or e_numero(c)


def e_simbolo(c):
    return (not e_letra_ou_numero(c))


def main():
    # Entrada de dados
    caractere = input('Digite um caractere:'.strip())
    # Saída de dados:
    if e_vogal(caractere):
        print('vogal')
    elif e_consoante(caractere):
        print('consoante')
    elif e_numero(caractere):
        print('número')
    elif e_simbolo(caractere):
        print('símbolo')


if __name__ == '__main__':
    main()
