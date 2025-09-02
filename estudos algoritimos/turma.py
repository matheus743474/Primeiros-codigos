print("---------------------------")
print("  ESCOLA SANTA PACIENCIA")
print("---------------------------")

alunos = int(input("Quantos alunos a turma tem? "))
contador = 1
aluno = 1
melhor_nota = 0
melhor_aluno = ""


print("---------------------------")

while contador <= alunos:
    print("ALUNO", aluno)
    nome = str(input("Nome do aluno: "))
    nota = float(input(f"Nota de {nome}: ",))
    aluno += 1
    contador += 1
    if nota >= melhor_nota:
        melhor_nota = nota
        melhor_aluno = nome
    print("---------------------------")
print("O melhor aproveitamento foi de", melhor_aluno,"com nota", melhor_nota)
