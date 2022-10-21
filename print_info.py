from os import path


def print_data(file_name): # печать в консоль из файла Phonebook.csv
    if path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as text:
            new_text = text.readlines()
            for i,v in enumerate(new_text):
                print(v.strip())
    else:
        print('path does not exist')
        


