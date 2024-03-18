# Código realizado por Fernando Zilion
# Data: 03/2024
# 11. Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.

import math # Importei uma biblioteca do python que possue diversas funções

class Circunferencia():
    raio = float(input("Digite o raio da circunferência: "))
    
    comprimento = 2 * math.pi * raio # A função math.pi representa o número do PI, assim fica mais fácil realizar o cálculo
    
    print(f"O comprimento da circunferência é: {comprimento:.2f}")