print("-----------------------------")
print("   CRIANÇA ESPEANÇA")
print("-----------------------------")
print(" Muito obrigado por ajudar")
print("[1] Para doar R$10")
print("[2] Para doar R$25")
print("[3] Para doar R$50")
print("[4] Para doar outros valores")
print("[5] Para cancelar")

escolha = int(input(""))

if escolha == 1:
    valor = 10
elif escolha == 2:
    valor = 25
elif escolha == 3:
    valor = 50
elif escolha == 4:
    valor = float(input("Digite o valor: R$"))
else:
    valor = 0
    
print("-----------------------------")
print("  SUA DOAÇÃO FOI DE R$", valor)
print("  MUITO OBRIGADO!")
print("-----------------------------")