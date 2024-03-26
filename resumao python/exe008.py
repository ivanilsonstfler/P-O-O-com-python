#Escreva um programa que determine se um ano  é bissexto ou não. 
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 ):
    print(" O ano é bissexto.")
else:
    print("não é bissexto.")
 