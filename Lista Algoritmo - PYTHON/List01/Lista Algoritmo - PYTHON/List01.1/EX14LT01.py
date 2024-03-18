# Código realizado por Fernando Zilion
# Data: 03/2024
# 14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

class AngulosTriangulo():
    angulo_1 = float(input("Digite o valor do primeiro ângulo: "))
    angulo_2 = float(input("Digite o valor do segundo ângulo: "))
    
    angulo_3 = 180 - (angulo_1 + angulo_2)
    
    print("O valor do terceiro ângulo é: " + str(angulo_3))