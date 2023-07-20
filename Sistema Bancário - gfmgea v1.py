menu = """
 ===============MENU===============
 
 Olá! Seja bem-vindo ao Banco Digital Aegug!

 Digite uma opção para começar:
 
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

        opcao = input(menu)
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
        
            if valor > 0:
                saldo += valor
                print(f"\nDepósito realizado com sucesso no valor de: R${valor:.2f}\n")
                extrato += f"Depósito realizado: R$ {valor:.2f}\n"
            else:
                print("Não podemos concluir com sua solicitação. Verifique o valor informado. Iremos te direcionar ao menu principal :D")
       
        elif opcao == "2":
            valor = float(input("Informe o valor do saque desejado: "))

            excedeu_valor_saldo = valor > saldo

            excedeu_limite_saque = valor > limite
            
            excedeu_quantidade_saques = numero_saques > LIMITE_SAQUES

            if excedeu_valor_saldo:
                print("\nO valor informado é maior que o seu saldo atual. Por favor tente novamente. Iremos te direcionar ao menu principal :D")

            elif excedeu_limite_saque:
                print("\nO valor informado é maior que o limite diário disponível. Por favor tente novamente. Iremos te direcionar ao menu principal :D")

            elif excedeu_quantidade_saques:
                print("\nA quantidade diária de saques foi excedida. Por favor tente outro dia. Iremos te direcionar ao menu principal :D")

            elif valor > 0:
                saldo -= valor
                print(f"\nSaque realizado com sucesso no valor de: R${valor:.2f}\n")
                extrato += f"Saque realizado: R$ {valor:.2f}\n"

            else:
                print("O valor informado é inválido. Verifique o valor informado. Iremos te direcionar ao menu principal :D")

        elif opcao == "3":
            print("\n==============EXTRATO==============")
            print("Não foram realizadas movimentações na conta." if not extrato else extrato)
            print(f"\nSaldo atual da conta: {saldo:.2f}")

        elif opcao == "0":
            break
    
        else:
            print("A opção desejada não é válida. Tente outra novamente!")