#### Variaveis ####
cliente = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

####################

MENU_CADASTRO = """
========= Cadastro =========

       [1] Cadastra
       [2] Depositar
       [0] Sair

============================
"""


def cadastrar_usuario():
        nome = input("Nome: ").strip() #Strip para não ter espaços 

        cpf = input("CPF (somente números): ").strip()
        cpf = ''.join(filter(str.isdigit, cpf)) # Filter vai passar por todas os caracteres

        if len(cpf) != 11:
                print("CPF inválido! Contate nosso suporte.")
                return

        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("\n Já existe um usuário cadastrado com esse CPF!")
                return
#checar se tem letra com true/false com isalpha()
#ve se tem 11 digitos 


while True:
    opcao = input(MENU_CADASTRO).strip()

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")


MENU = f("""
========= MENU =========
  Bem-Vindo {cliente}

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

========================
""")
#Cadastrar novo usuario 
#Cadastrar nova conta no banco 
#Criar funções para todo o sistema bancario 