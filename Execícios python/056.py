media = 0
homem_velho = ""
for x in range(4):
    nome = str(input("Digite o nome: "))
    idade = int("Digite a idade: ")
    sexo = str("Digite o sexo: ")
    if idade > homem_velho:
        homem_velho = idade
