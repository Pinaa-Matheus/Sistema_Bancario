#### Variaveis ####

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
AGENCIA = "0001"

####################

def menu():
    return input("""
========= MENU =========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Contas
[0] Sair
========================
Escolha: """)


def cadastrar_usuario(usuarios):
    nome = input("Nome: ").strip() 
    cpf = input("CPF (somente números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf)) #Chequando se tem alguma letra

    if len(cpf) != 11: #Verificando se ha espaços 
        print("CPF inválido! Contate nosso suporte.")
        return usuarios

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nJá existe um usuário cadastrado com esse CPF!")
            return usuarios

    nascimento = input("Nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço: ").strip()

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "nascimento": nascimento,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")
    

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor 
        extrato += f"\nDepósito: R$ {valor:.2f}"
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, valor, limite, limite_saques):
    if valor <= 0:
        print("Valor Inválido para saque.")
    elif numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor > limite:
        print(f"Saque acima do limite de R$ {limite:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        numero_saques += 1 
        extrato += f"\nSaque : R$ {valor:.2f}"
        print(f"Saque de R$ {valor:.2f} realizado!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    print("Sem movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("===================")


##      MENU      ##
while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("Valor do depósito R$: "))
        depositar(saldo, extrato, valor)

    elif opcao == "2":
        valor = float(input("Valor do saque R$: "))
        sacar(valor)

    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        cadastrar_usuario(usuarios)

    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        listar_contas()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")