termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
for x in range(1, 11):
    formula = termo1 + (x - 1) * razao
    print(f"{formula}", end=", ")