questions = {
    "Транспорт": {
        "100": {"question": "plane", "answer": "самолет", "asked": False},
        "200": {"question": "train", "answer": "поезд", "asked": False},
        "300": {"question": "train", "answer": "поезд", "asked": False},
        "bet": ['100', '200', '300']
    },
    "Животные": {
        "100": {"question": "mumu", "answer": "корова", "asked": False},
        "200": {"question": "dog", "answer": "собака", "asked": False},
        "300": {"question": "cat", "answer": "кошка", "asked": False},
        "bet": ['100', '200', '300']
    },
    "Еда": {
        "100": {"question": "fish", "answer": "рыба", "asked": False},
        "200": {"question": "petuh", "answer": "петух", "asked": False},
        "300": {"question": "cook", "answer": "курица", "asked": False},
        "bet": ['100', '200', '300']
    },
}

score = 0
answer = 0
round_game = 0
while round_game <= 9:

    for i in questions:
        print(f'{i.ljust(9)} {"  ".join(questions[i])}')

    user = input('Выбераем категорию\n').title()
    list_user_bet = user.split(' ')
    user_category = list_user_bet[0]
    user_bet = list_user_bet[1]
    if user_category in questions.keys() and user_bet in questions['Еда']['bet']:
        question = questions[user_category][user_bet]["question"]
        print(question)
        user_answer = input('Ваш ответ...\n').lower()
        if user_answer == questions[user_category][user_bet]["answer"]:

            index_list = questions[user_category]['bet'].index(user_bet)
            score += int(questions[user_category]['bet'][index_list])
            print(f"Верно, +{questions[user_category]['bet'][index_list]}. Ваш счет = {score}")
            questions[user_category]['bet'][index_list] = '   '
            answer += 1
            round_game += 1

        else:

            index_list = questions[user_category]['bet'].index(list_user_bet[1])
            score -= int(questions[user_category]['bet'][index_list])
            print(
                f"Неверно, на самом деле –{questions[user_category][user_bet]['answer']}, -{questions[user_category]['bet'][index_list]}. Ваш счет {score} ")
            questions[user_category]['bet'][index_list] = '   '
            round_game += 1
    else:
        print('Такого вопроса нет, попробуйте еще раз!')


print(f"""У нас закончились вопросы!
Ваш счет: {score}
Верных ответов: {answer}
Неверных ответов: {round_game - answer}""")
