from random import randint

escolha = input("Impar ou par: ").strip().lower()
jogador = int(input("Digite um número: "))
computador = randint(0, 10)

print(f"Você digitou {jogador}")
print(f"O computador escolheu {computador}")
soma = print(f"A soma é {jogador + computador}")

resultado = (jogador + computador) % 2

if resultado == 0 and escolha == "par":
    print("O resultado é par!")
    print("\033[0;32mVocê ganhou!\033[m")
elif resultado == 0 and escolha == "impar":
    print("O resultado é par!")
    print("\033[0;31mVocê perdeu!\033[m")
elif resultado == 1 and escolha == "par":
    print("O resultado é impar!")
    print("\033[0;31mVocê perdeu!\033[m")
elif resultado == 1 and escolha == "impar":
    print("O resultado é impar!")
    print("\033[0;32mVocê ganhou!\033[m")
else:
    print("Opção invalida")