a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a + b > c and b + c > a and a + c > b:
    print("Pode formar um triângulo ", end="")
    if a == b and b == c and a == c:
        print("equilátero")
    elif a == b != c or a == c != b or b == c != a:
        print("isósceles")
    elif a != b != c != a:
        print("escaleno")
else:
    print("Não pode formar um triângulo")