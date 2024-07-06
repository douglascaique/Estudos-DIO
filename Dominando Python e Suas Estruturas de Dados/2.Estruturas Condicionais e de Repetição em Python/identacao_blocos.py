saldo = 500


def sacar(valor):

    if saldo >= valor:
        print('Saque efetuado com sucesso!')
    else:
        print('Valor inválido!')
        print('Por favor, tente novamente!')
        sacar(int(input('Digite o valor do saque: ')))


sacar(int(input('Digite o valor do saque: ')))