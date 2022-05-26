dic = ['разработка', 'администрирование', 'protocol', 'standard']
for el in dic:
    el = el.encode('utf-8')
    print(el)
    bytes_1_enc = bytes.decode(el, 'utf-8')
    print(bytes_1_enc)



