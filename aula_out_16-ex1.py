import os
os.system('clear')

class Animal:
    def __init__(self, nome, idade, vacinado, dono):
        self.nome = nome
        self.idade = idade
        self.vacinado = vacinado
        self.dono = dono
    
    def comer(self):
        print(f"{self.nome} está dormindo")

    def dormir(self):
        print(f"{self.nome} está comendo")

class Cachorro(Animal):
    def __init__(self, nome, idade, vacinado, dono, parvovirose):
        super().__init__(nome, idade, vacinado, dono)
        self.parvovirose = parvovirose

    def latir(self):
        print(f"{self.nome} diz AUAU!!")

class Gato(Animal):
    def miar(self):
        print(f"{self.nome} diz MIAU!!")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
cli1 = Cliente("Mauro", "137.735.049-50")
c1 = Cachorro("Ricardo", 22, True, cli1, False)
g1 = Gato("Carlos", 10, False, cli1)

c1.latir()
c1.comer()
c1.dormir()

g1.miar()

print(f"O dono {c1.dono.nome} está preocuopado com seu cachorro {c1.nome}")

if c1.parvovirose == True:
    print("O cachoro tem parvovirose")
else:
    print("O cachorro nao tem parvovirose")
