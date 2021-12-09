import json
import requests

# Импорт классов

from classd import Word_chek
from classd import Read
from classd import Initialization

print('Добро пожаловать в игру!')

user1 = Initialization(input('Введите имя первого игрока\n').upper())
user2 = Initialization(input('Введите имя первого игрока\n').upper())

print(f'{user1.name} vs {user2.name}, игра начинается!')


def correct_rus(word_user):
    '''Проверка слова'''
    s = False
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    response.encoding = 'windows-1251'
    list_word = response.text

    list_word = list_word.split('\n')

    if word_user in list_word:
        s = True
    return s

def wr_json():
    '''Запись итогов игры'''

    result = {
        "users":
            {
                "1": user1.name,
                "2": user2.name,
            },
        "word": word,
        "words": user1.words + user2.words
    }
    raw_json = json.dumps(result, ensure_ascii=False)
    with open('result.json', "w", encoding='utf-8') as data_file:
        data_file.write(raw_json)


def result():
    '''Печать итогов'''

    print(f"""Игра окончена
===============
Игрок 1 {user1.name} - {user1.score}
Игрок 2 {user2.name} - {user2.score}
===============""")
    if user1.score > user2.score:
        print(f'Победил игрок 1 - {user1.name}')
    elif user1.score == user2.score:
        print('Победила дружба!')
    else:
        print(f'Победил игрок 2 - {user2.name}')


word = Read('https://jsonkeeper.com/b/1KFW').read_question()

print(f"Ваше слово на эту игру: {word}")

while True:
    print(f"""===========
Начало раунда!
{word}""")

    for gamer in [user1, user2]:

        print(f'Ходит {gamer.name}')
        word_user = str(input().upper())

        if word_user == 'STOP':
            break
        elif word_user == word:
            print("Так не честно")

        else:

            word_s = word
            # Проверка на наличие слова в русском языке
            if correct_rus(word_user.lower()) == True:
                # Проверка на повтор слова
                if word_user not in user1.words and word_user not in user2.words:
                    for i in word_user:
                        if i not in word:
                            print(f'Нет такого слова в слове - {word}')
                            break
                        else:
                            word_s = word_s.replace(i, '-', 1)
                    gamer.words.append(word_user)
                    gamer.score += len(gamer.words[-1])
                    print('Слово принято')
                else:
                    print('Это слово уже было')



            else:
                print('Нет такого слова в нашем языке')

    if word_user == 'STOP':
        break

result()
wr_json()
