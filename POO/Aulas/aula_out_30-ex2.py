from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    @abstractmethod
    def calcularSalario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcularSalario(self):
        self.salario += 0.5*self.salario
        print(f"Novo salario de gerente: {self.salario}")

class Supervisor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcularSalario(self):
        self.salario += 0.2*self.salario
        print(f"Novo salario de supervisor: {self.salario}")

funcionarios = [
    Gerente("Claudia", 1000),
    Supervisor("Fernando", 500)
]

for f in funcionarios:
    f.calcularSalario()