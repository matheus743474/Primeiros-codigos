m = float(input("Massa (Kg): "))
a = float(input("Altura (m): "))
IMC = m / (a ** 2)

print("IMC:", round(IMC, 2))

if (IMC >= 18.5) and (IMC <= 25):
    print("Peso Ideal")
elif IMC < 17:
    print("Muito Abaixo do Peso")
elif (IMC >=17) and (IMC < 25):
    print("Abaixo do Peso")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso")
elif IMC >= 30 and IMC < 35:
    print("Obesidade")
elif IMC >= 35 and IMC < 40:
    print("Obesidade Severa")
else:
    print("Obesidade Morbida")
