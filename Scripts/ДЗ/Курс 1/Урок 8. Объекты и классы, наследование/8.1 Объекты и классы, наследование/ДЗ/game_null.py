import json
import random

import requests

from implementation import Question


def read_question(link):
    questions_list = []
    questions_dict = json.loads(requests.get(link).text)

    for key in questions_dict.keys():
        questions_list.append(Question(
            text=key,
            creator=questions_dict[key]['creator'],
            difficulty=questions_dict[key]['difficulty'],
            answers=questions_dict[key]['answers'],
            theme=questions_dict[key]['theme']
        ))
    return questions_list


questions = read_question('https://jsonkeeper.com/b/XUXO')
random.shuffle(questions)

for question in questions:
    print(f"""Вопрос номер: {questions.index(question) + 1}. Сложность: {question.difficulty}/5
Тема: {question.theme}
Автор: {question.creator}""")


    user_answer = input().title()

    if user_answer == 'stop':
        break

    question.user_answer = user_answer
    question.is_asked = True

    if question.is_correct():

        print(f'Верно! Ты заработал {question.score} баллов')
        question.is_right = True
    else:
        print(f'Не верно! Верный ответ: {question.answers[0]}')
        question.is_right = False


def statictics(questions_list):
    stats = {
        'total': 0,
        'правильно': 0,
        'score': 0
    }
    for question in questions:
        if question.is_asked:
            stats['total'] += 1
            if question.is_right:
                stats['score'] += question.score
                stats['правильно'] += question.is_right
    return stats


stats = statictics(questions)

print(f"""Вот и все! Ты ответил {stats['правильно']} {stats['total']} {stats['score']}""")
