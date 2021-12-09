import random

index = 0
answers = []

dict = {
'car' : '1',
'given up' : '2',
'home' : '3',
'science' : '4'
}

#Переводчик
def morse_encode():
  s = list(dict)
  repley_qwe = []
  
  index = 1
  while index<=3:
    t = get_word()
    
    if s[t] in repley_qwe:
        continue
    
    print(f'Слово {index} - {dict[s[t]]}')
    ans = input()
    if ans == s[t]:
        print('Ответ верный')
        repley_qwe.append(s[t])
        index += 1
    else:
        print(f'Ответ неверный. Правильно {s[t]}')
        repley_qwe.append(s[t])
        index += 1

#Случайное слово
def get_word():
  s = list(dict)
  index = 0
  while index < len(s):
    index += 1
    random_key = random.randint(0, len(s)-1)
    return random_key #получаем индекс списка
    

#Сбор статистики
#def print_statistics():



morse_encode()
