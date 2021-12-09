import random

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

def morse_enc():
    for i in dict:
        if i == ' ':
            result.append(' / ')
        else:
            result.append(dict[i])
    return result

result = []
word_user = ['code', 'mode', 'tode']
answers = []
print("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")
user = str.lower(input())
random.shuffle(word_user)
for i in word_user:
    for z in i:
        result.append(morse_enc())


print(result)