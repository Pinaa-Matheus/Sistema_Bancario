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
        deposito = int(input("Valor do deposito"))
        if deposito > 0:
            deposito += saldo
            print(f"Realizando o deposito de {deposito}")
            extrato += f"\nDeposito realizado: R$ {deposito}\n" #Add o extrato, o \n é para não ficar desorganizado.
        else: #Adicionar uma mensagem para 0 reais
            print("Não foi possivel realizar seu deposito")
    elif opcao == "2":
        print("Saque selecionado")
    elif opcao == "3":
        print(extrato)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Operação Inválida")
