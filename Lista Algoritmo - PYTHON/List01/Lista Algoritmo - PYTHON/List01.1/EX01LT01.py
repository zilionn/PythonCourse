# Código realizado por Fernando Zilion
# Data: 03/2024
# 1.Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.

class ValorQuadrado():
    valor_lado = int(input("Insira o valor de um lado do quadrado: ")) # No python, precisamos fazer a conversão de um "input" caso este seja um int ou float (um número), pois o input retorna um texto (string)
                                                                           
    valor_area = valor_lado ** 2 # Os dois "*" significam que a variável "valor_quadrado" está sendo elevada a 2.
    
    print(f"A área é: {valor_area}")
    
    #Também podemos usar a função POW para realizar a mesma operação:
    lado = int(input("Insira o lado de um quadrado para agora calcularmos com a função pow: "))
    
    area = pow(lado, 2)
    
    print("A área utilizando a função pow é: " + str(area))
    # Observe que aqui utilizei o + para mostrar a variável "area" e a converti para um "str", ou seja, um "string". Sempre que quiser mostrar um NÚMERO em um "Print", converta-o para "str".
    