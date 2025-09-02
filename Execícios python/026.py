frase = input("Digite uma frase: ").strip()

print(f"Tem {frase.upper().count("A")} letras A na sua frase")
print(f"O primeiro A está na posição {frase.upper().find("A")+1}")
print(f"E último A está na posição {frase.upper().rfind("A")+1}")