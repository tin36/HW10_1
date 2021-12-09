#Импорт библиотек
import json
import random
import requests

#Импорт класса
from implementation import Question


#Чтение json, запись ключей в список
def read_question(link):
    questions_list = []
    questions_dict = json.loads(requests.get(link).text)

    for key in questions_dict.keys():
        questions_list.append(Question(
            key,
            questions_dict[key]['creator'],
            questions_dict[key]['difficulty'],
            questions_dict[key]['answers'],
            questions_dict[key]['theme']
        ))
    return questions_list


questions = read_question('https://jsonkeeper.com/b/XUXO')
random.shuffle(questions)

#Перебор вопросов, проверка ответов,
for question in questions:


    print(f'Вопрос №: {questions.index(question) + 1}. {question.build_question()}')
    user = input('Ваш ответ: \n').title()
    if user == 'Stop':
        break

    question.user_answer = user
    question.is_asked = True

    if question.is_correct():
        print(f'Верно! Ты заработал {question.get_points()} баллов\n')

    else:
        print(f'Не верно! Правильный ответ: {question.answers[0]}\n')
        question.is_right = False


#подсчет итогов
def results(questions):
    total = 0
    correct = 0
    score = 0

    for i in questions:
        if i.is_asked:
            total += 1
            if i.is_right:
                score += i.score
                correct += i.is_right
    print(f"""Вот и все! Ты ответил на {total} из {len(questions)} вопросов.
Правильных ответов: {correct}
Очков: {score}""")


results(questions)
