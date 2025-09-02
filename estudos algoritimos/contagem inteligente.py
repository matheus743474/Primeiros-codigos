print("-------------------------")
print("  CONTADOR INTELIGENTE")
print("-------------------------")

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

print("-------------------------")
print("        CONTADOR ")
print("-------------------------")

if inicio < fim:
    while inicio <= fim:
        print(inicio, end="... ")
        inicio += 1
else:
    while fim <= inicio:
        print(fim, end="... ")
        fim += 1