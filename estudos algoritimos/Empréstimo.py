emprestimo = float(input("Qual o valor do empréstimo? "))
parcelas = int(input("Quantas parcelas? "))

juros = emprestimo * 20 / 100
total = (emprestimo + juros) / parcelas

print("Vou pagar", parcelas, "parcelas de R$", round(total, 2))