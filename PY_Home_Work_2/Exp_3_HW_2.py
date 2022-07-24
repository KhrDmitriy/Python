
import numbers

numbers = [1, 7, 9, 0]

def max2_num(numbers):
    Max=max(numbers)
    index_Max=numbers.index(Max)
    print('Index Max=', index_Max)
    print('Max=',(Max))

    del numbers[index_Max]
    print(numbers)
    Max2=max(numbers)
    print(Max2)
    return Max2
max2_num(numbers)





# Второй вариант.

arr = [1, 7, 9, 0] 

def max2_num(arr):
    max_1=0                          # В начале цикла max=0.
    for num in arr:                 # ДЛЯ числа В МАССИВЕ (по "размеру").
        if num > max_1:              # Если число больше MAX.
            max_1=num                # ТОГДА MAX = числу.
    print(max_1)                     # ВЫВОД MAX первое максимальное число.
    arr.remove(max_1)                # Удаляю первое MAX число
    print(arr)
    max_2=0
    for num in arr:                 # ДЛЯ числа В МАССИВЕ (по "размеру").
        if num > max_2:              # Если число больше MAX.
            max_2=num                # ТОГДА MAX = числу.
    print(max_2)                     # Второе максимальное число.
max2_num(arr)










