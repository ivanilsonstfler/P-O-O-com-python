# . Faça um algoritmo/programa para ler: quanƟdade atual em estoque, quanƟdade
# máxima em estoque e quanƟdade mínima em estoque de um produto. Calcular e
# escrever a quanƟdade média ((quanƟdade média = quanƟdade máxima +
# quanƟdade mínima) /2). Se a quanƟdade em estoque for maior ou igual a
# quanƟdade média escrever a mensagem 'Não efetuar compra', senão escrever a
# mensagem 'Efetuar compra'. 
qtd_atual = float(input("Digite a quantidade atual de estoque: "))
qtd_maxima = float(input("Digite a qquantidade maxima em estoque: "))
qtd_minima = float(input("Digite  a quantidade minima em estoque: "))

qtd_media = (qtd_maxima + qtd_minima) / 2

if qtd_atual >= qtd_media:
    print("Não efetuar compra.")
else:
    print("Efetuar compra")
