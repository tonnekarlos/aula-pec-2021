# Processamento
def media(n1, n2, n3, n4, n5):
    return(n1+n2+n3+n4+n5) / 5


def main():
    # Entrada de dados
    n1 = float(input("Primeiro número: ".strip()))
    n2 = float(input("Segundo número: ".strip()))
    n3 = float(input("Terceiro número: ".strip()))
    n4 = float(input("Quarto número: ".strip()))
    n5 = float(input("Quinto número: ".strip()))

    # Processamento
    maior = []
    if n1 > media(n1, n2, n3, n4, n5):
        maior.append(n1)
    if n2 > media(n1, n2, n3, n4, n5):
        maior.append(n2)
    if n3 > media(n1, n2, n3, n4, n5):
        maior.append(n3)
    if n4 > media(n1, n2, n3, n4, n5):
        maior.append(n4)
    if n5 > media(n1, n2, n3, n4, n5):
        maior.append(n5)

    # Saída de dados
    print(f'A média é: {media(n1,n2,n3,n4,n5):.2f}')
    for item in maior:
        print('{:.2f} é maior que a média'.format(item))


if __name__ == '__main__':
    main()
