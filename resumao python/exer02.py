# 2. Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que
# a pessoa nasceu). 



ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano que você nasceu: '))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print('Voce podera votar!')
else:
    print('Você nao esta apto a votar')
    