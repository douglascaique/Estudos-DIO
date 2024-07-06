MAIOR_IDADE = 18
IDADE_ESPECIAL = 14

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade. Pode tirar a CNH.')
elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
    print('Você é um adolescente. Pode ter aula teóricas.')
else:
    print('Você é menor de idade. Não pode tirar a CNH.')