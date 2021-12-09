questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
end = ['', 'а', 'ов']  

score = 0 #очки заработанные пользователем  
answer_question = 0 #правильные ответы
total_question = 0 #счетчик вопросов
procent_answer_question = 0 #процент правильных ответов
points = 3 #очки за верный ответ     

#записываем в переменную количество вопросов, по меньшему значение списков вопросов или ответов
if len(questions) <= len(answers):
  total_question = len(questions)
else:
  total_question = len(answers)

#Приветсвие и ввод контрольного слова
while True:
  print('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать!')
  start = input()
  if start == 'ready':
    break
  print("Кажется, вы не хотите играть. Очень жаль.")

#блок вопросов и подсчета очков
for question_index in range(total_question):
  print()
  print(questions[question_index])
  user_answer = input()
  points = 3
  while True:
    if user_answer == answers[question_index]:
        if points == 1:
          print(f'Ответ верный! Ты заработал {points} балл')
        elif points == 1 or points == 3:
          print(f'Ответ верный! Ты заработал {points} баллa')
        score += points
        answer_question += 1
        break
    else:
        points -= 1
        if points == 0:
            print(f'Неправильно. Правильный ответ: {answers[question_index]}')
            break
        else:
            print(f'Осталось попыток: {points}, попробуйте еще раз!')
            user_answer = input()

#Подсчет итогов
if score == 1 and answer_question == 1:                                                
  print(f"""Вот и все!
Вы ответили на {answer_question} вопрос{end[0]} из {len(questions)}-x верно
Вы набрали {score} балл{end[0]}.""") 

if score >= 2 and score <= 4:                                                
  print(f"""Вот и все!
Вы ответили на {answer_question} вопрос{end[1]} из {len(questions)}-х верно
Вы набрали {score} балл{end[1]}.""") 

if score >=5 and score <= 9:                                                
  print(f"""Вот и все!
Вы ответили на {answer_question} вопрос{end[1]} из {len(questions)}-x верно
Вы набрали {score} балл{end[2]}.""") 

if score == 0:                                                
  print(f"""Вот и все!
Вы не ответили ни на один вопрос из {len(questions)}-x верно
Это 0 балл{end[2]}.""") 
