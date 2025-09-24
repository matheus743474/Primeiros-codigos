nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a outra nota: "))
media = (nota1 + nota2) / 2
print(f"A média foi {media}")
if media < 5:
    print("REPROVADO")
elif media > 5 and media < 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")