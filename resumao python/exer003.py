# 3. Faça um programa que leia um caractere e indique se é uma vogal ou consoante. 
caracter_letra = input('Digite uma lentra: ')


if caracter_letra in ['a','e','i','o','u', 'A','E','I','O','U']:
    print('A letra ',caracter_letra, 'é uma vogal.')

else:
    print('A letra', caracter_letra, 'é uma consoante.')