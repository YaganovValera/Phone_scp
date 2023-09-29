import os


def input_contact():
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()

    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        if len(user) != 3:
            print("Ошибка ввода данных!")
            return input_contact()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        try:
            command_index = int(input('Команда: '))
        except ValueError:
            print("Неверный ввод данных!")
            continue
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))


def change_contact():
    try:
        with open('data.txt', 'r+', encoding='utf-8') as f:
            contacts = f.readlines()

            user = input(
                'Введите имя, фамилию и телефон пользователя, чьи данные хотите изменить (через пробел): ').strip().split()
            if len(user) != 3:
                print("Ошибка ввода данных!")
                return

            # Проверяем, существует ли пользователь
            if not (';'.join(user) + '\n') in contacts:
                print("Пользователь не существует!")
                return

            while True:
                print('Какой параметр хотите изменить?:\n1. Имя\n2. Фамилия\n3. Телефон')
                try:
                    command_index = int(input('Команда: '))
                except ValueError:
                    print("Неверный ввод данных!")
                    continue
                if command_index not in [1, 2, 3]:
                    print('Других параметров нет.')
                else:
                    break

            data = input('Введите новые данные: ')

            # Обновляем информацию в списке контактов
            for i in range(len(contacts)):
                full_contact = contacts[i].strip().split(';')
                if user == full_contact:
                    full_contact[command_index - 1] = data
                    contacts[i] = ';'.join(full_contact) + '\n'
                    break

        # Перезаписываем файл с обновленными данными
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(contacts)

        print('Результат обновления: Данные успешно изменены.')

    except FileNotFoundError:
        print("Файл 'data.txt' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def delete_contact():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            contacts = f.readlines()

            user = input('Введите имя, фамилию и телефон пользователя, чью запись хотите удалить (через пробел): ').strip().split()
            if len(user) != 3:
                print("Ошибка ввода данных!")
                return

            # Проверяем, существует ли пользователь
            if not (';'.join(user) + '\n') in contacts:
                return print("Пользователь не существует!")

            # Удаляем строку из списка
            del contacts[contacts.index(';'.join(user) + '\n')]

        # Теперь перезаписываем файл без удаленной строки
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(contacts)

    except FileNotFoundError:
        print("Файл 'data.txt' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
