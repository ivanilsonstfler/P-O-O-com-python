# Crie um programa que receba o salário de um empregado e o percentual de
# aumento, calcule e mostre o valor do aumento e o novo salário. 



salario = float(input('Digite seu salario: '))
percentual_aumento  = float(input('Digite o percentual de aumento do salario: ')) 


valor_aumento = salario * percentual_aumento / 100
novo_salario = salario + valor_aumento

print("O valor do aumento é: ", novo_salario)

print("O novo salário é: ", novo_salario)