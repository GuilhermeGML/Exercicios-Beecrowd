class Frutas():
    def __init__(self, valor, quant):
        self.valor = valor
        self.quant = quant

    def maca(self, quant):
        self.quant = quant
        frut1 = ((self.quant * 200) / 1000) * 10
        print(f'Maça custo = R$:{frut1}')

    def uva(self, quant):
        self.quant = quant
        frut2 = ((self.quant * 200) / 1000) * 15
        print(f'Uva custo = R$:{frut2}')

    def banana(self, quant):
        self.quant = quant
        frut3 = ((self.quant * 200) / 1000) * 7
        print(f'Banana custo = R$:{frut3}')

    def laranja(self, quant):
        self.quant = quant
        frut4 = ((self.quant * 200) / 1000) * 12
        print(f'Laranja custo = R$:{frut4}')

    def limao(self, quant):
        self.quant = quant
        frut5 = ((self.quant * 200) / 1000) * 5
        print(f'Limão custo = R$:{frut5}')


# Programa Princial
print('Hortifruti Do Genius')
print('Frutas: ')
print('1 --- Maça --- R$:10,00 Kg')
print('2 --- Uva --- R$:15,00 Kg')
print('3 --- Banana --- R$:7,00 Kg')
print('4 --- Laranja --- R$:12,00 Kg')
print('5 --- Limão --- R$:5,00 Kg')
frutis = ['Maça', 'Uva', 'Banana', 'Laranja', 'Limão']

compras = Frutas(1, 1)
compras.maca(5)
compras.uva(5)
compras.banana(5)
compras.laranja(5)
compras.limao(5)
