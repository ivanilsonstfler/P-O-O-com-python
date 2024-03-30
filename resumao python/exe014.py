# Crie um programa que calcule o preço final de um produto com base em seu preço
# original e em um desconto informado pelo usuário. 
preco_original = float(input("Digite o preço original: "))
desconto = float(input("Digite o valor do desconto(em percentual): "))

preco_final = preco_original - (preco_original * desconto / 100)

print('O preço final do produto com desconto é: ', preco_final)