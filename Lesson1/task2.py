dic = ['Сокет', 'Разработка', 'Декоратор']
for el in dic:
    el = bytes(el, 'utf-8')
    print(el)
    print(type(el))
    print(len(el))