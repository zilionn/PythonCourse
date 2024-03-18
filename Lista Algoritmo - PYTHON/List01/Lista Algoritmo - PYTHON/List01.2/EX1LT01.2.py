class DiferencaMaior():
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    diferenca = abs(max(valor1, valor2) - min(valor1, valor2))
    print("A diferença entre os maiores valores é:", diferenca)