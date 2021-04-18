def calculo_idade(ano, anon):
    return ano-anon


def ano_atual_e_nasc(dian, dia, mesn, mes, ano, anon):
    if (mesn >= mes) and (dian >= dia):
        return calculo_idade(ano, anon)

    elif (mesn <= mes) and (dian < dia):
        return (calculo_idade(ano, anon)-1)


def main():

    dia = int(input("".strip()))
    mes = int(input("".strip()))
    ano = int(input("".strip()))

    dian = int(input("".strip()))
    mesn = int(input("".strip()))
    anon = int(input("".strip()))

    print(f'{ano_atual_e_nasc(dia, dian, mes, mesn, ano, anon)}')


if __name__ == '__main__':
    main()
