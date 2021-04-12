def main():
    soma_nota = 0
    media_nota = 0
# Entrada de dados
    for p in range(1, 4):
        nota = float(input(''.strip()))
        # Processamento de dados
        soma_nota += nota
        media_nota = soma_nota / 3
        if p == 3 and nota > 8:
            media_nota += 1
# Saida de dados
    if media_nota <= 10:
        print(f'{media_nota:.2f}')

    if media_nota > 10:
        media_nota = 10
        print(f'{media_nota:.2f}')


# Chama a função main
if __name__ == '__main__':
    main()
