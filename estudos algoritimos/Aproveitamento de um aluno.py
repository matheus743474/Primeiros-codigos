print("-------------------------")
print("  ESCOLA JAVALI CANSADO")
print("-------------------------")

primeira_nota = float(input("Primeira Nota: "))
segunda_nota = float(input("Segunda Nota: "))

media = (primeira_nota + segunda_nota) / 2

print("-------------------------")

print("Media:", media)

if media >= 9:
    print("A")
elif media < 9 and media >= 8:
    print("B")
elif media < 8 and media >= 7:
    print("C")
elif media < 7 and media >= 6:
    print("D")
elif media < 6 and media >= 5:
    print("E")
else:
    print("F")

print("-------------------------")
