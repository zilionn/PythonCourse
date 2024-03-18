# Código realizado por Fernando Zilion
# Data: 03/2024
# 12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

class Idade():
    ano_nasc = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    
    idade = ano_atual - ano_nasc
    idade_futura = idade + 17
    
    print("Sua idade é:" + idade)
    print("Daqui a 17 anos, você terá:" + idade_futura)