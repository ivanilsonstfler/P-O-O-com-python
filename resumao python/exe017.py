# 7. Escreva um algoritmo/programa que leia o número de litros vendidos e o Ɵpo de
# combusơvel (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima
# o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30
litros_vendidos = float(input("Digite o numero de litros: "))
tipo_combustivel = input("Digite o tipo de combustivel(A-álcool, G-gasolina):")

if tipo_combustivel == 'G' or tipo_combustivel == 'g':
    valor_total = litros_vendidos * 3.30

elif tipo_combustivel == 'A' or tipo_combustivel == 'a':
    valor_total = litros_vendidos * 2.90

else:
    print("Tipo de combustível inválido!")
    valor_total = 0

print("Valor a ser pago pelo cliente: R$", valor_total)