# Código realizado por Fernando Zilion
# Data: 03/2024
# 17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

class LitrosGastos():
    tempo = float(input("Digite o tempo de percurso em horas: "))
    velocidade_media = float(input("Digite a velocidade média em km/h: "))
    
    distancia = tempo * velocidade_media
    litros = distancia / 12
    
    print(f"A quantidade de litros gastos na viagem é: {litros}")