questions = {
    "Транспорт": {
        "100": {"question": "plane", "answer": "самолет", "asked": False},
        #"200": {"question": "train", "answer": "поезд", "asked": False},
        #"300": {"question": "boarding", "answer": "посадка", "asked": False}

    },
    "Животные": {
        #"100": {"question": "dog", "answer": "собака", "asked": False},
        #"200": {"question": "shark", "answer": "акула", "asked": False},
        #"300": {"question": "sparrow", "answer": "воробей", "asked": False}

    },
    "Еда": {
        "100": {"question": "apple", "answer": "яблоко", "asked": False},
        #"200": {"question": "berry", "answer": "ягода", "asked": False},
        #"300": {"question": "venison", "answer": "оленина", "asked": False}
    },
}
score = 0
answer = 0
round_game = 0
correct_answer = 0
fields = {}


def playing_field():
    for i in questions:
        fields[i] = []
        for z in questions[i]:
            fields[i].append(z)

    return fields


def game_over():
    print(f"""У нас закончились вопросы!
Ваш счет: {score}
Верных ответов: {correct_answer}
Неверных ответов: {round_game - correct_answer}""")


def summ_bet():
    keys = 0
    for i in fields.keys():
        keys += len(fields[i])
    return keys


def user_questions(user):
    list_bet = user.split(' ')
    return list_bet


playing_field()

while round_game < summ_bet():
    for i in fields:
        print(f'{i.ljust(9)} {"  ".join(fields[i])}')
    user = input('Выбераем категорию\n').title()
    if len(user_questions(user)) == 2:
        user_category = user_questions(user)[0]
        user_bet = user_questions(user)[1]

        if user_category in questions.keys() and user_bet in fields[user_category]:
            question = questions[user_category][user_bet]["question"]
            print(f'Слово {question} в переводе означает...')
            user_answer = input('Ваш ответ...\n').lower()
            if user_answer == questions[user_category][user_bet]["answer"]:

                score += int(user_bet)

                print(f"Верно, +{user_bet}. Ваш счет = {score}")

                index_list = fields[user_category].index(user_bet)
                fields[user_category][index_list] = '   '
                questions[user_category][user_bet]['asked'] = True
                round_game += 1
                print(questions)

            else:

                score -= int(user_bet)
                print(
                    f"Неверно, на самом деле – {questions[user_category][user_bet]['answer']}, -{user_bet}. "
                    f"Ваш счет {score}")
                index_list = fields[user_category].index(user_bet)
                fields[user_category][index_list] = '   '
                round_game += 1
        else:
            print('Такого вопроса нет, попробуйте еще раз!')
    else:
        print('Такого вопроса нет, попробуйте еще раз!')

for i in questions:
    for z in questions[i]:
        if questions[i][z]["asked"]:
            correct_answer += 1

game_over()

with open('questions.json', 'a') as file:
    file.write(f"""- points {score}
    -correct {correct_answer}
     -incorrect {round_game - correct_answer}\n""")