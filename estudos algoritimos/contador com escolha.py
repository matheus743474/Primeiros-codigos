contador = 0
valor = int(input("Quer conta ate quanto? "))
salto = int(input("Qual será o valor do salto? "))

while contador <= valor:
    print(contador)
    contador += salto
print("Terminei de contar")