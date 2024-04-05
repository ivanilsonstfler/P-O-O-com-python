# . Faça um algoritmo/programa para ler: a descrição do produto (nome), a quanƟdade
# adquirida e o preço unitário. Calcular e escrever o total (total = quanƟdade adquirida
# *preço unitário), o desconto e o total a pagar (total a pagar = total - desconto),
# sabendo-se que:
# - Se quanƟdade <= 5 o desconto será de 2%
# - Se quanƟdade > 5 e quanƟdade <=10 o desconto será de 3%
# - Se quanƟdade > 10 o desconto será de 5% 



nome_produto = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade adquirida: "))  # Convertendo para inteiro
preco_unitario = float(input("Digite o preço unitário: "))  # Convertendo para float

total = qtd * preco_unitario

if qtd <= 5:
    desconto = total * 0.02  
elif qtd > 5 and qtd <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
total_pagar = total - desconto

print("Produto:", nome_produto)
print("Total: R$", total)
print("Desconto: R$", desconto)
print("Total a pagar: R$", total_pagar)


    
