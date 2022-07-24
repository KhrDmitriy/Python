
def SummaOfTheNumber(N):
    N=abs(N)    # Модуль числа
    print(N)
    print(type(N))
    st=str(N)   # Превращаю число в строку.
    print(st)
    print(type(st))

    print ("Исходная строка: " + st) 
    new_str = ""         # Сюда будет записана новая строка без запятой.
    new_str=st.replace(".","")         # Здесь удаляю запятую.
    print ("Строка после удаления i-го элемента: " + new_str)
    a=int(new_str)      # Превращаю строку в число.
    print(a)

    last = 0   
    sum=0
    while a > 0:
        last= a % 10        # Последняя цифра от числа(остаток от деления)
        sum=sum+last
        a = a // 10         # Исходное число без последней цифры
    sum=sum + a  
    print(sum)
    return(sum)
Num = float(input('Введите число / Enter a number -->   '))
print(Num)
SummaOfTheNumber(Num)






