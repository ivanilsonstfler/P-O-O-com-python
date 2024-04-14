soma = 0

for contador in range(1, 31):
    numero = int(input(f"Digite o {contador} número: "))
    if numero > 0:
        soma += numero
print('A soma dos 30 numeros é:', soma)
