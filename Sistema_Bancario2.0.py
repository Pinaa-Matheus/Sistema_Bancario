#### Variaveis ####
cliente = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

####################

MENU_CADASTRO = """"
========= Cadastro =========

       [1] Cadastra
       [2] Depositar

============================
"""


while True:
    opcao = input(MENU_CADASTRO)



def cadastrar_usuario(opcao):
    nome = input("Nome: ").strip() #Strip para não ter espaços 

cpf = input("CPF (somente números): ").strip()
cpf = ''.join(filter(str.isdigit, cpf)) # Filter vai passar por todas os caracteres
#checar se tem letra com true/false com isalpha()
#ve se tem 11 digitos 



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