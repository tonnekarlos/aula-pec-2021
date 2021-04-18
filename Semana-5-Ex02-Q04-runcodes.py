def signo(dia, mes):
    if 21 <= dia <= 31 and mes == 3 or 1 <= dia <= 19 and mes == 4:
        print("Áries")
    elif 20 <= dia <= 31 and mes == 4 or 1 <= dia <= 20 and mes == 5:
        print("Touro")
    elif 21 <= dia <= 31 and mes == 5 or 1 <= dia <= 21 and mes == 6:
        print("Gêmeos")
    elif 22 <= dia <= 31 and mes == 6 or 1 <= dia <= 22 and mes == 7:
        print("Câncer")
    elif 23 <= dia <= 31 and mes == 7 or 1 <= dia <= 22 and mes == 8:
        print("Leão")
    elif 23 <= dia <= 31 and mes == 8 or 1 <= dia <= 22 and mes == 9:
        print("Virgem")
    elif 23 <= dia <= 31 and mes == 9 or 1 <= dia <= 22 and mes == 10:
        print("Libra")
    elif 23 <= dia <= 31 and mes == 10 or 1 <= dia <= 21 and mes == 11:
        print("Escorpião")
    elif 22 <= dia <= 31 and mes == 11 or 1 <= dia <= 21 and mes == 12:
        print("Sagitário")
    elif 22 <= dia <= 31 and mes == 12 or 1 <= dia <= 19 and mes == 1:
        print("Capricórnio")
    elif 20 <= dia <= 31 and mes == 1 or 1 <= dia <= 18 and mes == 2:
        print("Aquário")
    elif 19 <= dia <= 31 and mes == 2 or 1 <= dia <= 20 and mes == 3:
        print("Peixes")


def main():
    dia = int(input('').strip())
    mes = int(input('').strip())

    signo(dia, mes)


if __name__ == '__main__':
    main()
