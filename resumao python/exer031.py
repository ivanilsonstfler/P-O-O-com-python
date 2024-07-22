# . Desenvolva um algoritmo/programa que calcule e imprima o fatorial de um número
# inteiro fornecido pelo usuário. 


numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial de {} é: {}".format(numero, fatorial))



