import requests
import json
import random


class Initialization:

    def __init__(self, name):
        self.words = []
        self.name = name
        self.score = 0


class Read:
    def __init__(self, link):
        self.link = link

    def read_question(self):
        '''Получение слова из списка слов'''
        word = ''
        questions_dict = json.loads(requests.get(self.link).text)
        random.shuffle(questions_dict['word'])
        word = questions_dict['word'][0]
        return word.upper()


