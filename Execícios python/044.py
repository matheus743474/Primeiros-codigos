print(f"{" LOJAS GUANABARA ":=^40}")
valor = float(input("Preço das compreas: R$"))
print(""" FORMAS DE PAGAMENTO)
[1] Dinheiro
[2] À vista no cartão
[3] Em 2x no cartão
[4] 3x ou mais no cartão""")
metodo = str(input("Qual a forma de pagamento? "))
if metodo == "1":
    print(f"Sua compra de R${valor} vai custar R${valor - (valor / 100 * 10):.2f}")
elif metodo == "2":
    print(f"Sua compra de R${valor} vai custar é R${valor - (valor / 100 * 5):.2f}")
elif metodo == "3":
    print(f"O valor a ser pago é R${valor} sem juros")
elif metodo == "4":
    parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcelas}x de R${valor / parcelas:.2f} com juros")
    print(f"Sua compra de R${valor} vai custar R${(valor / 100 * 20) + valor:.2f}")
else:
    print("opção invalida de pagamento")