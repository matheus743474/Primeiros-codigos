from random import choice
escolhas = ["Cara", "Coroa"]
print("""Cara ou coroa
[1] Cara
[2] Coroa""")
jogador = str(input("Digite sua escolha: ")).strip()
moeda = choice(escolhas)
if jogador == "1":
    jogador = "Cara"
else:
    jogador = "Coroa"
print(f"Você escolheu {jogador}")
print(f"A moeda caiu {moeda}")
if jogador == "Cara" and moeda == "Cara" or jogador == "Coroa" and moeda == "Coroa":
    print("Você ganhou")
elif jogador == "Coroa" and moeda == "Cara" or jogador == "Cara" and moeda == "Coroa":
    print("Você perdeu")
else:
    print("Opção inválida")