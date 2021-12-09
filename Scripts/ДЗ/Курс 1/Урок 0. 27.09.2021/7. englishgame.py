

score = 0

a = str(input('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать!\n'))

if a == 'ready':
	print('Заполни пропуск')
	b = str(input('My name ___ Vova\n'))
	if b == 'is':
		score+=1
		print('Ответ верный!')
	else:
		print('Нет, ты ответил неправильно. Правильный ответ "is"')

	print('Заполни пропуск')
	c = str(input('I ___ a coder\n'))
	if c == 'am':
		score+=1
		print('Ответ верный!')
	else:
		print('Нет, ты ответил неправильно. Правильный ответ "am"')

	print('И еще заполни пропуск')
	d = str(input('I live ___ Moscow\n'))
	if d == 'in':
		score+=1
		print('Ответ верный!')
	else:
		print('Нет, ты ответил неправильно. Правильный ответ "in"')
else:
	print('Не хочешь, как хочешь')

proc = 100/3*score

print(f'Вот и все! Вы ответили на {score} вопроса из 3 верно, это {round(proc)} процентов.')