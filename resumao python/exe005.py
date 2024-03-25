# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas
# inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o
# tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um
# dia e terminar no dia seguinte. 
hora_inicio = int(input('Digite a hora do inicio do jogo: '))
hora_fim = int(input('Digite a hora do fim do jogo: '))

if hora_fim >= hora_inicio:
    duraçao = hora_fim - hora_inicio
else:
    duraçao = (24 - hora_inicio) + hora_fim

print('A duraçao do jogo foi de ', duraçao, 'horas.')