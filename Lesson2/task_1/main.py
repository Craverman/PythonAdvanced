"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv

list1 = []
with open('info_1.txt', encoding="utf8") as file:
    list1 = file.readlines()

list2 = []
with open('info_2.txt', encoding="utf8") as file:
    list2 = file.readlines()

list3 = []
with open('info_3.txt', encoding="utf8") as file:
    list3 = file.readlines()


def get_list(lines):
    list = []
    for line in lines:
        if line.__contains__("Тип системы:"):
            sys_type = line.split(':')
            list.insert(3, (sys_type[1].strip()))
            continue
        if line.__contains__("Изготовитель системы"):
            step_0 = line.split(':')
            list.insert(0, (step_0[1].strip()))
            continue
        if line.__contains__("Название ОС:"):
            name_os = line.split(':')
            list.insert(1, (name_os[1].strip()))
            continue
        if line.__contains__("Код продукта"):
            code = line.split(':')
            list.insert(2, (code[1].strip()))
            continue
    return list


titles = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

with open('data_report', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(titles)
    writer.writerow(get_list(list1))
    writer.writerow(get_list(list2))
    writer.writerow(get_list(list3))
