# Мимикрия
#
# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
#
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# или любой другой список transformed_values = list(map(transformation, values))
#
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
#
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
#
# Напишите такое лямбда- выражение transformation, чтобы transformation_values
# получился копией values. Переменная transformation должна быть глобальной, чтобы 
# проверяющая система смогла его найти. Кроме transformation вам ничего писать не нужно.
# Печать на экран - тоже.
#
# ПРИМЕР.
#
# Ввод
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#   print('ok')
# else:
#   print('fall')



import copy

def transformation(x):
   return copy.copy(x) 

values = [2, 3, 5, 7, 11, 13, 19, 23, 29]
transformed_values = list(map(transformation, values))

print(id(values))
print(id(transformed_values))

print(values)                   # Для визуальной проверки)))
print(transformed_values)       # Для визуальной проверки)))

if values == transformed_values:
    print('ok')
else:
    print('fail')