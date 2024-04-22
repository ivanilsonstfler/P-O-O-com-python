# Desenvolva um algoritmo/programa que converta um número decimal em sua
# representação hexadecimal. 
# Solicita ao usuário que insira um número decimal
num_decimal = int(input("Digite um número decimal: "))

num_hexadecimal = hex(num_decimal)

print("A representação hexadecimal do número é: ", num_hexadecimal[2:])
