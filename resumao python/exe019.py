# 9. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$
# 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
# algoritmo/programa para ler a quanƟdade (em Kg) de morangos e a quanƟdade (em Kg)
# de maças adquiridas e escreva o valor a ser pago pelo cliente. 
kg_morango = float(input("Digite a quantidade em kg de morango: "))
kg_maca = float(input("Digite a quantidade em kg de maçãs: "))

preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

preco_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)

if preco_total > 25.00 or (kg_morango + kg_maca) > 8:
    desconto = preco_total * 0.10
    preco_total = preco_total - desconto
    
print("O valor total a ser pago é: R$ ", preco_total)
