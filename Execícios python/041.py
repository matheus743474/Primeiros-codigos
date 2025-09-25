from datetime import date
nascimento = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - nascimento
print(f"O atleta tem {idade} anos")
if idade <= 9:
    print("Atleta mirim")
elif idade > 9 and idade <= 14:
    print("Atleta infantil")
elif idade > 14 and idade <= 19:
    print("Atleta junior")
elif idade <= 25:
    print("Atleta sênior")
else:
    print("Atleta master")