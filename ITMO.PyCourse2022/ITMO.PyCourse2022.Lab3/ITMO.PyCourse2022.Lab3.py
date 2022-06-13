from statistics import *
from math import *
from random import *

numbers = []
for i in range(10):
    numbers.append(randint(1,100))
print(numbers)
print('сумма всех чисел: ', fsum(numbers) )
print('среднее значение: ', mean(numbers) )
print('медиана: ', median(numbers))
print('стандартное отклонение: ', stdev(numbers))
print('случайное число в интервае от 1 до 100: ', randint(1,100))

