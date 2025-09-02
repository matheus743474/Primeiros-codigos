largura = float(input("Qual a largura? "))
altura = float(input("Qual a altura? "))

m2 = largura * altura
quantidade_tinta = m2 / 2

print(f"Para pintar uma parede com largura de {largura} e altura de {altura} ({m2}m²), será necessario {quantidade_tinta:.2f}l de tinta")