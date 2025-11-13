from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        self.dist = 0
    
    @abstractmethod
    def mover(self):
        pass

class Aquatico(Animal):
    def __init__(self):
        super().__init__()

    def mover(self):
        self.dist += 5

        return print(f"Distancia percorrida por aquatico: {self.dist}")

class Terrestre(Animal):
    def __init__(self):
        super().__init__()

    def mover(self):
        self.dist += 2

        return print(f"Distancia percorrida por terrestre: {self.dist}")       

class Aereo(Animal):
    def __init__(self):
        super().__init__()

    def mover(self):
        self.dist += 10

        return print(f"Distancia percorrida por aereo: {self.dist}")
        
animais = [Aquatico(), Terrestre(), Aereo()]

for a in animais:
    a.mover()
    a.mover()

