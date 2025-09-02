a = float(input("Digite um número: "))
operador = input("Digite um operador logico: ")
b = float(input("Digite outro número: "))
resultado = 0
if operador == "+":
    resultado = a + b
    print(f"O resultado é {resultado}")
elif operador == "-":
    resultado = a - b
    print(f"O resultado é {resultado}")
elif operador == "*":
    resultado = a * b
    print(f"O resultado é {resultado}")
elif operador == "/":
    resultado = a / b
    print(f"O resultado é {resultado}")
elif operador == "**":
    resultado = a ** b
    print(f"O resultado é {resultado}")
else:
    print("Digite um operador valido")