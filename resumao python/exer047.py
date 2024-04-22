# Faça um algoritmo/programa para ler o código e o preço de 15 produtos, calcular e
# # escrever:
# a. o maior preço lido
# b. a média aritméƟca dos preços dos produtos

produtos = {}

for i in range(15):
    codigo = input(f"Digite o código do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[codigo] = preco

maior_preco = max(produtos.values())

media_preco = sum(produtos.values()) / len(produtos)

print("O maior preço lido é: ", maior_preco)
print("A média aritmética dos preços dos produtos é: ", media_preco)