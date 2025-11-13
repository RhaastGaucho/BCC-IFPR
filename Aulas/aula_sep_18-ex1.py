class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular

        if saldo < 0:
            self.__saldo = 0.0
        else:
            self.__saldo = saldo

    def getNumero(self): 
        return self.numero
    
    def getTitular(self): 
        return self.titular
    
    def getSaldo(self): 
        return self.__saldo
    
    def setNumero(self, novoNumero):
        self.numero = novoNumero
    
    def setTitular(self, novoTitular):
        self.titular = novoTitular
    
    def setSaldo(self, novoSaldo):
        self.__saldo = novoSaldo

    def depositar(self, deposito):
        while True:
            if deposito >= 1:
                self.__saldo += deposito
                break
            else:
                deposito = float(input("Informe um valor maior que 0 para depositar: "))

    def sacar(self, saque):
        while True:
            if saque <= self.__saldo:
                self.__saldo -= saque
                break
            else:
                saque = float(input(f"Informe um valor menor que {self.__saldo}: "))

    def transferir(self, contaDestino, valor):
        if isinstance(contaDestino, Conta) and valor <= self.__saldo:
            contaDestino.__saldo += valor
            self.__saldo -= valor
            print("Transferencia realizada com sucesso")
        else:
            print("A conta não existe ou seu saldo é insuficiente")
    
            
    def __str__(self):
        return f"Numero: {self.numero} || Titular: {self.titular} || Saldo: {self.__saldo}"

c1 = Conta('112233', 'Mauricio', 10000)
c2 = Conta('52321', 'Claudio', 500)

print(c1)
print(c2)

c1.depositar(0)

print(c1.getSaldo())

c1.sacar(100000)
    
print(c1.getSaldo())

c1.transferir(c2,100)
print(c2.getSaldo())
print(c1.getSaldo())