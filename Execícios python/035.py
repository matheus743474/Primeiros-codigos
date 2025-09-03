lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 + lado3 > lado2 and lado2 + lado3 > lado1 and lado1 + lado2 > lado3:
    print("Os segmentos acima podem forma um triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")