class Carro:
    def __init__(self, odometro, marca, modelo, placa, cor):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.odometro = odometro

    def getInformacoes(self):
        print(f"Marca: {self.marca} || Modelo: {self.modelo} || Placa: {self.placa} || Cor: {self.cor}")
c1 = Carro(2000, 'Ford', 'Ka','BNA-1234', 'branco')

c1.getInformacoes()