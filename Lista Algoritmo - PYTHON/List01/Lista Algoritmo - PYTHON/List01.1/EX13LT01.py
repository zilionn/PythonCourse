# Código realizado por Fernando Zilion
# Data: 03/2024
# 13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

class Alimento():
    quantidade_alimento = float(input("Digite a quantidade de alimento em quilos: "))
    
    dias_duracao = int(quantidade_alimento * (1000 / 50))
    
    print("Esse alimento durará aproximadamente " + str(dias_duracao) + " dias.")