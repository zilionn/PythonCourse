# Código realizado por Fernando Zilion
# Data: 03/2024
# 7. Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

class Volume():
    comprimento = float(input("Digite o comprimento do paralelepípedo: "))
    largura = float(input("Digite a largura do paralelepípedo: "))
    altura = float(input("Digite a altura do paralelepípedo: "))
    
    volume = comprimento * largura * altura
    
    print(f"O volume do paralelepípedo é: {volume}")
