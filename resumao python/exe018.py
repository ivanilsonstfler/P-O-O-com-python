# # . Escreva um algoritmo/programa que leia as idades de 2 homens e de 2 mulheres
# (considere que as idades dos homens serão sempre diferentes entre si, bem como as
# das mulheres). Calcule e escreva a soma das idades do homem mais velho com a
# mulher mais nova, e o produto das idades do homem mais novo com a mulher mais
# velha. 
idadeHomem01 = int(input("Digite a idade do Homem 01: "))
idadeHomem02 = int(input("Digite a idade do Homem 02: "))

idadeMulher01 = int(input("Digite a idade da Mulher 01: "))
idadeMulher02 = int(input("Digite a idade da Mulher 02: "))

if idadeHomem01 > idadeHomem02:
    homemMaisVelho = idadeHomem01
    homemMaisNovo = idadeHomem02
else:
    homemMaisVelho = idadeHomem02
    homemMaisNovo = idadeHomem01

if idadeMulher01 > idadeMulher02:
    mulherMaisVelha = idadeMulher01
    mulherMaisNova = idadeMulher02
else:
    mulherMaisVelha = idadeMulher02
    mulherMaisNova = idadeMulher01

print("Homem mais velho: ", homemMaisVelho)
print("Homem mais novo: ", homemMaisNovo)
print("Mulher mais velha: ", mulherMaisVelha)
print("Mulher mais nova: ", mulherMaisNova)