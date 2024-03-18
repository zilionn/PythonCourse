class VelocidadeMedia():
    num_voltas = int(input("Digite o número de voltas: "))
    extensao_circuito = float(input("Digite a extensão do circuito em metros: "))
    tempo_duracao = float(input("Digite o tempo de duração em minutos: "))

    distancia_total = num_voltas * extensao_circuito
    tempo_horas = tempo_duracao / 60

    velocidade_media = distancia_total / tempo_horas

    print("A velocidade média é de", velocidade_media, "km/h.")