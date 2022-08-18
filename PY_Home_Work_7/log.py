
from create_data import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input("В каком формате Вы хотите записать данные?\n\n"
                    "1 Вариант:\n\n"
                    "ФАМИЛИЯ\n"
                    "ИМЯ\n"
                    "ТЕЛЕФОН\n"
                    "АДРЕС\n\n"
                    "2 Вариант:\n\n"
                    "ФАМИЛИЯ; ИМЯ; ТЕЛЕФОН; АДРЕС\n\n"
                    "Выберите номер варианта:   "))

    while var != 1 and var != 2:                                                # ПОКА НЕ 1 вариант И НЕ 2 вариант.
        print('Неправильно введен номер варианта записи')
        var = int(input("Введите номер варианта: "))

    if var == 1:                                                                # ЕСЛИ 1 вариант записи.
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:     # Создание и добавление данных в файл.
            file.write(f'\n Имя: {name}\n Фамилия: {surname}\n Телефон: {phone}\n Адрес: {address}\n')            # Записать в файл.
    else:                                                                       # ИНАЧЕ (2 вариант записи)
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:    # Создание и добавление данных в файл.
            file.write(f'Name: {name}; Surname: {surname}; Phone: {phone}; Address: {address}\n')               # Записать в файл.



def print_data():                                                               # Функция вывода (чтения) файла (данных).
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:         # Чтение данных из 1 файла.
        data_first = file.readlines()                                           # список строк файла.
        data_first_version_second = []
        data_middle = ''                                                        # Промежуточные данные
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))                                              # Вывод данных 2 вариант.
    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:        # Чтение данных из 2 файла.
        data_second = list(file.readlines())
        print(*data_second)                                                     # Вывод данных 2 вариант.
    return data_first, data_second                                              # ВОЗВРАТ данных 1 и 2 варианты ( для дальнейшего изменения данных).


def put_data():                                                                 # Функция изменения данных.
    print('Из какого файла Вы хотите изменить данные?')                         
    data_first, data_second = print_data()                                      # Обращение к функции вывода данных (двух файлов).
    number_file = int(input('Введите номер файла: '))                           # Запрос на номер варианта исполнения данных.

    while number_file != 1 and number_file != 2:                                # ПОКА НЕ 1 вариант И НЕ 2 вариант.
        print('Неправильно введен номер варианта записи')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла                # ЕСЛИ 1 вариант файла.
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print(f'Изменить данную запись\n{data_first[number_journal]}')
        name = name_data()                                                      # Изменение данной записи.
        surname = surname_data()                                                # Изменение данной записи.
        phone = phone_data()                                                    # Изменение данной записи.
        address = address_data()                                                # Изменение данной записи.
        data_first = data_first[:number_journal] + [f' Имя: {name}\n Фамилия: {surname}\n Телефон: {phone}\n Адрес: {address}'] + \
                     data_first[number_journal + 1:]                            # Запись изменённых данных.
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:     # Изменение данных в 1 файле.
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:                                                                       # ИНАЧЕ 2 вариант.
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'Имя: {name}; Фамилия: {surname}; Телефон: {phone}; Адрес: {address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные


def delete_data():                                                                # Функция удаления данных.
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()                                        # Обращение к функции вывода данных (двух файлов).
    number_file = int(input('Введите номер файла: '))                             # Запрос на номер варианта исполнения данных.

    while number_file != 1 and number_file != 2:                                  # ПОКА НЕ 1 вариант И НЕ 2 вариант.
        print('Неправильно введен номер варианта записи')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:        # Изменение данных в 1 файле.
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные