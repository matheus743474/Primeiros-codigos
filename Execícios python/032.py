from calendar import isleap

ano = int(input("Digite um ano: "))
bissexto = isleap(ano)

if bissexto == True:
    print(f"O ano {ano} é um ano bissesto")
else:
    print(f"O ano {ano} não é um ano bissesto")