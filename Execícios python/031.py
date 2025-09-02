km = float(input("Qual a distancia da sua viagem em Km: "))
if km <= 200:
    r = km * 0.5
else:
    r = km * 0.45
print(f"O valor da sua passagem é de {r}")