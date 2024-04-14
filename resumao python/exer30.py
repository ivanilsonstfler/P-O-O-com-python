# 30. Escrever um algoritmo/programa que leia um valor digitado pelo usuário e mostre
# a tabuada deste número de 1 até 10. 

numero = int(input("Digite um número para ver sua Tabuada:"))

for fator in range(1, 11):
    print('-'*10)
    print(f'{numero} x {fator} = { numero*fator}')