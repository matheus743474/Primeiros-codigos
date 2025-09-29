numero = int(input("Digite um número: "))
primo = 0
for x in range(2 , 999999):
    if numero % x == 0:
        primo += 1
if primo == 1:
    print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")