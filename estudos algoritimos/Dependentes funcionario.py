nome = str(input("Qual o nome do funcionario? "))
salario = float(input("Qual o salário do funcionario? R$"))
dependente = int(input("Qual e a quantidade de dependentes? "))

if dependente == 0:
    novo_salario = salario + (salario * 5 / 100)
elif dependente >= 1 and salario < 4:
    novo_salario = salario + (salario * 10 / 100)
elif dependente >= 4 and dependente < 7:
    novo_salario = salario + (salario *15 / 100)
else:
    novo_salario = salario + (salario * 18 / 100)

print("O novo salário de", nome, "será de R$", novo_salario)