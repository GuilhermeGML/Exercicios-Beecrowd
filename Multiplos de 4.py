def pum(num):
    p = 1
    s = 2
    t = 3
    a = 4
    c = 0

    while c < num:
        print(f'{p} {s} {t} Pum')
        p += a
        s += a
        t += a
        c += 1



#PRograma Principal
valor = int(input('Quantas sequencias quer? R: '))
pum(valor)