import os
os.system("clear")

class Pedido:
    contador = 0

    def __init__(self, cliente, endereco, valor):
        Pedido.contador += 1
        self.numero = Pedido.contador  
        self.cliente = cliente
        self.endereco = endereco
        self.valor = valor
        self.status = "Pendente"

    def __str__(self):
        return f"Pedido {self.numero}: {self.cliente}, {self.endereco}, R${self.valor:.2f}, Status: {self.status}"

class Entregador:
    def __init__(self, nome, telefone, veiculo):
        self.nome = nome
        self.telefone = telefone
        self.veiculo = veiculo
        self.pedidos = []

    def aceitarPedido(self, pedido):
        if len(self.pedidos) >= 3:
            print(f"{self.nome} já atingiu o limite de 3 pedidos.")
            return
        if pedido.status == "Pendente":
            pedido.status = "Em entrega"
            self.pedidos.append(pedido)
            print(f"Pedido {pedido.numero} aceito por {self.nome}.")
        else:
            print(f"Pedido {pedido.numero} não pode ser aceito (status: {pedido.status}).")

    def finalizarEntrega(self, pedido):
        if pedido in self.pedidos and pedido.status == "Em entrega":
            pedido.status = "Entregue"
            print(f"Pedido {pedido.numero} entregue por {self.nome}.")
        else:
            print(f"Pedido {pedido.numero} não pode ser finalizado (status: {pedido.status}).")

    def __str__(self):
        return f"Entregador: {self.nome}, Telefone: {self.telefone}, Veículo: {self.veiculo}"

class SistemaEntregas:
    def __init__(self):
        self.entregadores = []
        self.pedidos = []

    def adicionarEntregador(self, entregador):
        self.entregadores.append(entregador)

    def adicionarPedido(self, pedido):
        self.pedidos.append(pedido)

    def listarPedidosPendentes(self):
        for pedido in self.pedidos:
            if pedido.status == "Pendente":
                print(pedido)

    def listarEntregadores(self):
        for i, entregador in enumerate(self.entregadores):
            print(f"{i+1}. {entregador}")

    def buscarPedido(self, numero):
        for pedido in self.pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def buscarEntregadorPorIndice(self, indice):
        if 0 <= indice < len(self.entregadores):
            return self.entregadores[indice]
        return None

    def menu(self):
        while True:
            print("\n=== SISTEMA DE ENTREGAS ===")
            print("1. Adicionar pedido")
            print("2. Listar pedidos pendentes")
            print("3. Atribuir pedido a entregador")
            print("4. Finalizar entrega")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cliente = input("Nome do cliente: ")
                endereco = input("Endereço: ")
                valor = float(input("Valor: "))
                pedido = Pedido(cliente, endereco, valor)
                self.adicionarPedido(pedido)
                print("Pedido adicionado.")

            elif opcao == "2":
                print("\nPedidos pendentes:")
                self.listarPedidosPendentes()

            elif opcao == "3":
                print("\nPedidos pendentes:")
                self.listarPedidosPendentes()
                try:
                    num_pedido = int(input("Número do pedido para atribuir: "))
                    pedido = self.buscarPedido(num_pedido)
                    if not pedido or pedido.status != "Pendente":
                        print("Pedido inválido ou já atribuído.")
                        continue
                    print("\nEntregadores:")
                    self.listarEntregadores()
                    idx = int(input("Escolha o entregador (número): ")) - 1
                    entregador = self.buscarEntregadorPorIndice(idx)
                    if entregador:
                        entregador.aceitarPedido(pedido)
                    else:
                        print("Entregador inválido.")
                except Exception as e:
                    print("Entrada inválida.")

            elif opcao == "4":
                print("\nEntregadores:")
                self.listarEntregadores()
                try:
                    idx = int(input("Escolha o entregador (número): ")) - 1
                    entregador = self.buscarEntregadorPorIndice(idx)
                    if entregador:
                        print("\nPedidos em entrega:")
                        for pedido in entregador.pedidos:
                            if pedido.status == "Em entrega":
                                print(pedido)
                        num_pedido = int(input("Número do pedido para finalizar: "))
                        pedido = self.buscarPedido(num_pedido)
                        if pedido and pedido in entregador.pedidos:
                            entregador.finalizarEntrega(pedido)
                        else:
                            print("Pedido inválido para este entregador.")
                    else:
                        print("Entregador inválido.")
                except Exception as e:
                    print("Entrada inválida.")

            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

sistema = SistemaEntregas()

entregador1 = Entregador("João", "41 1234", "Moto")
entregador2 = Entregador("Carlos", "41 4321", "Carro")
entregador3 = Entregador("Junior", "41 5678", "Van")
entregador4 = Entregador("Carlos", "41 8765", "Caminhao")

sistema.adicionarEntregador(entregador1)
sistema.adicionarEntregador(entregador2)
sistema.adicionarEntregador(entregador3)
sistema.adicionarEntregador(entregador4)

sistema.adicionarPedido(Pedido("Maria", "Rua A, 123", 45.90))
sistema.adicionarPedido(Pedido("José", "Rua B, 456", 32.50))
sistema.adicionarPedido(Pedido("Ana", "Rua C, 789", 27.30))
sistema.adicionarPedido(Pedido("Carlos", "Rua D, 321", 50.00))
sistema.adicionarPedido(Pedido("Paula", "Rua E, 654", 18.75))

sistema.menu()