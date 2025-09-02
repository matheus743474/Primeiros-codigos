usuario = "Matheus"
idade = 16
data_de_nascimento = "09/02/2008"
senha = "1234"

usuario_inserido = input("Insira um nome de usuario:")
senha_inserida = input("Insira uma senha:")

if usuario_inserido == usuario and senha_inserida == senha:
    print(f"Bem vindo {usuario}")

else:
    print("Usuario ou senha não encontrado")
