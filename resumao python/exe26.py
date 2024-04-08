# Escrever um algoritmo/programa que lê 10 valores e mostra a média dos valores
# lidos. 
valores = []
for _ in range(10):
    valor = float(input("Digite um valor: "))
    valores.append(valor)
media = sum(valores) / len(valores)
print("A média é:", media)
