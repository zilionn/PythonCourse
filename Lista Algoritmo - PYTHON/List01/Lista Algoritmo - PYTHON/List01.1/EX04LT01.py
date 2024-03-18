# Código realizado por Fernando Zilion
# Data: 03/2024
# 4. Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em Fahrenheit.

class Temperatura():
    celsius = float(input("Digite a temperatura em Celsius: "))
    
    fahrenheit = (celsius * 1.8) + 32
    
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")