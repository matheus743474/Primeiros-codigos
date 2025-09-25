from datetime import date
nascimento = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}")
if idade == 18:
    print("Está na hora de se alistar")
elif idade < 18:
    print("Ainda vai se alistar")
    print(f"falta {18 - idade} ano(s) para se alistar ")
    ano = atual + (18 - idade)
    print(f"Seu alistamento será em {ano}")
else:
    print("Já passou do tempo de se alistar")
    print(f"Já passou {idade - 18} ano(s) para se alistar")
    ano = atual - (idade - 18)
    print(f"Seu alistamento foi em {ano}")