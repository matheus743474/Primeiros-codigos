preco_produto = float(input("Qual o preço do produto? R$"))

desconto = preco_produto - (preco_produto * 5 / 100)

print(f"O valor de R${preco_produto} com 5% de desconto é de R${desconto:.2f}")