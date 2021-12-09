import random

answers = []
word_list = []
dict = {
    'car': '−•−• •− •−•',
    'given up': '−−• •• •••− • −• / ••− •−−•',
    'home': '•••• −−− −− •',
    'who': '•−− •••• −−−',
    'land': '•−•• •− −• −••',
    'card': '−•−• •− •−• −••',
    'telephone': "− • •−•• • •−−• •••• −−− −• •",
    'shop': '••• •••• −−− •−−•',
    'python': '•−−• −•−− − •••• −−− −•',
    'live': '•−•• •• •••− •',
    'text': '− • −••− −'

}


# Переводчик
def morse_encode(key_dict):
    key = key_dict
    return dict[key]


# Случайное слово
def get_word():
    s = list(dict)
    random_index = random.randint(0, len(s) - 1)
    random_word = s[random_index]
    return random_word  # получаем индекс списка


# Сбор статистики
def print_statistics():
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {sum(answers)}')
    print(f'Отвечено неверно: {len(answers) - sum(answers)}')


print("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")
user = input()

index = 1

# Ввод количества желаемых вопросов от пользователя
while True:
    question_quantity = int(input('Выбери количество вопросов от 5 до 10\n'))
    if question_quantity <= 4 or question_quantity >= 11:
        print('У меня нет столько вопросов')

    else:
        print('Начинаем!')
        break

# Блок вопросов, проверка на повторение слов, булевый список
while index <= question_quantity:

    key_dict = get_word()
    word = morse_encode(key_dict)

    if key_dict in word_list:
        continue

    print(f'{index} Слово: {word}')
    user_word = input()

    if user_word == key_dict:
        print(f'Верно, {key_dict}')
        answers.append(True)
        word_list.append(key_dict)
        index += 1

    else:
        print(f'Неверно, {key_dict}')
        answers.append(False)
        word_list.append(key_dict)
        index += 1

# Печать итогов
print_statistics()
