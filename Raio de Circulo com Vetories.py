def pontos(x1, x2, y1, y2):
    r = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return r


#Programa Principal
x1 = float(input('1 Ponto:'))
x2 = float(input('2 Ponto:'))
y1 = float(input('3 Ponto:'))
y2 = float(input('4 Ponto:'))
print(pontos(x1, x2, y1, y2))