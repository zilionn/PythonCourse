# Código realizado por Fernando Zilion
# Data: 03/2024
# 10. Receba 2 números reais. Calcule e mostre a diferença dos custos desses valores.

class DiferencaCustos():
    num1 = float(input("Digite o primeiro número real: "))
    num2 = float(input("Digite o segundo número real: "))
    
    diferenca_custos = abs(num1 - num2) # A função ABS garante que a diferença seja sempre positiva, com um valor absoluto. Como nesse caso queremos a diferença dos custos dos valores, o número terá que ser positivo.
    
    print(f"A diferença dos custos é: {diferenca_custos}")