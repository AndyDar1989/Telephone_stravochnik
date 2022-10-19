from os import path

def writing_scv(file_name, dict_name: dict):
    with open(file_name, 'a', encoding='utf-8') as data:
        data.write('№,Фамилия,Имя,Номер телефона,Описание\n')
        for key, val in dict_name.items():
            data.write('{}:{}\n'.format(key,val))


def writing_txt(file_name, dict_name:dict):
    with open(file_name, 'a', encoding='utf-8') as data:
        for key, val in dict_name.items():
            data.write(
                f'№ {key}\nФамилия: {val[0]}\nИмя: {val[1]}\nНомер телефона: {val[2]}\nОписание: {val[3]}\n\n')
            
def record_all(file_name, file_1, file_2):  # запись данных из всех файлов в отдельный фаил Phonebook_all.csv
     with open(file_name, 'w', encoding='utf-8') as rec_text:
        if path.exists(file_1) and path.exists(file_2):
             with open(file_1, 'r', encoding='utf-8') as text_1,\
                 open(file_2, 'r', encoding='utf-8') as text_2:
                 t_1 = text_1.readlines()
                 rec_text.write(f'Данные из телефонного справочника в файле {file_1}!\n')
                 for i, v in enumerate(t_1):
                    rec_text.write(f'{v.strip()}\n')
                 t_2 = text_2.readlines()
                 rec_text.write(f'\n\n\nДанные из телефонного справочника в файле {file_2}!\n')
                 for i, v in enumerate(t_2):
                    rec_text.write(f'{v.strip()}\n')
                 print(f'Все данные успешно занесены в файл {file_name}')
                 
                             


