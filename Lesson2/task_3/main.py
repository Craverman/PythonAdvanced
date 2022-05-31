"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

itemlist = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
            'items_quantity': 4,
            'items_ptice': {'computer': '200\u20ac-1000\u20ac',
                            'printer': '100\u20ac-300\u20ac',
                            'keyboard': '5\u20ac-50\u20ac',
                            'mouse': '4\u20ac-7\u20ac'}
            }

with open('file.yaml', 'w') as f_n:
    yaml.dump(itemlist, f_n, default_flow_style=False, allow_unicode=True, encoding='windows-1252')

with open("file.yaml", 'r', encoding='windows-1252') as f_o:
    readed_data = yaml.load(f_o, Loader=yaml.SafeLoader)

if itemlist == readed_data:
    print('Everything is fine')
