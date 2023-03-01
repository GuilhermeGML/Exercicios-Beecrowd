def balanceamento(temp, neutrons):
    cond = 0
    if temp <= 800:
        cond += 1
    if neutrons >= 500:
        cond += 1
    if (temp * neutrons) <= 500000:
        cond += 1
    if cond == 3:
        print('As condições de Temperatura, Número de Neutros e o produto entre eles'
              ' estão estáveis ')


def eficiencia(voltage, corrente, max_poder):
    percentual = ((voltage * corrente)/max_poder) * 100
    if percentual >= 80:
        print('Verd')
    elif 80 > percentual >= 60:
        print('Laranja')
    elif 60 > percentual >= 30:
        print('Vermelho')
    elif percentual < 30:
        print('Preto')


def zona_secura(temp, neutro_ps, limite):
    if temp * neutro_ps < 0.90 * limite:
        print('Baixa')
    elif 1.1 * limite > temp * neutro_ps > 0.9 * limite:
        print('Ideal')
    else:
        print('Perigo')


balanceamento(750, 600)
eficiencia(200, 50, 15000)
zona_secura(1000, 30, 5000)