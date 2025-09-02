print("BANGU X MADUREIRA")
print("-------------------------------")
bangu = int(input("Quantos gols do BANGU? "))
madureira = int(input("Quantos gols do MADUREIRA? "))
print("-------------------------------")

diferenca = abs(bangu - madureira)
print("DIFERENÇA:", diferenca)

if diferenca == 0:
    print("STATUS: EMPATE")
elif diferenca >= 1 and diferenca <= 4:
    print("STATUS: PARTIDA NORMAL")
else:
    print("STATUS: GOLEADA")
    
print("-------------------------------")