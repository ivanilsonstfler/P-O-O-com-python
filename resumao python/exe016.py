# Crie um programa que leia uma sequência de números inteiros e exiba apenas os
# números pares
numeros = []
numero = int(input("Digite uma sequencia de numeros inteiros(digite um numero negativo para encrtta)"))
while numero >= 0:
    numeros.append(numero)
    numero = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))

print("Numeros pares na sequencia:")
for num in numeros:
    if num %2 == 0:
        print(num,end=" ")