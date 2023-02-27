def trocado(real):
    cem = 0
    cinquenta = 0
    vinte = 0
    dez = 0
    cinco = 0
    dois = 0

    if real >= 100:
        while real >= 100:
            real -= 100
            cem += 1
    if real >= 50:
        while real >= 50:
            real -= 50
            cinquenta += 1
    if real >= 20:
        while real >= 20:
            real -= 20
            vinte += 1
    if real >= 10:
        while real >= 10:
            real -= 10
            dez += 1
    if real >= 5:
        while real >= 5:
            real -= 5
            cinco += 1
    if real >= 2:
        while real >= 2:
            real -= 2
            dois += 1

    print('Notas:')
    print(f'{cem} notas de R$:100')
    print(f'{cinquenta} notas de R$:50')
    print(f'{vinte} notas de R$:20')
    print(f'{dez} notas de R$:10')
    print(f'{cinco} notas de R$:5')
    print(f'{dois} notas de R$:2')
    print(f'Falta {real} de trocado')



# Programa Principal
trocado(389.75)