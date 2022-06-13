from random import randint
import time

# Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
playerOneScores = 0
playerTwoScores = 0

for i in range(5):
    # Моделирование бросания кубика первым играющим
    print("Игра ", i + 1)
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    playerOneScores += n1
    # Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    playerTwoScores += n2

print(igrok1, "сумма очков: ", playerOneScores)
print(igrok2, "сумма очков: ", playerTwoScores)
# Определение результата (3 возможных варианта)
if playerOneScores > playerTwoScores:
    print('Выиграл', igrok1)
elif playerOneScores < playerTwoScores:
    print('Выиграл', igrok2)
else:
    print('Ничья')
