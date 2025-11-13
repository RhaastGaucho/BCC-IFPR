class Carro:
    def __init__(self, odometro_inicial: int):
        self.odometro = odometro_inicial
        self.ultima_troca = odometro_inicial
        self.precisa_trocar_oleo = False

    def set_odometro(self, km: int):
        self.odometro = km
        if self.odometro - self.ultima_troca >= 5000:
            self.precisa_trocar_oleo = True

    def trocar_oleo(self):
        if self.precisa_trocar_oleo:
            self.ultima_troca = self.odometro
            self.precisa_trocar_oleo = False
            print("Óleo trocado.")
        else:
            print("Ainda não precisa trocar.")

c1 = Carro(2000)

while True:
    print(f"Última troca: {c1.ultima_troca} km | Atual: {c1.odometro} km")
    km_atual = int(input("Informe a quilometragem atual: "))
    c1.set_odometro(km_atual)

    if c1.precisa_trocar_oleo:
        print("Hora de trocar o óleo!")
        c1.trocar_oleo()
    else:
        print("Ainda não é hora de trocar o óleo.")

    if input("Continuar? (s/n) ").lower() != 's':
        break
