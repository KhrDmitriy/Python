
# МОДУЛИ для записной книжки:

1. MAIN - управляющий/запускающий программу модуль.
    Из U_I импортируем функцию user_interface (from U_I import user_interface).

2. UI (User_Interface) (модуль пользовательского УПРАВЛЕНИЯ приложением).
    Из log имортируем функции input_data, delete_data, put_data, print_data (from log import input_data, delete_data, put_data, print_data)
    В модуле присутствует меню выбора операций над данными.

3. LOG (модуль логирования)
    Из create_data импортируем функции name_data, surname_data, phone_data, address_data (from create_data import name_data, surname_data, phone_data, address_data).
    Все обрабатывающие данные функции находятся в этом блоке, такие как:

print_data (модуль вывода информации)
put_data (модуль внесения изменений)
delete_data


