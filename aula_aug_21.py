import os
os.system("clear")

class Carro:
    def __init__(self, modelo, odometro, preco, cor):
        self.modelo = modelo
        self.odometro = odometro
        self.preco = preco
        self.cor = cor
    
    def setOdometro(self, novoOdometro):
        self.odometro = novoOdometro

    def setModelo(self, novoModelo):
        self.modelo = novoModelo

    def setPreco(self, novoPreco):
        self.preco = novoPreco

    def setCor(self, novoCor):
        self.cor = novoCor

c1 = Carro('Fiat Uno', 50000, 20000, 'Verde')

print(f"Modelo: {c1.modelo} || Quilometragem: {c1.odometro} || Preço: {c1.preco} || Cor: {c1.cor}")

c1.setOdometro(500)
c1.setModelo('Fiat Palio')
c1.setPreco(22000)
c1.setCor('Roxo')

print(f"Modelo: {c1.modelo} || Quilometragem: {c1.odometro} || Preço: {c1.preco} || Cor: {c1.cor}")
