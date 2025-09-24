nome = str(input("Qaul o seu nome? "))
if nome == "Matheus":
    print("Que nome lindo você tem!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Maria Clara":
    print("Que nome feminino bonito")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {nome}")