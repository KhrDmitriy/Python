
s = int(input('Введите точность: ')) # подсчет только до 15 знаков после запятой
pi = 0
for n in range(s):
    pi += (1 / 16 ** n) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
print('Число ПИ: ', round(pi, s))


# вариант 2
from math import acos

def value_of_pi():
    pi = round (2 * acos( 0.0 ), 15)
    print (pi)

value_of_pi()


# вариант 3
import math
print (math.pi)