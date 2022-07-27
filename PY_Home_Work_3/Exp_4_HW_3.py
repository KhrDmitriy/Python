

def binary_number(Num):
    b=''                                #Пустая строка.
    while Num > 0:                      #Пока число больше 0.
        b=str(Num%2)+b                  #Получение остатка от деления.
        Num=Num//2                      #Целочисленное деление на 2.
    print(b)
print()
Number=int(input("Введите десятичное число: "))  
binary_number(Number)



# Второй вариант через функцию bin.

def binary_number(Num):
    print(f'{Num:b}')   #Вывод без префикса 0b.
Number=int(input("Введите десятичное число: "))  
binary_number(Number)



