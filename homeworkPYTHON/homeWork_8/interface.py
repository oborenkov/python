from os.path import exists
from csv_creating import creating
from file_writing import writing_csv, writing_txt, get_info
from export import from_file


def view():
    print(from_file('Phonebook.txt'))


def record_info():
    info = get_info()
    writing_csv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Для продолжения работы нажмите \'yes\', или любой символ для завершения работы... ')
    while (flag.lower() == 'yes'):
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'yes\', если хотите записать новые данные, и любой другой символ, если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'yes':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы нажмите \'yes\', или любой символ для завершения работы... ')
    print('Программа завершена.')