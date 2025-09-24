valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos vai ser pago: "))

prestacao = round((valor / (anos * 12)), 2)
porcentagem = (salario/100 * 30) + salario
if prestacao > porcentagem:
    print("Empréstimo negado!")
else:
    print("Empréstimo aceito!")