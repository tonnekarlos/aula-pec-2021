# Processamento
def calculo_idade(ano, anon):
    return ano-anon


def ano_atual_e_nasc(dian, dia, mesn, mes, ano, anon):
    if (mesn >= mes) and (dian >= dia):
        return calculo_idade(ano, anon)

    elif (mesn <= mes) and (dian < dia):
        return (calculo_idade(ano, anon)-1)


def main():

    # Entrada de dados
    print("Digite a data atual conforme solicitada a seguir")
    dia = int(input("Digite o dia: ".strip()))
    mes = int(input("Digite o mes: ".strip()))
    ano = int(input("Digite o ano: ".strip()))

    print("Digite a data de nascimento conforme solicitada a seguir")
    dian = int(input("Digite o dia: ".strip()))
    mesn = int(input("Digite o mes: ".strip()))
    anon = int(input("Digite o ano: ".strip()))

    # Saída de dados
    print(
        f'Sua idade é: {ano_atual_e_nasc(dia, dian, mes, mesn, ano, anon)} anos')


if __name__ == '__main__':
    main()
