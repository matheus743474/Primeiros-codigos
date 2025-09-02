from random import choice

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Digite pedra, papel ou tesoura: ").strip().lower()
computador = choice(opcoes)

print(f"Você escolheu {jogador}")
print(f"O computador escolheu {computador}")

if jogador == computador:
    print("Empate!")
elif jogador == "tesoura" and computador == "papel" or jogador == "pedra" and computador == "tesoura" or jogador == "papel" and computador == "pedra":
    print("Você ganhou!")
elif jogador == "pedra" and computador == "papel" or jogador == "tesoura" and computador == "pedra" or jogador == "papel" and computador == "tesoura":
    print("Você perdeu!")
else:
    print(f"Opção invalida!")