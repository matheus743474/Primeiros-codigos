peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")