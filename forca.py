import random
import os

os.system("clear")

class Palavra:
    def __init__(self, palavra):
        self.palavra = palavra.lower().strip()
        self.letrasAcertadas = []
        for i in range(len(palavra)):
            self.letrasAcertadas.append('_')

    def verificar_letra(self, letra):
        acertou = False
        i = 0
        for ltr in self.palavra:
            if ltr == letra:
                self.letrasAcertadas[i] = letra
                acertou = True
            i += 1
        return acertou

    def mostrar_palavra(self):
        separator = " "
        result = separator.join(self.letrasAcertadas)
        print(f"Palavra: {result}")

class Jogo:
    def __init__(self):
        self.palavraAtual = None

    def iniciar_jogo(self, palavra):
        self.palavraAtual = Palavra(random.choice(palavra))
        self.jogar()

    def jogar(self):
        ganhou = False
        self.tentativasRestantes = 6
        while self.tentativasRestantes > 0:
            print(f"Tentativas restantes: {self.tentativasRestantes}")
            self.palavraAtual.mostrar_palavra()
            certo = self.palavraAtual.verificar_letra(input("Informe uma letra: "))
            if certo == False:
                self.tentativasRestantes -= 1
                print("Você errou!!!!")

            if '_' not in self.palavraAtual.letrasAcertadas:
                self.palavraAtual.mostrar_palavra()
                print("Você ganhou!!")  
                break
            
        if '_' in self.palavraAtual.letrasAcertadas:
            print("Você perdeu!!")

# Lista de palavras
palavras = ["python", "linguagem", "computador"]

# Iniciar o jogo
jogo = Jogo()
jogo.iniciar_jogo(palavras)