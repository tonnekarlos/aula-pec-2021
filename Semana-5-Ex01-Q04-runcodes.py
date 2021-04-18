def media(n1, n2, n3, n4, n5):
    return(n1+n2+n3+n4+n5) / 5


def main():
    n1 = float(input("".strip()))
    n2 = float(input("".strip()))
    n3 = float(input("".strip()))
    n4 = float(input("".strip()))
    n5 = float(input("".strip()))
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

    print(f'{media(n1,n2,n3,n4,n5):.2f}')
    for item in maior:
        print('{:.2f}'.format(item))


if __name__ == '__main__':
    main()
