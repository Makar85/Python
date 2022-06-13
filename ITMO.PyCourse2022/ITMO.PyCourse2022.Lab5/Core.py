from random import randint
import time

def input_name(num):
    print('Введите имя {:d}-го играющего ' .format(num))
    return input()

def game_core(player1, player2):
    playerOneScores = 0
    playerTwoScores = 0
    for i in range(3):
     # Моделирование бросания кубика первым играющим
     print("Игра ", i + 1)
     print('Кубик бросает', player1)
     time.sleep(2)
     n1 = randint(1, 6)
     print('Выпало:', n1)
     playerOneScores += n1
     # Моделирование бросания кубика вторым играющим
     print('Кубик бросает', player2)
     time.sleep(2)
     n2 = randint(1, 6)
     print('Выпало:', n2)
     playerTwoScores += n2

    return [playerOneScores, playerTwoScores]

def winner(player1, player2, playerOneScores, playerTwoScores):
    # Определение результата (3 возможных варианта)
    if playerOneScores > playerTwoScores:
        print('Выиграл', player1)
    elif playerOneScores < playerTwoScores:
        print('Выиграл', player2)
    else:
        print('Ничья')
