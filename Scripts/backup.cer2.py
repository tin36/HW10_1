import os
import time

source = ['"D:\\Test"', 'C:\\Code']

target_dir = 'D:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
target = today + os.sep + now + '.zip'

zip_command = "C:\Program Files (x86)\GnuWin32\bin\zip.exe - qr {0} {1}".format(target, ' '.join(source))


if os.system(zip_command) == 0:
    print('Успех')
else:
    print('Не успех')