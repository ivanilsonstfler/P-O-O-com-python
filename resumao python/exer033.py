# 33. Escreva um algoritmo/programa para ler 2 valores e se o segundo valor informado
# for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser
# aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo
# segundo valor lido. (uƟlizar a estrutura REPITA). 

while True:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor (não pode ser zero): "))
    if valor2 != 0:
        break
print("O resultado da divisão é: ", valor1 / valor2)
