def main():
    soma_nota = 0
    media_nota = 0

# Entrada de dados

    # for cria um ciclo com uma lista de 1 a 3 referente a nota 1 a nota 3
    for p in range(1, 4):
        print('==========={}ª NOTA ========'.format(p))
        # Variavel nota recebe valor digitado pelo o usuário
        nota = float(input('Digite: '.strip()))

 # Processamento de dados
        # A variavel soma_nota soma as notas digitada ate finalizar o ciclo
        soma_nota += nota
        # A variável media_nota faz a divisão da var. soma_nota (soma das notas) por 3
        media_nota = soma_nota / 3
        # Se a Terceira nota digitada for maior que 8 soma-se + 1 a variável media_nota
        if p == 3 and nota > 8:
            media_nota += 1

# Saída de dados:
    # Se a var. media_nota(media das notas) for menor ou igual a 10 mostre na tela a média para o usuário
    if media_nota <= 10:
        print(f'A média é {media_nota:.2f}')

    # Se a var. media_nota(media das notas) for maior que 10 media será ajustada(media_nota recebe 10) e vai ser 10 mostre na tela a média para o usuário
    if media_nota > 10:
        media_nota = 10
        print(f'Média: {media_nota:.2f}')


# chama a função main
if __name__ == '__main__':
    main()
