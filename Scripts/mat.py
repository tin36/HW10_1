# файл guess_number.py
# импортируем модуль для работы со случайными числами
import random

# число попыток угадать
guesses_made = 0

# получаем имя пользователя из консольного ввода
name = input('Опять ты?! Дай хоть кликуху твою узнаю. Как звать?\n')
firstname = input('Йопта. А фамилия какая тогда?\n')
# получаем случайное число в диапазоне от 1 до 30
number = random.randint(1, 29)
print ('Тупое имя, {0} {1}! Лады. Я стал умнее, и загадал число от 1 до 30. Догогяешь? У тебя 5 попыток, басота.'.format(name, firstname))

# пока пользователь не превысил число разрешенных попыток - 6
while guesses_made < 6:
   
    # получаем число от пользователя
    guess = int(input('Введи число: '))
   
    # увеличиваем счетчик числа попыток
    guesses_made += 1

    if guess < number:
        print ('Придурок АХАХ. Твое число меньше, чем я загадал. Жги дальше...')

    if guess > number:
        print ('Не попал, твое число больше.')

    if guess == number:
        break

if guess == number:
    print ('''АлиллЛЛЛЛЛЛЛЛЛуйя, {0}! я уж думал до утра с тобой тут мучаться буду. Ты использовал {1} попыток!
    	Bсе, вали'''.format(name, guesses_made))
else:
    print ('Ну ты и кретин. Я загадал число {0}. Не возвращайся'.format(number))
   
     