import os
import statistics

os.system('clear')

i = 0
salario = []

while i < 10:
    novo_salario = float(input("Informe um salário: R$ "))
    salario.append(novo_salario)
    i += 1

print("O maior salário é: R$", max(salario))
print("O menor salário é: R$", min(salario)) 
print("A média dos salários é: R$", statistics.mean(salario))