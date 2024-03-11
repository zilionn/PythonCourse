# Código realizado por Fernando Zilion
# Data: 03/2024
# 16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

class Salario():
    horas = float(input("Digite a quantidade de horas trabalhadas: "))
    valor_hora = float(input("Digite o valor por hora: "))
    desconto = float(input("Digite o percentual de desconto: "))
    descendentes = int(input("Digite o número de descendentes: "))
    
    salario_bruto = horas * valor_hora
    desconto = salario_bruto * (desconto / 100)
    salario_liquido = salario_bruto - desconto + (descendentes * 100)
    
    print(f"O salário a receber é: {salario_liquido}")