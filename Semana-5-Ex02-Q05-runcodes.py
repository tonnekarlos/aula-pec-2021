def maior(n1, n2, n3):
    if n2 < n1 > n3 and n1 > n2 > n3:
        return print(f'{n3}\n{n2}\n{n1}')

    if n2 < n1 > n3 and n1 > n3 > n2:
        return print(f'{n2}\n{n3}\n{n1}')

    elif n1 < n2 > n3 and n2 > n1 > n3:
        return print(f'{n3}\n{n1}\n{n2}')

    elif n1 < n2 > n3 and n2 > n3 > n1:
        return print(f'{n1}\n{n3}\n{n2}')

    elif n2 < n3 > n1 and n3 > n2 > n1:
        return print(f'{n1}\n{n2}\n{n3}')

    elif n2 < n3 > n1 and n3 > n1 > n2:
        return print(f'{n2}\n{n1}\n{n3}')


def main():
    n1 = int(input(""))
    n2 = int(input(""))
    n3 = int(input(""))

    maior(n1, n2, n3)


if __name__ == '__main__':
    main()
