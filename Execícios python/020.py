from random import sample
contador = 1
alunos = []

while contador < 5:
    nome = input("Digite o nome dos alunos: ")
    nome = alunos.append(nome)
    contador += 1

print(f"A ordem de apresentação é: {sample(alunos, 4)}")