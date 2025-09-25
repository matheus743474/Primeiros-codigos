numero = int(input("Digite um número: "))
print("""Escolha uma das bases para conversão
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal""")
escolha = int(input("Digite uma das opções: "))
if escolha == 1:
    print(f"{numero} convertido para binário é {bin(numero)[2:]}")
elif escolha == 2:
    print(f"{numero} convertido para octal é {oct(numero)[2:]}")
elif escolha == 3:
    print(f"{numero} convertido para hexadecimal {hex(numero)[2:]}")
else:
    print("Opção inválida")