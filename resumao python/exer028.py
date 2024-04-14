
soma = 0
contador_positivos = 0
    
for contador in range(1, 21):
        numero = float(input(f"Digite o {contador} número: "))
        if numero > 0:
            soma += numero
            contador_positivos += 1
    
if contador_positivos > 0:
        media = soma / contador_positivos
        print("A media aritmetica dos numeros positivos é:", media)
else:
    print("Nenhum número positivo foi inserido.")

