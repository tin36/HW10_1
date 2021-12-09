import random

number = random.randint(10,30)
running = True

while running:
    guess = int(input('введите целое число:'))

    if guess == number:
        print('угадал')
        running = False #остановка цикла
    elif guess < number:
        print('твое число меньше')
    else:
        print('твое число больше')

else:
    print('цикла вайл закончен')

print('Завершено')