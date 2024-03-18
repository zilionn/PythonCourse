class Investimento():
    tipo_investimento = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
    valor_investimento = float(input("Digite o valor do investimento: "))

    if tipo_investimento == 1:
        valor_corrigido = valor_investimento * 1.03
    elif tipo_investimento == 2:
        valor_corrigido = valor_investimento * 1.05
    else:
        valor_corrigido = valor_investimento

    print("O valor corrigido após 30 dias é de R$", valor_corrigido)