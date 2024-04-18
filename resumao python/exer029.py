# Escreva um algoritmo/programa que recebe o lado de 10 quadrados e mostra a área
# de cada um deles. 
for i in range(1, 11):
    lado = float(input("Digite o lado do quadrado {}: ".format(i)))
    area = lado * lado
    print("A área do quadrado {} é: {}".format(i, area))

