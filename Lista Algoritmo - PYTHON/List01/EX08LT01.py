# Código realizado por Fernando Zilion
# Data: 03/2024
# 8. Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

class Rendimento():
    deposito = float(input("Digite o valor do depósito em poupança: "))
    
    rendimento = deposito * 0.013
    novo_valor = deposito + rendimento
    
    print(f"O valor após 1 mês de aplicação é: {novo_valor:.2f}")