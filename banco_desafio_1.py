menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
statement = ""
withdrawals_count = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("Qual valor do depósito?: "))

        if value > 0:
            balance += value
            statement += "Depósito   | R$ {:.2f}\n".format(value)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "s":
        value = float(input("Qual valor do saque?: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawals = withdrawals_count >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operação falhou! Saldo suficiente.")

        elif exceeded_limit:
            print("Operação falhou! Valor do saque excede o limite.")

        elif exceeded_withdrawals:
            print("Operação falhou! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            statement += "Saque      | R$ {:.2f}\n".format(value)
            withdrawals_count += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "e":
        print("\n================ EXTRATO ================")
        if not statement:
            print("Não foram realizadas movimentações.")
        else:        
            print("Tipo       | Valor\n" + "-"*25)
            print(statement)
        print("Saldo: R$ {:.2f}".format(balance))
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")