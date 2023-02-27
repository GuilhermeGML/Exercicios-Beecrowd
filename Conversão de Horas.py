def horario(s):
    min = 0
    hor = 0
    if s >= 60:
        while s >= 60:
            s -= 60
            min += 1
    if min >= 60:
        while min >= 60:
            min -= 60
            hor += 1
    if min >= 60:
        while min >= 60:
            min -= 60
    print(f'Horas: {hor}, Minutos: {min}, Segundos: {s}')


# Programa Principal
horario(3600)
