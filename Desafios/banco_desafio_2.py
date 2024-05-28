menu = """
[u] Novo Usuario
[n] Nova Conta

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
customers = []
checking_accounts = []
branch = "0001"



def withdrawals(*, balance, value, statement, limit, withdrawals_count, WITHDRAWAL_LIMIT):
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
          
    return balance, withdrawals_count, statement
    
def deposit(value, balance, statement, /):
    if value > 0:
        balance += value
        statement += "Depósito   | R$ {:.2f}\n".format(value)
    else:
        print("Operação falhou! O valor informado é inválido.")
    return balance, statement

def record():
    print("\n================ EXTRATO ================")
    if not statement:
        print("Não foram realizadas movimentações.")
    else:        
        print("Tipo       | Valor\n" + "-"*25)
        print(statement)
    print("Saldo: R$ {:.2f}".format(balance))
    print("==========================================")

def new_user(customers):
    name = (input("Nome do usuário: "))
    birth = (input("Data de Nascimento: "))
    number_CPF = (input("CPF: "))
    city = input("Cidade: ")
    
    for customer in customers:
        if customer["CPF"] == number_CPF:
            print("****Erro: CPF já cadastrado!*****")
            return
    
    customer = {
        "nome": name,
        "data_nascimento": birth,
        "CPF": number_CPF,
        "cidade": city        
    }
    
    customers.append(customer)
    
    print("Usuário cadastrado com sucesso!")
    
    return customers

def create_account(customers, checking_accounts, branch):
    cpf = input("Digite o CPF do cliente para o qual deseja criar a conta: ")
    
    customer_found = False
    for customer in customers:
        if customer["CPF"] == cpf:
            customer_found = True
            break
        
    if not customer_found:
        print("Erro: Cliente não encontrado.")
        return
    
    account_number = len(checking_accounts) + 1
    
    account = {
        "agencia": branch,
        "numero_conta": account_number,
        "cliente": cpf
    }
    
    checking_accounts.append(account)

    print(f"Conta criada com sucesso para o cliente com CPF: {cpf}.")
    return customers, checking_accounts
    
     
while True:

    option = input(menu)

    if option == "d":
        value = float(input("Informe o valor do depósito: "))
        balance, statement = deposit(value, balance, statement)
        
    elif option == "s":
        value = float(input("Informe o valor do saque: "))
        balance, withdrawals_count, statement = withdrawals(balance=balance, value=value, statement=statement, limit=limit, withdrawals_count=withdrawals_count, WITHDRAWAL_LIMIT=WITHDRAWAL_LIMIT)
        
    elif option == "e":
        record()

    elif option == "q":
        break
    
    elif option == "u":
        new_user(customers)
        
    elif option == "n":
        create_account(customers, checking_accounts, branch)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
 