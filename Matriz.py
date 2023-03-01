matriz = list()
for l in range(1, 4):
    for c in range(1, 4):
        a = int(input(f'Valor {l} {c}: '))
        matriz.append(a)


# (0,0) (0,1) (0,2) /(1,0) (1,1) (1,2)/(2,0) (2,1) (2,2)
print(matriz[:3])
print(matriz[3:6])
print(matriz[6:])


