# Crie um programa que verifique se um caractere inserido pelo usuário é uma letra
# maiúscula ou minúscula
caractere = input("Digite um caractere: ")

if caractere >= 'A' and caractere <= 'Z':
    print("O caractere é uma letra Maiuscula")
elif caractere >= 'a' and caractere <= 'z':

    print("O caractere é minusculo.")
else:
    print("O caractere não é lentra.")