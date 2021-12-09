import json
import random
import requests

print('Добро пожаловать в игру!')
gamer_1 = input('Введите имя первого игрока\n').upper()
gamer_2 = input('Введите имя второго игрока\n').upper()

print(f'{gamer_1} vs {gamer_2}, игра начинается!')

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


def read_question(link):
    '''Получение слова из списка слов'''
    word = ''
    questions_dict = json.loads(requests.get(link).text)
    random.shuffle(questions_dict['word'])
    word = questions_dict['word'][0]
    return word.upper()


def correct_rus(word_rus):
    '''Проверка слова'''
    s = False
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    response.encoding = 'windows-1251'
    list_word = response.text

    list_word = list_word.split('\n')

    if word_rus in list_word:
        s = True
    return s


word = read_question('https://jsonkeeper.com/b/1KFW')
result['word'] = word
result['users']['1'] = gamer_1
result['users']['2'] = gamer_2

print(f"Ваше слово на эту игру: {word}")
word_list = list(word)

while True:
    russian_words = open('russian.txt', 'r', encoding="windows-1251")
    print(f"""===========
Начало раунда!
{word}""")
    word_user = ''
    for gamer in list_gamers:

        print(f'ходит {gamer}')
        word_user = str(input().upper())
        word_user_list = list(word_user)

        if word_user == 'STOP':
            break
        else:
            if correct_rus(word_user.lower()) == True:
                lists = []
                #Разбиваем слово по буквам
                word_list = list(word)
                #Перебираем буквы в слове от пользователя
                for i in word_user_list:
                    #Если буква есть в списке букв загаданного слова, продолжаем
                    if i in word_list:
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

print(list_gamers)
print(f"""Игра окончена
===============
Игрок 1 {gamer_1} - {list_gamers[gamer_1]['score']}
Игрок 2 {gamer_2} - {list_gamers[gamer_2]['score']}
===============""")
if list_gamers[gamer_1]['score'] > list_gamers[gamer_2]['score']:
    print(f'Победил игрок 1 - {gamer_1}')


def wr_json():
    raw_json = json.dumps(result, ensure_ascii=False)
    with open('result.json', "w", encoding='utf-8') as data_file:
        data_file.write(raw_json)


wr_json()
