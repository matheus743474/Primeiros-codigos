ano = int(input("Em que ano estamos? "))
nascimento = int(input("Em que ano você nasceu? "))
idade = ano - nascimento

maior_ou_menor = "e você será maior de idade" if idade >= 18 else "e você será menor de idade"

print("Em", ano , "você tera" , idade , maior_ou_menor)
