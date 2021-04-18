# Processamento
def maior(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        return n5


def menor(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return n1
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return n2
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return n3
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return n4
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        return n5


def main():
    # Entrada de dados
    n1 = int(input("Primeiro número: ".strip()))
    n2 = int(input("Segundo número: ".strip()))
    n3 = int(input("Terceiro número: ".strip()))
    n4 = int(input("Quarto número: ".strip()))
    n5 = int(input("Quinto número: ".strip()))

    # Saída de dados
    print(f'{maior(n1, n2, n3, n4, n5)} é o maior número')
    print(f'{menor(n1, n2, n3, n4, n5)} é o menor número')


if __name__ == '__main__':
    main()
