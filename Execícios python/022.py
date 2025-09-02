nome = input("Digite seu nome completo: ").strip()

print(nome.upper())
print(nome.lower())
print(f"Seu nome completo tem {len(nome) - nome.count(" ")} letras")
print(f"Seu primeiro nome tem {nome.find(" ")} letras")