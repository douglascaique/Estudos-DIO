menu = """
-----------------------------------
    Bem-vindo ao Banco do Dev
-----------------------------------
Escolha sua opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor >= 0:
            saldo += valor
            extrato += f"  Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if saldo - valor >= 0:
                saldo -= valor
                extrato += f"  Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários atingido.")
    elif opcao == "e":
        print(f"Saldo: R$ {saldo:.2f}")
        print("Extrato:")
        print(extrato)
    elif opcao == "x":
        break
