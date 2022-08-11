# Алгоритм сжатия RLE (строка).

stroka = "aaaaacbbaaabbgwwwww"

def RLE(stroka):
    past_simbol = ""                     # Прошлый символ (для цикла for).
    new_stroka =""                         # Новая строка куда будет запись.
    count = 1                             # Счетчик начинается с 1.

    for simbol in stroka:               # Для СИМВОЛА в stroka.
                                    # Цикл проходит по каждому символу в строке.
        if simbol != past_simbol:       # ЕСЛИ simbol (текущий) НЕ РАВЕН предыдущему символу.
            if past_simbol:             # ЕСЛИ предыдущий символ.
                new_stroka += str(count) + past_simbol    # (число превращается в строку)+ добавляется предыдущий символ.
                print(new_stroka)       # Вывод текущего состояния.
            count = 1                   
            past_simbol = simbol        # Записываем в предыдущий символ текущий символ.
        else:
            count += 1                # Если символы совпадают увеличиваем счетчик на 1.
    else: 
        new_stroka += str(count) + past_simbol
        print(new_stroka)
        return(new_stroka)
RLE(stroka)


def rev_line(new_stroka):
    initial_line = '' 
    count = ''
    for simbol in new_stroka:
        if simbol.isdigit():      # Если символ является числом, возвращает число
            count += simbol
        else:
            initial_line += simbol * int(count)     # В строку добавляем символ "умноженный" на число.
            count = ''
    print(initial_line)

rev_line(RLE(stroka))