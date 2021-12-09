import random

answers = []  # Список с ответами
word_list = []  # В список добавляются слова, которые уже были заданы
index = 1
word = []  # Слова от пользователя
translate_morse = []  # Морзянка, очищается каждую итерацию

dict = {
    'а': '•−',
    'б': '−•••',
    'в': '•−−',
    'г': '−−•',
    'д': '−••',
    'е': '•',
    'ё': '•',
    'ж': '•••−',
    'з': '−−••',
    'и': '••',
    'й': '•−−−',
    'к': '−•−',
    'л': '•−••',
    'м': '−−',
    'н': '−•',
    'о': '−−−',
    'п': '•−−•',
    'р': '•−•',
    'с': '•••',
    'т': '−',
    'у': '••−',
    'ф': '••−•',
    'х': '••••',
    'ц': '−•−•',
    'ч': '−−−•',
    'ш': '−−−−',
    'щ': '−−•−',
    'ъ': '−−•−−',
    'ы': '−•−−',
    'ь': '−••−',
    'э': '••−••',
    'ю': '••−−',
    'я': '•−•−'

}

print("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")
user = str.lower(input())

while True:
    word_user = str.lower(input("""Ввведи слово, для перевода
Если закончил, набери: save
"""))
    if word_user == 'save':
        print('Слова записаны')
        break
    else:
        word.append(word_user)
        print(word)


# Случайное слово
def get_word():
    word_rand = random.randint(0, len(word) - 1)
    return word_rand


# Переводчик. Добавляет в список перевод каждой буквы. Перед каждой итерации, производит очистку
def morse_encode(key_dict):
    word_rand = key_dict
    translate_morse.clear()
    for i in word[word_rand]:
        translate_morse.append(dict[i])
    return translate_morse


# Сбор статистики
def print_statistics():
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {sum(answers)}')
    print(f'Отвечено неверно: {len(answers) - sum(answers)}')


# Исполняемый блок: проверка на повторение слов, проверка ответов пользователя, сбор статистики
while index <= len(word):
    key_dict = get_word()
    words = morse_encode(key_dict)

    if word[key_dict] in word_list:
        continue

    user_answer = str.lower(input(f'{index} слово: "{"".join(words)}"\n'))

    if user_answer == word[key_dict]:
        print(f'Верно, {word[key_dict]}!')
        answers.append(True)
        word_list.append(word[key_dict])
        index += 1

    else:
        print(f'Не верно, правильный ответ: {word[key_dict]}')
        answers.append(False)
        word_list.append(word[key_dict])
        index += 1

# Вывод итогов
print_statistics()
