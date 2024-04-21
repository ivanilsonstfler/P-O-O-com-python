# Acrescente uma mensagem 'NOVO CÁLCULO (S/N)? ' ao final do exercício [37]. Se 
# for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá 
# encerrar o algoritmo/programa. 
while True:
    try:
        not1 = float(input("Digite a prieira nota:"))
        if not1 < 0 or not1 >10:
            print("nota invalida! Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada Invalida! Tente novamente.")

while True:
    try:
        nota2 = float(input("Digite a segunda nota; "))
        if nota2 < 0 or nota2 >10:
            print("Nota Invalida! Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada invalida! Tente novamente")

media = (not1 + nota2) / 2
print("A media do aluno é: ", media)

novo_calculo = input("NOVO CÁLCULO (S/N)? ")
if novo_calculo.upper() != 'S':
    
break
