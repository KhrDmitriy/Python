
from random import randint as rd

k = int(input('Задайте натуральную степень k: '))
arr = []
if k == 1:
    print('0')
else:   
    for i in range(k, 1, -1):
        x = rd(-100, 100)
        if x > 0:
            print(f'+{x}x^{i}', end='')
        else:
            print(f'{x}x^{i}', end='')
    x = rd(-100, 100)
    if x > 0:
        print(f'+{x} = 0', end='')
    else:
        print(f'{x} = 0', end='')
print()