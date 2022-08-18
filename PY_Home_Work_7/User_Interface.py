
from log import input_data, delete_data, put_data, print_data

def user_interface():
        print('Добро пожаловать в телефонный справочник')
        print('Мы можем выполнить следующие действия:\n'
                '1. Записать данные(2 варианта)\n'
                '2. Удалить данные\n'
                '3. Изменить данные\n'
                '4. Вывести данные\n')
        command = int(input('Введите номер опрерации:'))

        while command < 1 or command > 4:
                print('Попробуйте ввести ещё раз или попросите друга')
                command = int(input('Введите номер операции:'))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            put_data()
        else:
            print_data()









