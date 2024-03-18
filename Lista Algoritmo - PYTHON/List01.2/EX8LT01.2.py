class TempoJogo():
    hora_inicio = input("Digite a hora de início (HH:MM): ")
    horas_inicio, minutos_inicio = map(int, hora_inicio.split(':'))

    hora_final = input("Digite a hora de término (HH:MM): ")
    horas_final, minutos_final = map(int, hora_final.split(':'))

    horas = horas_final - horas_inicio
    minutos = minutos_final - minutos_inicio

    if minutos < 0:
        horas -= 1
        minutos += 60

    if horas < 0:
        horas += 24

    print("A duração do jogo foi de", horas, "horas e", minutos, "minutos.")