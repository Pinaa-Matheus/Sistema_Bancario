saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

MENU = """
========= MENU =========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

========================
"""

while True:
    opcao = input(MENU)

    if opcao == "1":
        deposito = float(input("Valor do deposito R$: "))
        if deposito > 0:
            saldo += deposito
            print(f"Realizando o deposito de {deposito}!")
            extrato += f"\nDeposito realizado: R$ {deposito}\n" #Add o extrato, o \n é para não ficar desorganizado.
        else: 
            print("Não foi possivel realizar seu deposito!")

    elif opcao == "2":
            saque = float(input("Valor do Saque R$: "))
            if saque <= 0: #Ver se o valor é posivo
                print("Operação falhou! O valor informado para o saque é inválido. Por favor, insira um valor positivo.")
            elif numero_saques >= LIMITE_SAQUES: #Ver se ele atingiu o limite diario
                print("Operação falhou! Você atingiu o limite diário de saques.")          
            elif saque > limite: #Ver se ele tem limite
                print(f"Operação falhou! Voce atingiu o seu limite de {limite}")
            elif saque > saldo: #Ver se ele tem saldo
                print("Operação falhou! Você não tem saldo suficiente")
            else:
                saldo -= saque #Diminui o valor do saque do saldo
                numero_saques += 1 
                extrato += f"\nSaque Realizado: {saque}\n"
                print(f"Saque de R$ {saque} realizado!")

    elif opcao == "3":
            print(extrato)

    elif opcao == "4":
            print("Saindo...")
            break
    else:
        print("Operação Inválida")
