scoreB = 0    
scoreC = 0  
scoreD = 0                                                    
correct = 0                                                     
attemptB = 0
attemptC = 0
attemptD = 0

attempt_leftB = 3 
attempt_leftC = 3     
attempt_leftD = 3                                                

name = str(input("""Привет!
Предлагаю проверить свои знания английского!                    
Расскажи, как тебя зовут!\n"""))                               
print('======================================')
print(f"Привет, {name}, начинаем тренировку!")                 

print("""Заполни пропуски...
  """)                                                          

print()
                          
while attemptB < 3:
    
    b = str(input('My name ___ Vova\n'))  
    attemptB += 1
    attempt_leftB -= 1 
    if b != 'is' and attempt_leftB >= 1:                                                           
        print(f'Осталось попыток: {attempt_leftB} , попробуйте еще раз!')
    if attempt_leftB == 0 and b != 'is':
        print(f'Увы, но нет. Верный ответ: "is"') 
    if b == 'is':                                                   
        correct+=1                                                    
        scoreB = 1 + attempt_leftB                                     
        print(f"""Ответ верный!
Вы получаете {scoreB} баллов!""")  
        break                             
    
while attemptC < 3:
     
    c = str(input('I ___ a coder\n'))  
    attemptC += 1
    attempt_leftC -= 1 
    if c != 'am' and attempt_leftC >= 1:                                                           
        print(f'Осталось попыток: {attempt_leftC} , попробуйте еще раз!')
    if attempt_leftC == 0:
        print(f'Увы, но нет. Верный ответ: "am"') 
    if c == 'am':                                                   
        correct+=1                                                    
        scoreC = 1 + attempt_leftC                                     
        print(f"""Ответ верный!
Вы получаете {scoreC} баллов!""") 
        break  

while attemptD < 3:
     
    d = str(input('I live ___ Moscow\n'))  
    attemptD += 1
    attempt_leftD -= 1  
    if c != 'in' and attempt_leftD >= 1: 
                                                                 
        print(f'Осталось попыток: {attempt_leftD} , попробуйте еще раз!')
    if attempt_leftD == 0:
        print(f'Увы, но нет. Верный ответ: "in"') 
    if d == 'in':                                                   
        correct+=1                                                    
        scoreD = 1 + attempt_leftD                                     
        print(f"""Ответ верный!
Вы получаете {scoreD} баллов!""") 
        break  

print(f'Вот и все! Вы ответили на {correct} вопросов из 3-х верно, вы набрали {scoreB + scoreC + scoreD} баллов.')