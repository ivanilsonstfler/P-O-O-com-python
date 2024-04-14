# . Escreva um algoritmo/programa que recebe o lado de 10 quadrados
# e mostra a área de cada um deles. 


    
for contador in range(1, 11):
    
    lado = float(input(f"Digite o lado do quadrado {contador}: "))
    
    
    area = lado ** 2
    
    print(f"A área do quadrado {contador} é: {area}")
