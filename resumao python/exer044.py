# 44. Faça um algoritmo/programa que leia 100 valores e no final, escreva o maior e o
# menor valor lido. 


valores = []

for i in range(100):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

print("O maior valor lido é: ", maior_valor)
print("O menor valor lido é: ", menor_valor)
