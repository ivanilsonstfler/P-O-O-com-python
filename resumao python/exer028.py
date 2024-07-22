<<<<<<< HEAD
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
=======

soma = 0
contador_positivos = 0
    
for contador in range(1, 21):
        numero = float(input(f"Digite o {contador} número: "))
        if numero > 0:
            soma += numero
            contador_positivos += 1
    
if contador_positivos > 0:
        media = soma / contador_positivos
        print("A media aritmetica dos numeros positivos é:", media)
>>>>>>> 0bf459b8c1b0c8a1c97ceaf52a5f036cc04d6f83
else:
    print("Nenhum número positivo foi inserido.")

