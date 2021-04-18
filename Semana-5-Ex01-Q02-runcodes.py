def data1(dia1, mes1, ano1):
    return print(f'{dia1}/{mes1}/{ano1}')


def data2(dia2, mes2, ano2):
    return print(f'{dia2}/{mes2}/{ano2}')


def data_recente(dia1, dia2, mes1, mes2, ano1, ano2):
    if ano1 > ano2:
        return data1(dia1, mes1, ano1)

    elif ano2 > ano1:
        return data2(dia2, mes2, ano2)

    elif ano1 == ano2 and mes1 > mes2:
        return data1(dia1, mes1, ano1)

    elif ano1 == ano2 and mes2 > mes1:
        return data2(dia2, mes2, ano2)

    elif ano1 == ano2 and mes1 == mes2 and dia1 > dia2:
        return data1(dia1, mes1, ano1)

    elif ano1 == ano2 and mes1 == mes2 and dia2 > dia1:
        return data2(dia2, mes2, ano2)
    else:
        return data1(dia1, mes1, ano1)


def main():

    dia1 = int(input("".strip()))
    mes1 = int(input("".strip()))
    ano1 = int(input("".strip()))

    dia2 = int(input("".strip()))
    mes2 = int(input("".strip()))
    ano2 = int(input("".strip()))

    data_recente(dia1, dia2, mes1, mes2, ano1, ano2)


if __name__ == '__main__':
    main()
