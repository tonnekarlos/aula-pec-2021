
def sinal(cor):
    if cor.upper() == 'V':
        return 'Siga'
    elif cor.upper() == 'A':
        return 'Atenção'
    elif cor.upper() == 'E':
        return 'Pare'


def main():
    # Entrada de dados
    digite_cor = input('')


# Processamento chamando a função
    resultado = sinal(digite_cor)


# Saida de dados
    print(f'{resultado}')


if __name__ == '__main__':
    main()
