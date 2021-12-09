import random

words = []
index = 0
score = 0

history_score = []
gamers = []
#Открываем два файла, с обычными словами и со словами, более 9 символов
#Получаем два списка. В онодм - 4 простых слова, в другом одно сложное
def read_file_word(file_name):
    '''
    Читаем файл со словами,
    выбираем четыре слова из списка
    Можно использовать для списков слов, разной сложности'''
    with open(file_name, 'r') as file:
        content = file.read().replace('\n', ' ')
        words_full = content.split(' ')
        words_easy = random.sample(words_full, 4)
        return words_easy


def add_history(name, score):
    '''
    Добавляем результаты игры
    '''
    with open('history.txt', 'a') as file:
        file.write(f'{name}: {score} \n')



# Складываем два списка в один (4 простых слова и 4 сложных) и перемешиваем слова.
words = random.sample(read_file_word('words_top.txt') + read_file_word('words.txt'), 8)

#Получаем ответы от пользователя. За сложое слово, начисляется 20 очков.
name = str(input("Введите Ваше имя:\n"))
for i in words:
    wr = words[index]
    wrs = ''.join(random.sample(wr, len(wr)))
    print(wr)

    word = str(input(f'Угадайте слово: {wrs}\n'))

    if word.lower() == words[index]:
        if len(words[index]) >= 9:
            score += 20
            index += 1
            print(f'Верно! Вы получаете 20 очков')
        else:
            score += 10
            index += 1
            print(f'Верно! Вы получаете 10 очков')

    else:
        print(f'Неверно! Верный ответ - {words[index]}')
        index += 1

#Добавляем результат игры в файл
add_history(name, score)

games = 0

#Получаем максимальный результат
with open('history.txt', 'r') as file:
    for i in file:
        games += 1
        name, scores = i.rstrip('\n').split(":")
        history_score.append(scores)
        gamers.append(name)
    max_score = max(history_score)
    t = history_score.index(max(history_score))
    gamer = gamers[t]
    print(t)

#Сообщаем о рекорде, если он побит и выводим результат
if max_score == scores:
        print(f'Вы побили рекорд! {max_score} баллов')
        print(f"""Всего игр сыграно: {games}
Максимальный рекорд: {max_score} и это твой рекорд!""")
else:
    print(f"""Вы заработали: {scores} баллов.
Всего игр сыграно: {games}
Максимальный рекорд: {max_score}, у игрока: {gamer}""")