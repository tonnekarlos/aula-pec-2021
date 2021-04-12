def n_par(n1):
    return n1 % 2 == 0


def main():
    # Entrada de dados
    n1 = int(input("Digite um numero: "))


# Saida de dados
    if n_par(n1):
        print(False)
    else:
        print(True)


if __name__ == '__main__':
    main()
