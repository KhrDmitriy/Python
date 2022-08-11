
# summa = 100                       # Начальное число конфет.
# i = 0                             #
# count = 0                         # Счётчик
# while summa != 0:                 # ПОКА Начальное число конфет не равно 0.
#     if i == 0:
#         print('Player 1, возьми конфеты (от 1 до 28):')
#         n = int(input())          # Число конфет.
#         while n < 1 or n > 28:    # ПОКА n меньше 1 ИЛИ больше 28.
#             print('!!!!!!')       # При выполнении условия while.
#             n = int(input())      # Вводим число конфет.
#         summa = summa - n         # Каждую итерацию уменьшем общее число конфет на n.
#         print(f'Пользователь взял {n} конфет\n Осталось {summa} конфет')
#         i = 1
#     else:
#         print('Player 2, возьмити конфеты(от 1 до 28): ')
#         n = int(input())
#         while n < 1 or n > 28:
#             print('!!!!!!')
#             n = int(input())
#         summa = summa - n
#         print(f'Пользователь взял {n} конфет\n Осталось {summa} конфет')
#         i = 0
# if i == 1:
#     print('Player 1 выиграл')
# else:
#     print('Player 2 выиграл')



# С Игрок и ИИ.

summa = 100
i = 0
count = 0
while summa != 0:
    if i == 0:
        print('Сейчас ходит пользователь, возьмите определенное кол-во конфет(от 1 до 28): ')
        n = int(input())
        while n < 1 or n > 28:
            print('!!!!!!')
            n = int(input())
        summa = summa - n
        print(f'Пользователь взял {n} конфет\n Осталось {summa} конфет')
        i = 1
    else:
        count = summa % 29
        summa = summa - count
        print(f'ИИ взял {count} конфет\nОсталось {summa} конфет')
        i = 0
if i == 1:
    print('Пользователь выиграл')
else:
    print('ИИ выиграл')