# . Faça um algoritmo/programa para ler uma quanƟdade e a seguir ler esta quanƟdade
# de números. Depois de ler todos os números o algoritmo deve apresentar na tela o
# maior dos números lidos e a média dos números lidos. 
# Solicita ao usuário que insira a quantidade de números

quantidade = int(input("Digite a quantidade de números: "))

numeros = []

for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

maior_numero = max(numeros)

media = sum(numeros) / quantidade

print("O maior número lido é: ", maior_numero)
print("A média dos números lidos é: ", media)
