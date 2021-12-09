

import os                                              #Модуль os позволяет работать с файловой системой, с окружением, управлять процессами
import time
print(os.getcwd())                                                     #Time - модуль для работы со временем в Python.
os.chdir(r'C:\\Program Files (x86)\GnuWin32\bin')                               #Указываем путь к архиватору

source = ['"D:\YandexDisk\YandexDisk\Личка\Chevrolet Cruze"', 'C:\\Code']                                             #Собираем папки, которые будут копироваться в список

target_dir = 'd:\\backup'                                                       #Путь к каталогу, в котором будут

target = target_dir + os.sep + time.strftime('%Y_%m_%d_%H-%M-%S') + '.zip'

zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Успех')
else:
    print('Не успех')