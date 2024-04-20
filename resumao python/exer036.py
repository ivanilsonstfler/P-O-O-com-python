# 34. Reescreva o exercício anterior uƟlizando a estrutura ENQUANTO. 

valor1 = float(input("Digite o primeiro valor: "))
valor2 = 0

while valor2 == 0:
    valor2 = float(input("Digite o segundo valor (não pode ser zero): "))
    if valor2 == 0:
        print("VALOR INVALIDO")

print("O resultado da divisão é: ", valor1 / valor2)

