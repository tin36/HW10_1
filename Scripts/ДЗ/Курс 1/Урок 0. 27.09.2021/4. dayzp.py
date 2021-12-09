day   = int(input('Какое сегодня число?\n'))
mouth = 30
avans = 10
zp    = 25
if day >= 26:
	print()
	print(f'До зарплаты {mouth-day+avans} дней')
	print()
if day == 25:
	print()
	print(f'Ура! Ура! Сегодня зарплата')
	print()
if day == 10:
	print()
	print('Ура! Ура! Сегодня аванс!')
	print()
if day <= 9:
	print()
	print(f'До зарплаты {avans-day} дней')
	print()
if day >= 11 and day <=24:
	print(f'До зарплаты {zp-day} дней')
	print()
if day == 26:
	print()
	print('Ты ж только вчера получил...')
	print()
if day == 11:
	print()
	print('Ты ж только вчера получил...')
	print()