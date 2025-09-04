numero = float(input("Digite um número: "))

if numero > 1:
    print(f"O número {numero} é \033[0;32mpositivo\033[m")
elif numero < -1:
    print(f"O número {numero} é \033[0;31mnegativo\033[m")
elif numero == 0:
    print(f"O número {numero} é 0")