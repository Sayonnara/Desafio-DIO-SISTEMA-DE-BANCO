# Nesse desafio o comando while se encaixa perfeitamente
# É usado para fazer repetição de bloco de codigo varias vezes
menu = ("""
Seja Bem Vindo(A) 

[1] Sacar
[2] Depostar
[3] Extrato
[4] Sair
""")


SALDO = 1000
LIMITE = 500
EXTRATO = " "
SAQUE_MAX = 3
NUMERO_SAQUE = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor =float(input("Informa o valor do Saque:"))

        execedeu_saldo = valor >= SALDO
        execedeu_limite = valor >= LIMITE
        execedeu_saque = NUMERO_SAQUE >= SAQUE_MAX

        if execedeu_saldo:
            print("Saldo insuficiente, seu saldo é:" ,SALDO)
            
        elif execedeu_limite:
            print("Ops! Você utrapassou o limite o seu limite diario, tente outra opçao ")
        
        elif execedeu_saque:
            print("Ops! Você excedeu o limite de saque diario, Somente amanha conseguirá")

        elif valor > 0:
            SALDO -= valor
            EXTRATO += f"Saque:${valor:2f}\n"
            NUMERO_SAQUE += 1
        else:
            print("Valor informado é inválido")

    elif opcao == "2" :
        valor =float(input("Informa o valor do Depósito:"))
        
        if valor > 0:
            SALDO += valor
            EXTRATO += f"Deposito: R$ {valor:.2f}\n"

        else :
            print("Tente novamente")

    elif opcao == "3":
        print("\n********** extrato **********")
        print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
        print(f"\nSeu saldo é de R$ {SALDO:.2f}")
        print("\n****************************")
    elif opcao == "4":
        print("DESAFIO DA DIO CONCLUIDO COM SUCESSOOO UHUUU ")
        break
