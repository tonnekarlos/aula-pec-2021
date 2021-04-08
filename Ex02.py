
valor = float(input('valor da geladeira: '))
#
desconto = float(input('Percentual do desconto: '))
#
fator = 1 - desconto / 100
#
valor = valor * fator
#
print(f'A geladeira com {desconto:.0f}% de desconto fica por {valor:.2f}')

answer = input('Run again?(y/n) : ')
if answer == 'y':

    if answer == 'n':
        SystemExit
