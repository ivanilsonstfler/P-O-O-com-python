# 24. Escrever um algoritmo/programa que lê 20 valores e mostra quantos destes valores
# são maiores ou iguais a 5. 
valores = [int(input("Digite um valor: "))for _ in range(20)]
maiores_que_cinco = len([valor for valor in valores if valor >= 5])
print("Número de valores maiores ou iguais a 5:", maiores_que_cinco)


