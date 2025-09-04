from time import sleep
from random import choice
jogar_de_novo = "sim"
while jogar_de_novo == "sim":
    print("Jokenpo")
    print("[1]\033[0;31mPedra\033[m")
    print("[2]\033[0;33mPapel\033[m")
    print("[3]\033[0;34mTesoura\033[m")
    jogador = str(input("Digite sua escolha: "))
    escolha = ["pedra", "papel", "tesoura"]
    computador = choice(escolha)
    print("JO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PO...")
    print(f"O computador escolheu {computador}")
    if jogador == "1" and computador == "pedra" or jogador == "2" and computador == "papel" or jogador == "3" and computador == "tesoura":
        print("Empate!")
    elif jogador == "1" and computador == "tesoura" or jogador == "2" and computador == "pedra" or jogador == "3" and computador == "papel":
        print("\033[0;32mParabéns! Você ganhou!\033[m")
    elif jogador == "1" and computador == "papel" or jogador == "2" and computador == "tesoura" or jogador == "3" and computador == "pedra":
        print("\033[0;31mVocê perdeu!\033[m")
    else:
        print("Você jogou uma opção invalida")
    jogar_de_novo = input("Quer jogar de novo? ").lower().strip()