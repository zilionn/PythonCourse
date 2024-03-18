class QuatroValores():
    
    valor1 = int(input("Digite o primeiro valor (crescente): "))
    valor2 = int(input("Digite o segundo valor (crescente): "))
    valor3 = int(input("Digite o terceiro valor (crescente): "))
    valor4 = int(input("Digite o quarto valor: "))

    if valor4 < valor1:
        print("Valores em ordem crescente:", valor4, valor1, valor2, valor3)
    elif valor4 < valor2:
        print("Valores em ordem crescente:", valor1, valor4, valor2, valor3)
    elif valor4 < valor3:
        print("Valores em ordem crescente:", valor1, valor2, valor4, valor3)
    else:
        print("Valores em ordem crescente:", valor1, valor2, valor3, valor4)