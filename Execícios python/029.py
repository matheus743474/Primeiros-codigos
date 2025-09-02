velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido de 80Km/h")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma mula de R${multa}")
print("Tenha um bom dia! Dirija com segurança!")
