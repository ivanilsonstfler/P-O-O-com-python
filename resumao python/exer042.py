# . Uma loja está levantando o valor total de todas as mercadorias me estoque. Escreva
# um algoritmo que permita a entrada das seguintes informações:
# a. o número total de mercadorias no estoque;
# b. o valor de cada mercadoria. Ao final imprimir o valor total em estoque e a
# média de valor das mercadorias.


5
num_mercadorias = int(input("Digite o número total de mercadorias no estoque: "))

valores = []

for i in range(num_mercadorias):
    valor = float(input(f"Digite o valor da mercadoria {i+1}: "))
    valores.append(valor)

valor_total = sum(valores)

media = valor_total / num_mercadorias

print("O valor total em estoque é: ", valor_total)
print("A média de valor das mercadorias é: ", media)
