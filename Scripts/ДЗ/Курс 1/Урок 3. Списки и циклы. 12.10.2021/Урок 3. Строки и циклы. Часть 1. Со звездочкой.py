questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
end = ['', 'а', 'ов']  

#Счетчики очков за правильные ответы
scoreB = 0    
scoreC = 0  
scoreD = 0  

#Cчетчик правильных ответов                                               
correct = 0 
       
#Счетчик попыток                                                     
attemptB = 0
attemptC = 0
attemptD = 0

#Максимальное число попыток для каждого вопроса 
attempt_leftB = 3 
attempt_leftC = 3     
attempt_leftD = 3                                                

#Приветствие и ввод именя
name = str(input("""Привет!
Предлагаю проверить свои знания английского!                    
Расскажи, как тебя зовут!\n"""))                               
print('======================================')
print(f"Привет, {name}, начинаем тренировку!")                 

print("""Заполни пропуски...
  """)                                                          

print()
         
#Цикл, пока счетсик попыток меньше трех, выполняются условия                          
while attemptB < 3:
    print()
    print(questions[0])
    b = str(input())

    attemptB += 1
    attempt_leftB -= 1 
    if b != answers[0] and attempt_leftB >= 1:                                                           
        print(f'Осталось попыток: {attempt_leftB} , попробуйте еще раз!')
    if attempt_leftB == 0 and b != answers[0]:
        print(f'Увы, но нет. Верный ответ: "is"') 
    if b == answers[0]:                                                   
        correct+=1                                                    
        scoreB = 1 + attempt_leftB 
        if scoreB == 1:                                    
            print(f"""Ответ верный!
Вы получаете {scoreB} балл!""")  
        else:
            print(f"""Ответ верный!
Вы получаете {scoreB} балл{end[1]}!""") 
        break                             
    
while attemptC < 3:
    print()
    print(questions[1])
    c = str(input())  
    attemptC += 1
    attempt_leftC -= 1 
    if c != answers[1] and attempt_leftC >= 1:                                                           
        print(f'Осталось попыток: {attempt_leftC} , попробуйте еще раз!')
    if attempt_leftC == 0:
        print(f'Увы, но нет. Верный ответ: "am"') 
    if c == answers[1]:                                                   
        correct+=1                                                    
        scoreC = 1 + attempt_leftC
        if scoreC == 1:                                    
            print(f"""Ответ верный!
Вы получаете {scoreC} балл!""")  
        else:
            print(f"""Ответ верный!
Вы получаете {scoreC} балл{end[1]}!""")                                     
        
        break  

while attemptD < 3:
    print()
    print(questions[2])
    d = str(input())  
    attemptD += 1
    attempt_leftD -= 1  
    if c != answers[2] and attempt_leftD >= 1:                                                         
        print(f'Осталось попыток: {attempt_leftD} , попробуйте еще раз!')
    if attempt_leftD == 0:
        print(f'Увы, но нет. Верный ответ: "in"') 
    if d == answers[2]:                                                   
        correct+=1                                                    
        scoreD = 1 + attempt_leftD  
        if scoreD == 1:                                   
            print(f"""Ответ верный!
Вы получаете {scoreD} балл!""")  
        else:
            print(f"""Ответ верный!
Вы получаете {scoreD} балл{end[1]}!""")  
        break  
score = scoreD + scoreC + scoreB  


#Подсчет итогов   
print('=============================================')
if score == 1 and correct == 1:                                                
    print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[0]} из {len(questions)}-x верно
вы набрали {score} балл{end[0]}.""") 

if score >= 2 and score <= 4:                                                
    print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[1]} из {len(questions)}-х верно
вы набрали {score} балл{end[1]}.""") 

if score >=5 and score <= 9:                                                
    print(f"""Вот и все!
Вы ответили на {correct} вопрос{end[1]} из {len(questions)}-x верно
вы набрали {score} балл{end[2]}.""") 

if score == 0:                                                
    print(f"""Вот и все!
Вы не ответили ни на один вопрос из {len(questions)}-x верно
Это 0 балл{end[2]}.""")       