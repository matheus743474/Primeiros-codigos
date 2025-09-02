from random import randint
from time import sleep

computador = randint(0, 5)
print("-" * 57)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-" * 57)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
print("")

if jogador == computador:
    print("Parabéns! Você ganhou!")
    print(f"O número era {computador}")
else:
    print("Eu ganhei!")
    print(f"O número era {computador}")