import subprocess
import chardet
import time

params = ['ping', 'youtube.ru']

pinging = subprocess.Popen(params, stdout=subprocess.PIPE)
for line in pinging.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

time.sleep(3)

params = ['ping', 'yandex.ru']

pinging = subprocess.Popen(params, stdout=subprocess.PIPE)
for line in pinging.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

