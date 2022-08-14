# ВСЕ РАВНЫ, КАК НА ПОДБОР.
#
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли 
# объекты имеют одинаковое значение некоторой характеристики, и возвращает True,
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
#
# ПРИМЕР 1
#
# values = [0,2, 10, 6]
# if same_by(lambda x: x%2, values):
#   print('same')
# else:
#   print('different')
#
# ПРИМЕР 2
#
# values = [1, 2, 3, 4]
# if same_by(lambda x: x%2, values):
#   print('same')
# else:
#   print('different')
#
#
#
#
values = [2, 4, 10, 8]
    
def same_by(characteristic, objects):
    if not objects:
       return True

    etalon = characteristic(objects[0])

    for i in objects:
        if characteristic(i) != etalon:
            return False
    return True


if same_by(lambda x : x % 2, values):
    print('same')
else:
    print('different')