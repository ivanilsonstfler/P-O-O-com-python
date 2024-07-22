# Escrever um algoritmo/programa que leia um valor digitado pelo usuário e mostre
# a tabuada deste número de 1 até 10. 

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))


