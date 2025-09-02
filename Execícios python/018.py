from math import sin, cos, tan, radians

angulo = float(input("Digite o angulo: "))
angulo_radiano = radians(angulo)

print(f"Com o angulo sendo {angulo}, o seno é {sin(angulo_radiano):.2f}, cosseno é {cos(angulo_radiano):.2f}, tangente {tan(angulo_radiano):.2f}")