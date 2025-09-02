nome_completo = input("Digite seu nome completo: ").strip()
print(f"Primeiro nome: {nome_completo.split()[0]}")
print(f"Último nome: {nome_completo.split()[-1]}")