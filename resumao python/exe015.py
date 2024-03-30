time_A = input('Digitte o nome do time A:')
time_B = input('Digite o nome do time B: ')

gols_A = input('Digitte o numero de gols A:')
gols_B = input('Digite o numero de gols B: ')

 
if gols_A > gols_B:
    print('O vencedor é:', time_A)
elif gols_B > gols_A:
    print('O vencedor é:', time_B)
else:
    print("EMPATE")