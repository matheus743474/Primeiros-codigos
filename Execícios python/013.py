salario = float(input("Qual o valor do salário? R$"))

novo_salario = salario + (salario * 15 / 100)

print(f"Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}")