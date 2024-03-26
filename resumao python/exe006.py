#  A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que
# trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular
# com um acréscimo de 50%. Escreva um algoritmo/programa que leia o número de
# horas trabalhadas em um mês, o salário por hora e escreva o salário total do
# funcionário, que deverá ser acrescido das horas extras, e caso tenham sido
# trabalhadas.
# (Considere que o mês possua 4 semanas exatas).
# Variáveis para entrada de dados
horas_trab_mes = float(input("Digite o número de horas trabalhadas no mês: "))
salario_hora = float(input("Digite o salário por hora: "))


horas_semana = 40


if horas_trab_mes > (4 * horas_semana):
    horas_extras = horas_trab_mes - (4 * horas_semana)
else:
    horas_extras = 0


salario_total = (4 * horas_semana * salario_hora) + (horas_extras * salario_hora * 1.5)

print("O salário total do funcionário é: R$", salario_total)
