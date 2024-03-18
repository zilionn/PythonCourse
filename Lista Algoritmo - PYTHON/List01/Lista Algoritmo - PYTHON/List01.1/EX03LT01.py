# Código realizado por Fernando Zilion
# Data: 03/2024
# 3. Receba a base e a altura de um triângulo. Calcule e mostre a sua área.

class AreaTriangulo():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    
    area = (base * altura) / 2
    
    print("A área do triângulo é:" + area)
    