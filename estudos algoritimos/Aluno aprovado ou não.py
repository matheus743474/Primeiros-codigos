print("-------------------------")
print("  ESCOLA JAVALI CANSADO")
print("-------------------------")
primeira_nota = float(input("Primeira Nota: "))
segunda_nota = float(input("Segunda Nota: "))
print("-------------------------")
media = (primeira_nota + segunda_nota) / 2
print("MEDIA: ", media)
if media >= 7:
    print("ALUNO APROVADO")
elif media >= 5 < 7:
    print("ALUNO DE RECUPERAÇÃO")
else:
    print("ALUNO REPROVADO")
print("-------------------------")