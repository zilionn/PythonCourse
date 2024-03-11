# Código realizado por Fernando Zilion
# Data: 03/2024
# 15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

import math

class Hipotenusa():
    cateto1 = float(input("Digite o valor do primeiro cateto: "))
    cateto2 = float(input("Digite o valor do segundo cateto: "))
    
    hipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))
    
    print(f"O valor da hipotenusa é: {hipotenusa:.2f}")