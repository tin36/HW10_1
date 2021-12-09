import random

secnumber = random.randint(10,100)
running = True

while running:
	usernumber = int(input('Введи целое число: '))
	
	if usernumber == secnumber:
		print('Угадал')
		running = False
	elif usernumber < secnumber:
		print('Твое число меньше')
	else:
		print('Твое число больше')
if usernumber == 'stop':
		break

else:
    print('цикла вайл закончен')

print('Завершено')