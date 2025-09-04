velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("\033[0;31mMULTADO! Você excedeu o limite permitido de 80Km/h\033[m")
    multa = (velocidade - 80) * 7
    print(f"\033[0;31mVocê deve pagar uma multa de R${multa}\033[m")
print("Tenha um bom dia! Dirija com segurança!")
