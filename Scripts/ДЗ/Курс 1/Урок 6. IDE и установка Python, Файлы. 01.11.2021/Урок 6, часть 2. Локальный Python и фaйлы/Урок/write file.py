user_lan = input('кАКОЙ ЯЗЫК УЧИТЕ')
time = input('Как давно')
inst = input('Где')

with open('text3.txt', 'w') as file:
    file.write(f'{user_lan}\n')
    file.write(f'{time}\n')
    file.write(f'{inst}\n')
print('ok')