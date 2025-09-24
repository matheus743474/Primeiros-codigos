numero = int(input("Digite um número: "))
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")
escolha = str(input("Digite uma das opções acima: "))
if escolha == "1":
    print(f"O resultado é {bin(numero)[2:]}")
elif escolha == "2":
    print(f"O resultado é {oct(numero)[2:]}")
else:
    print(f"O resultado é {hex(numero)[2:]}")