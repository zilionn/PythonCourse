import math

class EquacaoSegundoGrau():

    coeficiente_a = float(input("Digite o coeficiente 'a': "))
    coeficiente_b = float(input("Digite o coeficiente 'b': "))
    coeficiente_c = float(input("Digite o coeficiente 'c': "))

    delta = coeficiente_b**2 - 4*coeficiente_a*coeficiente_c
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        raiz = -coeficiente_b / (2*coeficiente_a)
        print(f"Existe uma raiz real: {raiz}")
    else:
        raiz1 = (-coeficiente_b + math.sqrt(delta)) / (2*coeficiente_a)
        raiz2 = (-coeficiente_b - math.sqrt(delta)) / (2*coeficiente_a)
        print(f"As raízes reais são: {raiz1} e {raiz2}")