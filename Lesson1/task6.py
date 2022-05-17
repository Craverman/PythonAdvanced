import chardet


rawdata = open('test_file.txt', 'rb').read()
result = chardet.detect(rawdata)
print(result)

with open('test_file.txt', encoding='utf-8') as f_n:

    for el_str in f_n:
        print(el_str)