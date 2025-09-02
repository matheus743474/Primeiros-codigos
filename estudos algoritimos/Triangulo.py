l1 = float(input("DIgite o Primeiro lado: "))
l2 =float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

tri = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)
eq = (l1 == l2) and (l2 == l3)
es = (l1 != l2) and (l2 != l3) and (l1 != l3)

print("Pode formar um triangulo?", tri)
print("O triangulo é equilatero?", eq)
print("O triangulo é escaleno?" , es)

