class Multiplos():

    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    if max(numero1, numero2) % min(numero1, numero2) == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")