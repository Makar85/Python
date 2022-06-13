from Core import input_name, game_core, winner

player1 = input_name(1)
print('Добро пожаловать в игру, ' + player1)
player2 = input_name(2)
print('Добро пожаловать в игру, ' + player2)

playersScores=game_core(player1, player2)
pl1=playersScores[0]
pl2=playersScores[1]

print('Колличество очков у '+ player1 + ': ' + str(pl1))
print('Колличество очков у '+ player2 + ': ' + str(pl2))

winner(player1, player2, pl1, pl2)
