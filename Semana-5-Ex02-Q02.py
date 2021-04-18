def des_num(n):
    u = n % 10
    n1 = n//10
    d = n1 % 10
    c = n1//10
    return c, d, u


def main():
    # Entrada de dados
    n = int(input('Digite um número entre 10 e 999: ').strip())

    # Processamento
    c, d, u = des_num(n)
    x = 0

    if 100 <= n <= 999 and c % 2 == 0:
        x += 1
    if 100 <= n <= 999 and d % 2 == 0:
        x += 1
    if 100 <= n <= 999 and u % 2 == 0:
        x += 1
        # Saída de dados
        print(f'{x}')

    if 100 <= n <= 999 and c % 2 != 0:
        x += 0
    if 100 <= n <= 999 and d % 2 != 0:
        x += 0
    if 100 <= n <= 999 and u % 2 != 0:
        x += 0
        # Saída de dados
        print(f'{x}')

    else:
        x += 0


if __name__ == '__main__':
    main()
