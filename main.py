from logger import *


def menu():
    text = '' \
           "Главное меню:\n" \
           "1. Добавить контакт\n" \
           "2. Посмотреть все контакты\n" \
           "3. Найти контакт\n"\
           "4. Изменить контакт\n"\
           "5. Удалить контакт\n"
    print(text)
    while True:
        try:
            comand = int(input('Введите команду: '))
        except ValueError:
            continue

        if comand == 1:
            input_contact()
        if comand == 2:
            print_contacts()
        if comand == 3:
            find_contact()
        if comand == 4:
            change_contact()
        if comand == 5:
            delete_contact()
        if comand == 0:
            break
        print('_' * 30)


if __name__ == '__main__':
    menu()
