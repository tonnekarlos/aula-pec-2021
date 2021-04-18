# Processamento
def imc(m, a):
    return m / (a*a)


def main():
    # Entrada de dados
    m = float(input('Digite seu peso: ').strip())
    a = float(input('Digite sua altura: ').strip())

    # Processamento e saída de dados
    if 18.5 > imc(m, a):
        print(f'{imc(m,a):.1f}\nAbaixo do peso')
    elif 25 > imc(m, a):
        print(f'{imc(m,a):.1f}\nPeso normal')
    elif 30 > imc(m, a):
        print(f'{imc(m,a):.1f}\nSobrepeso')
    elif 35 > imc(m, a):
        print(f'{imc(m,a):.1f}\nObeso leve')
    elif 40 > imc(m, a):
        print(f'{imc(m,a):.1f}\nObeso moderado')
    elif 40 <= imc(m, a):
        print(f'{imc(m,a):.1f}\nObeso mórbido')


if __name__ == '__main__':
    main()
