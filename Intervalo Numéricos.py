def interval(num):
    if 0 <= num <= 25:
        print(f'{num} pertence ao intervalo [0, 25]')
    elif 25 < num <= 50:
        print(f'{num} pertence ao intervalo [25.1, 50]')
    elif 50 < num <= 75:
        print(f'{num} pertence ao intervalo [50.1, 75]')
    elif 75 < num <= 100:
        print(f'{num} pertence ao intervalo [75.1, 100]')
    else:
        print(f'{num} não pertence aos intervalos analisádos')

#Programa Principal
interval(15)
interval(32.7)
interval(51)
interval(99.74)
interval(200)
