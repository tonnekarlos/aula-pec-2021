# ENTRADA DE DADOS:
nome = str(input("Digite seu nome: ".strip()))
print("Diga qual é o seu sexo .\n Digite:.\n 1- Masculino .\n 2- Feminino")
sexo = int(input("Digite: ".strip()))

# PROCESSAMENTO E SAIDA

if sexo == 1:
    print(f'Ilmo Sr.{nome}')

elif sexo == 2:
    print(f'Ilmo Sra. {nome}')

else:
    print("Número incorreto")
