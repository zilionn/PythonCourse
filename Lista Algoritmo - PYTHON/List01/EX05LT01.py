import math # O que fiz aqui é importar a biblioteca MATH. O Python possui diversas bibliotecas que contam com funções que facilitam a vida do programador.

# Código realizado por Fernando Zilion
# Data: 03/2024
# 5. Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).

class RaizesEquacao2Grau():
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    
    delta = B**2 - 4*A*C
    x1 = (-B + math.sqrt(delta)) / (2*A) # Observe que utilizei a função math.sqrt para conseguir a raíz do delta
    x2 = (-B - math.sqrt(delta)) / (2*A)
    
    print(f"As raízes reais da equação são: {x1:.2f} e {x2:.2f}")
    print("X1 é igual a: " + str(x1) + " e o X2 é igual a: " + str(x2))
    