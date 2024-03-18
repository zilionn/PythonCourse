class Preco():
    preco_atual = float(input("Digite o preço atual do produto: "))
    venda_mensal = float(input("Digite a média mensal de venda do produto: "))

    if venda_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.10
    elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
        novo_preco = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95
    else:
        novo_preco = preco_atual

    print("O novo preço do produto é de R$", novo_preco)