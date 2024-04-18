# Escreva um algoritmo/programa que receba 20 números e mostre a média
# aritméƟca dos números posiƟvos recebidos.

soma = 0
contagem = 0

for i in range(20):
    numero = float(input("Digite um numero: "))
    if numero > 0:
        soma += numero
        contagem += 1

if contagem > 0:
    media = soma / contagem
    print("A média dos números positivos é:", media)
else:
    print("Nenhum número positivo foi inserido.")

