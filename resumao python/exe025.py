# 25. Escrever um algoritmo/programa que lê 10 valores e mostra quantos destes valores
# são negaƟvos.
# Inicializa o contador de valores negativos
cont_negativos = 0

for _ in range(10):
    valor = float(input("Digite um valor: "))
    if valor < 0:
        cont_negativos += 1


print("Quantidade de valores negativos:", cont_negativos)


