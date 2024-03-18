class Divisibilidade():
    valor = int(input("Digite um valor inteiro: "))

    if valor % 2 == 0 and valor % 3 == 0:
        print("O valor é divisível por 2 e por 3.")
    elif valor % 2 == 0:
        print("O valor é divisível apenas por 2.")
    elif valor % 3 == 0:
        print("O valor é divisível apenas por 3.")
    else:
        print("O valor não é divisível por 2 nem por 3.")