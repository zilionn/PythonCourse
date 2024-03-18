# Código realizado por Fernando Zilion
# Data: 03/2024
# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

class Reajuste():
    salario = float(input("Digite o salário do funcionário: ")) # Float permite números decimais
    
    novo_salario = salario * 1.15 # * == MULTIPLICAÇÃO 
    
    print("O novo salário com reajuste de 15% é:", novo_salario) # Observe que aqui utilizei uma vírgula para incluir a variável ao "print"
    
    # Caso você queira exibir uma quantidade determinada de números após a vírgula, você pode fazer o print da seguinte maneira:
    print(f"O novo salário reajustado é de: {novo_salario:.2f}")
    # O "f" antes da sua frase é o que indica que seu texto é uma string especial (f-string), na qual você pode incorporar variáveis por meio de chaves e formatá-las