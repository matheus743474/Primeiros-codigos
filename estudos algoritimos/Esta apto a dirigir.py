print("---------------------------- ")
print("  DEPARTAMENTO DE TRANSITO")
print("---------------------------- ")

ano_atual = int(input("Ano Atual (yyyy): "))
ano_de_nasci = int(input("Ano de Nascimento (yyyy): "))

idade = ano_atual - ano_de_nasci

apto_ou_nao = "APTO A TIRAR CARTEIRA" if idade >= 18 else "INAPTO A TIRAR A CARTEIRA"

print("----------Status----------")
print("IDADE: ", idade)
print(apto_ou_nao)
print("--------------------------")
