#Список вопросов
questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
#Список ответов
answers = ['is', 'am', 'in']
correct = 0
name = str(input("""Привет! 
Предлагаю проверить свои знания английского!
Наберите "ready", чтобы начать!\n"""))  

#При вводе контрольного слова, выполняется проверка ответов и подсчет правильных
if name == 'ready':
    print(questions[0])
    questions_0 = str(input())
    print()
    if questions_0 == answers[0]:
        print('Ответ верный!')
        correct += 1
    else:
        print(f'Неправильно. Правильный ответ: {answers[0]}')
    print(questions[1])
    questions_1 = str(input())
    print()
    if questions_1 == answers[1]:
        print('Ответ верный!')
        correct += 1
    else:
        print(f'Неправильно. Правильный ответ: {answers[1]}')

    print(questions[2])
    questions_2 = str(input())
    print()
    if questions_2 == answers[2]:
        print('Ответ верный!')
        correct += 1
    else:
        print(f'Неправильно. Правильный ответ: {answers[2]}')

#Расчет процента верных ответов 
    proc = 100/3*correct                                            
    end = ['', 'а', 'ов']   
    print('=============================================')
    if correct == 1:                                                
        print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[0]} из 3-x верно
Это {round(proc)} процент{end[1]}.""")                          
    if correct == 2:                                                
        print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[1]} из 3-x верно
Это {round(proc)} процент{end[2]}.""")                          
    if correct == 3:                                                
        print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[1]} из 3-x верно
Это {round(proc)} процент{end[2]}.""")                          
    if correct == 0:                                                
       print(f"""Вот и все!
Вы не ответили ни на один вопрос из {len(questions)}-x верно
Это 0 процент{end[2]}.""")       

else:
    print('Кажется, вы не хотите играть. Очень жаль')