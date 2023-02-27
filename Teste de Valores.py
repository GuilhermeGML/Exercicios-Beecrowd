def teste(a, b, c, d):
    n = 0
    if b > c:
        n += 1
    if d > a:
        n += 1
    if c + d > a + b:
        n += 1
    if c and d > 0:
        n += 1
    if a % 2 == 0:
        n += 1
    if n == 5:
        print('Valores aceitos')
    else:
        print('Valores não aceitos')




# Programa Principal
a = float(input('Numero A: '))
b = float(input('Numero B: '))
c = float(input('Numero C: '))
d = float(input('Numero D: '))
teste(a, b, c, d)
