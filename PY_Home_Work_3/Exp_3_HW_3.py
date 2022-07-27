# 1 Вариант.

def max_min(arr):
    arr = [x for x in arr if type(x) == float]

    arr_float = list()
    for i in arr:
        arr_float.append(round(i - int(i), 5))
    print(max(arr_float) - min(arr_float))
arr = [1.1, 1.2, 3.1, 5, 10.01]   
max_min(arr)


# 2 Вариант. 
# Вот только вопрос, а есть ли функция которая сама 
# убирает целую часть дроби?

def max_min(arr):
    arr2 = [int((i % 1)*100) for i in arr]
    print(arr2)
    max_1 = 0
    min_1 = 0
    for i in arr2:                 # ДЛЯ числа В МАССИВЕ (по "значению").
        if i > max_1:              # Если число больше MAX.
            max_1=i                # ТОГДА MAX = числу.
    for i in arr2:                 # ДЛЯ числа В МАССИВЕ (по "значению").
        if i < min_1:              # Если число меньше MIN.
            min_1=i                # ТОГДА MIN = числу.
    print(max_1-min_1)
arr = [1.1, 1.2, 3.1, 5, 10.01] 
max_min(arr)



# 3 Вариант

def max_min(arr):
    arr2 = []             # Объявление нового пустого списка.
    for i in arr:
        arr2.append(int((i % 1)*100))
    print(arr2)  
    max_1 = 0
    min_1 = 0
    for i in arr2:                 # ДЛЯ числа В МАССИВЕ (по "размеру").
        if i > max_1:              # Если число больше MAX.
            max_1=i                # ТОГДА MAX = числу.
    for i in arr2:                 # ДЛЯ числа В МАССИВЕ (по "значению").
        if i < min_1:              # Если число меньше MIN.
            min_1=i                # ТОГДА MIN = числу
    print(max_1-min_1) 
arr = [1.1, 1.2, 3.1, 5, 10.01]
max_min(arr)


