todas_idade = 0
maior_idade = 0
homem_velho = ""
mulher = 0
for x in range(4):
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: ")).strip().lower()
    todas_idade += idade
    if sexo == "feminino" and idade < 20:
        mulher += 1
    if idade > maior_idade and sexo == "masculino":
        homem_velho = nome
        maior_idade = idade
    print("")
media = todas_idade / 4
print(f"A média de idade do grupo é {media}")
print(f"O homem mais velho é {homem_velho}")
print(f"Tem {mulher} mulheres com menos de 20 anos")