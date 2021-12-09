import json
import random
import requests

# Импорт классов

from classd import Word_chek
from classd import Read
from classd import Initialization
print('Добро пожаловать в игру!')



gamer_1 = input('Введите имя первого игрока\n').upper()
gamer_2 = input('Введите имя второго игрока\n').upper()
user1 = Initialization(gamer_1)
user2 = Initialization(gamer_2)


print(f'{user1.name} vs {user2.name}, игра начинается!')

result = {
    "users": {
        "1": None,
        "2": None
    },
    "word": None,
    "words": []
}

list_gamers = {
    gamer_1: {
        'words': [],
        'score': 0},

    gamer_2: {
        'words': [],
        'score': 0}
}


def wr_json():
    '''Запись итогов игры'''
    raw_json = json.dumps(result, ensure_ascii=False)
    with open('result.json', "w", encoding='utf-8') as data_file:
        data_file.write(raw_json)


word = Read('https://jsonkeeper.com/b/1KFW').read_question()
# result['word'] = word
# result['users']['1'] = user1
# result['users']['2'] = user2

print(f"Ваше слово на эту игру: {word}")


while True:
    russian_words = open('russian.txt', 'r', encoding="windows-1251")
    print(f"""===========
Начало раунда!
{word}""")
    word_user = ''
    for gamer in list_gamers:

        print(f'ходит {gamer}')
        word_user = str(input().upper())


        if word_user == 'STOP':
            break
        else:
            if Word_chek(word_user.lower()).correct_rus() == True:

                for i in word_user:
                    if i in word:
                        word

                    if i in word:
                        word_list.pop(word_list.index(i))
                        lists.append(i)

                if len(lists) == len(word_user_list):
                    list_gamers[gamer]['words'].append(word_user)
                    list_gamers[gamer]['score'] += len(word_user_list)
                    result['words'].append(word_user)
                    print('Слово принято')

                    lists.clear()
                else:
                    print(f'Нет такого слова в слове - {word}')
                    lists.clear()
            else:
                print('Нет такого слова в нашем языке')

    if word_user == 'STOP':
        break


print(f"""Игра окончена
===============
Игрок 1 {gamer_1} - {list_gamers[user1]['score']}
Игрок 2 {gamer_2} - {list_gamers[user2]['score']}
===============""")
if list_gamers[user2]['score'] > list_gamers[user2]['score']:
    print(f'Победил игрок 1 - {user1}')

wr_json()
