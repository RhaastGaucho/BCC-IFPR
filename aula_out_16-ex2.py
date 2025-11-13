class Veiculo:
    def __init__(self, marca, modelo, ano, numeroPortas):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.numeroPortas = numeroPortas

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numeroPortas, tipoCombustivel):
        super().__init__(marca, modelo, ano, numeroPortas)
        self.tipoCombustivel = tipoCombustivel

class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, tipoMoto):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        self.tipoMoto = tipoMoto
    
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cargaMaxima):
        super().__init__(marca, modelo, ano)
        self.cargaMaxima = cargaMaxima