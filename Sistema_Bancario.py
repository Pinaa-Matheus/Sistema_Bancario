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
        print("Depósito selecionado")
    elif opcao == "2":
        print("Saque selecionado")
    elif opcao == "3":
        print("Extrato selecionado")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Operação Inválida")
