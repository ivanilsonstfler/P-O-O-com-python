# Faça um algoritmo/programa que exiba os N primeiros termos da sequência de
# Fibonacci, onde N é fornecido pelo usuário. 

N = int(input("Digite um número: "))

a, b = 0, 1

for i in range(N):
    print(a)
    a, b = b, a + b




