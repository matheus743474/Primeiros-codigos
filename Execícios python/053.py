palavra = str(input("Digite uma palavra: "))

palavra_certa = palavra.lower().replace(" ", "")
palindromo = palavra_certa[::-1]

if palavra_certa == palindromo:
    print(f"A palavra {palavra} é um palindromo")
else:
    print(f"A palavra {palavra} não é um palindromo")