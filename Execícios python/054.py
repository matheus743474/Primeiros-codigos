from datetime import date
atual = date.today().year
maior = 0
menor = 0
for x in range(7):
    data = int(input("Digite o ano de nascimento: "))
    ano = atual - data
    if ano >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoas são maiores de idade")
print(f"{menor} pessoas são menores de idade")