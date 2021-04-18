def main():
    # Entrada de dados
    nome = input('Digite seu nome: ')
    estado_civil = int(
        input('Digite seu estado civil:\n 1 - Casado\n 2 - Solteiro\n '))

    # Processamento
    n1 = []
    n2 = []
    if estado_civil == 2:
        n1.append(nome)
        for i in n1:

            # Saída de dados
            print(len(i))
    elif estado_civil == 1:

        # Entrada de dados
        nome2 = input('Digite o nome do cônjuge: ')

        # Processamento
        n1.append(nome)
        n2.append(nome2)
        for i in n1:
            for w in n2:
                # Saída de dados
                print(len(i) + len(w))


if __name__ == '__main__':
    main()
