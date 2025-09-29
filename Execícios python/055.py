maior = 0
menor = 99999999999
for x in range(5):
    peso = float(input("Digite o peso da pessoa: Kg"))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
        
print(f"A pessoa mais pesada tem {maior}Kg")
print(f"A pessoa mais leve tem {menor}Kg")