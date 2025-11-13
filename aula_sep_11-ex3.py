class Carro:
    def __init__(self, marca, modelo, placa, cor, odometro):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.odometro = odometro

    def set_odometro(self, km: int):
        while True:
            if km >= self.odometro:
                self.odometro = km
                break
            else: 
                km = int(input(f"Valor inválido, informe um número maior que {self.odometro}: "))

    def getInformacoes(self):
        print(f"Marca: {self.marca} || Modelo: {self.modelo} || Placa: {self.placa} || Cor: {self.cor} || Odometro: {self.odometro}")

prog = 1
i = 1
carros = []

while prog != 0:
    marca = input(f"Informe a marca do veículo {i}: ")
    modelo = input(f"Informe a modelo do veículo {i}: ")
    placa = input(f"Informe a placa do veículo {i}: ")
    cor = input(f"Informe a cor do veículo {i}: ")
    odometro = int(input(f"Informe a odometro do veículo {i}: "))

    carros.append(Carro(marca, modelo, placa, cor, odometro))

    i += 1

    busca = input("Deseja buscar algum veículo pela placa? (s/n): ").lower()
    if busca == 's':
        placa_busca = input("Informe a placa: ")

        for carro in carros:
            if carro.placa == placa_busca:
                carro.getInformacoes()
                break
    
    prog = int(input("Cadastrar outro veículo? (1=sim / 0=não): "))