# 4. Crie um programa que calcule o valor total a ser pago em uma conta de restaurante,
# considerando o valor da refeição e uma taxa de serviço. 

valor_refeiçao = float(input('Digite o valor da refeiçao: '))
taxa_serviço = float(input('Digite o valor da taxa de serviço (em porcentagem): '))


valor_total = valor_refeiçao + (valor_refeiçao * taxa_serviço / 100)

print('O valor total da conta é: ', valor_total)