n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
r = n1 + n2 + n3
print(f"Sua nota foi {r}")
if r >= 15:
    print("Você passou de ano! parabéns")
else:
    print("Você repetiu de ano! estude mais")