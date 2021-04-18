def main():
    nome = input('')
    estado_civil = int(input(''))
    n1 = []
    n2 = []
    if estado_civil == 2:
        n1.append(nome)
        for i in n1:
            print(len(i))
    elif estado_civil == 1:
        nome2 = input('')
        n1.append(nome)
        n2.append(nome2)
        for i in n1:
            for w in n2:
                print(len(i) + len(w))


if __name__ == '__main__':
    main()
