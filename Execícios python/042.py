a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))
if a + b > c and b + c > a and a + c > b:
    if a == b and b == c and a == c:
        print("É um triângulo equilátero")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")