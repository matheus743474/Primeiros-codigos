idade = int(input("Digite a idade do atleta: "))
if idade <= 9:
    print("Atleta mirim")
elif idade > 9 and idade <= 14:
    print("Atleta infantil")
elif idade > 14 and idade <= 19:
    print("Atleta junior")
elif idade == 20:
    print("Atleta sênior")
else:
    print("Atleta master")