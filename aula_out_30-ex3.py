from abc import ABC, abstractmethod
import math

class Formas(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def calcularArea(self):
        pass

class Retangulo(Formas):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def calcularArea(self):
        area = self.a * self.b
        return area

class Quadrado(Formas):
    def __init__(self, a):
        super().__init__(a)

    def calcularArea(self):
        area = self.a * self.a
        return area

class Paralelogramo(Formas):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    def calcularArea(self):
        area = self.a * self.b * math.sin(math.radians(self.c))
        return area

class Trapezio(Formas):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    def calcularArea(self):
        area = ((self.a + self.b) * self.c) / 2
        return area

formas = [
    Retangulo(10, 5),
    Quadrado(6),
    Paralelogramo(8, 4, 30), 
    Trapezio(10, 6, 4)
] 

for f in formas: 
    print(f"{f.__class__.__name__}:")
    print(f"Área = {f.calcularArea():.2f}")
    print()