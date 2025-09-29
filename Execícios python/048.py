soma = 0
for x in range(1, 501,):
    if x % 3 == 0 and x % 2 != 0:
        soma += x
print(soma)