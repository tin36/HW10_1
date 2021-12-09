words = ['разработчики', 'сервисов', 'ориентируются', 'на', 'скорость', 'ответа', 'и', 'производительность', 'при', 'проектировании', 'архитектуры']

words_with_letter = []

for i in words:
    if 'р' in i:
        words_with_letter.append(i)

words_with_letter.sort()
print(words_with_letter)