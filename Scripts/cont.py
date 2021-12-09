while True:
	s = input('Введи число: ')
	if s == 'выход':
		break
	if len(s) < 3:
		print ('Слишкомкоротко')
		continue
	print('достаточно, Длина строки: ', len(s))
print('Завершено')