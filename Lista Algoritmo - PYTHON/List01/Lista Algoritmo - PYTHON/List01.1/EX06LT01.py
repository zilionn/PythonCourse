# Código realizado por Fernando Zilion
# Data: 03/2024
# 6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

class TrocaValores():
    x = input("Digite o valor de x: ")
    y = input("Digite o valor de y: ")
    
    x,y = y,x
    
    print(f"O valor de x após a troca é: {x}")
    print(f"O valor de y após a troca é: {y}")