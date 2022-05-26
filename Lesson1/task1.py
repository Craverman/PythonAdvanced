dic = ['Сокет', 'Разработка', 'Декоратор']
for el in dic:
    print(el)
    print(type(el))
    print(el.encode('unicode_escape').decode('utf-8'))
    print(type(el))
