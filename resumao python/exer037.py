# Escreva um algoritmo/programa para ler as notas da 1a e 2a avaliações de um aluno, 
# calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores 
# válidos durante a leitura (0 a 10) para cada nota.  
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