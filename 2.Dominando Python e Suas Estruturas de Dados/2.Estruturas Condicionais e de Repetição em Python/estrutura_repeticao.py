# texto = input('Informe um texto: ')
VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# print()


# for numero in range(0, 11):
    # print(numero, end=" ")

# for numero in range(0, 51, 5):
#     print(numero, end=" ")

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
print('Obrigado por utilizar nosso sistema!')