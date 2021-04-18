def verifica_numero(n):
    d = n // 10
    u = n % 10
    return d, u


def main():
    # Entrada de dados
    n = int(input('digite um número entre 10 e 99: ').strip())

    # Processamento
    x = 0
    d, u = verifica_numero(n)

    if 10 <= n <= 99:
        if d % 2 != 0:
            x += 1
        if u % 2 != 0:
            x += 1

        if d % 2 == 0:
            x += 0
        if u % 2 == 0:
            x += 0
        # Saída de dados
        if x == 0:
            print(f'Nenhum dígito é ímpar.')
        elif x == 1:
            print(f'Apenas um dígito é ímpar.')
        elif x == 2:
            print(f'Os dois dígitos são ímpares.')


if __name__ == '__main__':
    main()
