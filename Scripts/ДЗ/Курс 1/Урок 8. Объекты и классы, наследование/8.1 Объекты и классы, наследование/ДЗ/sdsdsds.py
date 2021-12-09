import json
import random
import requests

from implementation import Question


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
