from random import randint
from time import sleep

computador = randint(0, 5)
print("-" * 57)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-" * 57)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
print("")

if jogador == computador:
    print("\033[0;32mParabéns! Você ganhou!\033[m")
    print(f"O número era {computador}")
else:
    print("\033[0;31mEu ganhei!\033[m")
    print(f"O número era {computador}")