# Acrescente uma mensagem 'NOVO CÁLCULO (S/N)? ' ao final do exercício [37]. Se 
# for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá 
# encerrar o algoritmo/programa. 
while True:
    while True:
        try:
            not1 = float(input("Digite a primeira nota:"))
            if not1 < 0 or not1 >10:
                print("Nota inválida! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Tente novamente.")

    while True:
        try:
            nota2 = float(input("Digite a segunda nota: "))
            if nota2 < 0 or nota2 >10:
                print("Nota inválida! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Tente novamente")

    media = (not1 + nota2) / 2
    print("A média do aluno é: ", media)

    novo_calculo = input("NOVO CÁLCULO (S/N)? ")
    if novo_calculo.upper() != 'S':
        break
