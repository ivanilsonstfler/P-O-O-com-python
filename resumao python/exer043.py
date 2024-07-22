# O mesmo exercício anterior, mas agora não será informado o número de
# mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler
# o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir
# o valor total em estoque e a média de valor das mercadorias em estoque.
valores = []

while True:
    valor = float(input("Digite o valor da mercadoria: "))
    valores.append(valor)

    mais_mercadorias = input("MAIS MERCADORIAS (S/N)? ")
    if mais_mercadorias.upper() != 'S':
        break

valor_total = sum(valores)

media = valor_total / len(valores)

print("O valor total em estoque é: ", valor_total)
print("A média de valor das mercadorias é: ", media)
