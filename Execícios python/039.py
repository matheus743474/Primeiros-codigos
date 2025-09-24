from datetime import date
ano = int(input("Digite o ano que você nasceu: "))
idade = date.today().year - ano
if idade == 18:
    print("Está na hora de se alistar")
elif idade < 18:
    print("Ainda vai se alistar")
    print(f"falta {abs(date.today().year - ano - 18)} ano(s) para se alistar ")
else:
    print("Já passou do tempo de se alistar")
    print(f"Já passou {date.today().year - ano - 18} ano(s) para se alistar")