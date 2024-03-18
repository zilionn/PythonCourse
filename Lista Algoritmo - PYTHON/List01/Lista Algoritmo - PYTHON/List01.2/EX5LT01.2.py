class OrdemCrescente():
    
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    if valor1 > valor2:
        print("Valores em ordem crescente:", valor2, valor1)
    else:
        print("Valores em ordem crescente:", valor1, valor2)