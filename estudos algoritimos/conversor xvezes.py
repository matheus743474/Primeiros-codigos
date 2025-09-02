contador = 1
quantas = int(input("Quantas vezes quer converter? "))

while contador <= quantas:
    real = float(input("Qual o valor em R$? "))
    dolar = real / 5.54
    print("O valor convertido é US$", round(dolar, 2))
    contador += 1
