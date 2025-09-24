valor = float(input("Digite o valor a ser pago: "))
print("[1] Dinheiro")
print("[2] À vista no cartão")
print("[3] Em 2x no cartão")
print("[4] 3x ou mais no cartão")
metodo = str(input("Digite a forma de pagamento: "))
if metodo == "1":
    print(f"O valor a ser pago é R${abs((valor / 100 * 10) - valor)}")
elif metodo == "2":
    print(f"O valor a ser pago é R${abs((valor / 100 * 5) - valor)}")
elif metodo == "3":
    print(f"O valor a ser pago é R${valor}")
elif metodo == "4":
    print(f"O valor a ser pago é R${(valor / 100 * 20) + valor}")
else:
    print("opção invalida")