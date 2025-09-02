salario = float(input("Digite o salário do funcionário: "))

if salario >= 1250:
    novo_salario = (salario * 10 / 100) + salario
    print(f"O novo salário é de R${novo_salario}")
else:
    novo_salario = (salario * 15 / 100) + salario
    print(f"O novo salário é de R${novo_salario}")