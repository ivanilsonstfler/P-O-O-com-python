# . O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá 
# ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los.

valor1 = int(input("Digite o primeira valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor2 < valor1:
    valor1, valor2 = valor2 , valor1


soma = sum(range(valor1, valor2 + 1))

print("A soma dos inteiros entre", valor1, "e", valor2, "é:", soma)
