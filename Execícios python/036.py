valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salário do comprador: R$"))
anos = int(input("Digite em quantos anos vai ser pago: "))

prestacao = round((valor / (anos * 12)), 2)
minimo = (salario/100 * 30) 
print(f"Para pagar uma casa de R${valor} em {anos}")
print(f"A prestação será de {prestacao}")
if prestacao >= minimo:
    print("Empréstimo negado!")
else:
    print("Empréstimo aceito!")