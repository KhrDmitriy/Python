# САМАЯ ДАЛЁКАЯ ПЛАНЕТА.
#
# Планеты вращаются вокруг звёзд по эллиптическим орбитам. 
# Назовём самой далёкой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка
# орбит планет найдёт ту, по которой вращается самая далёкая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
# зато искусственные спутники были запущены на круговые орбиты.
#
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса 
# орбиты самой далёкой планеты.
#
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей её эллипса.
# Площадь эллипса вычисляется по формуле: S = пиab, где a и b - длины полуосей элипса.
#
# При решении задачи используйте списочные выражения.
#
# Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. 
#
# Гарантируется, что самая далёкая планета ровно одна.
#
# ПРИМЕР
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


def find_farthest_orbit(arr):
    return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])]
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))










