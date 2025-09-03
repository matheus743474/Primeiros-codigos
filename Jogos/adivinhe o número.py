from random import randint

computador = randint(1, 100)
tentativas = 0

while True:
    numero = int(input("Digite um número entre 0 a 100: "))

    if numero == computador:
        print(f"\033[0;32mVocê acertou!\033[m O número era {computador}")
        tentativas += 1
        print(f"Você acertou com {tentativas} tentativas")
        break
    elif numero > computador:
        print("Digite um número menor")
        print("")
        tentativas += 1
    elif numero < computador:
        print("Digite um número maior")
        print("")
        tentativas += 1

    
