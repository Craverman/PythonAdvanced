dic = ['attribute', 'класс', 'функция', 'type']
for el in dic:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f"this word {el} can't be converted to bytes")

