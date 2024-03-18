# Código realizado por Fernando Zilion
# Data: 03/2024
# 9. Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

class SomaQuadrados():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    soma_quadrados = pow(num1, 2) + pow(num2, 2)
    
    print("A soma dos quadrados é:", soma_quadrados)