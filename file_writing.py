from get_data import last_names, get_name, telephone, info, dic
from pathlib import Path

phonebook = dic(last_names(), get_name(), telephone(), info())


def writing_scv(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    with open(file, 'a', encoding='utf-8') as data:
        data.write('№,Фамилия,Имя,Номер телефона,Описание\n')
        for k, v in phonebook.items():
            data.write(
                f'{k},{v[0]},{v[1]},{v[2]},{v[3]}\n')


def writing_txt(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.txt')
    with open(file, 'a', encoding='utf-8') as data:
        for k, v in phonebook.items():
            data.write(
                f'№ {k}\n\nФамилия: {v[0]}\n\nИмя: {v[1]}\n\nНомер телефона: {v[2]}\n\nОписание: {v[3]}\n\n\n')

def last_key():
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return new_key + 1

writing_txt(phonebook)
writing_scv(phonebook)
