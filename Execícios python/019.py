from random import choice

alunos = []
contador = 1
while contador < 5:
    nomes = input("Digite o nome dos alunos: ")
    alunos.append(nomes)
    contador += 1

print(f"O aluno sorteado foi o {choice(alunos)}")