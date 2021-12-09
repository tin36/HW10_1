normal   = 90     #Обычная стирка
express  = 20     #Быстрая стирка
cotton   = 120    #Хлопок
spinning = -10     #Отжим 
rinsing  = 10     #Полоскание

nsr = normal  + spinning + rinsing
ns  = normal  + spinning
nr  = normal  + rinsing
esr = express + spinning + rinsing
es  = express + spinning
er  = express + rinsing
csr = cotton  + spinning + rinsing
cs  = cotton  + spinning
cr  = cotton  + rinsing


def calc():
    print("""Выбери режим стрики:
        1 - Обычный
        2 - Быстрый
        3 - Хлопок""")
    i = int(sys.stdin.readline())

    print("""Выключить отжим?
        1 - Да
        2 - Нет""")
    j = int(sys.stdin.readline())

    print("""Включить полоскание?
        1 - Да
        2 - Нет""")
    b = int(sys.stdin.readline())

    if  i == 1 and j == 1 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % nsr)
    if  i == 1 and j == 1 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % ns) 
    if  i == 1 and j == 2 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % normal) 
    if  i == 1 and j == 2 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % nr) 

    if  i == 2 and j == 1 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % esr) 
    if  i == 2 and j == 1 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % es) 
    if  i == 2 and j == 2 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % er) 
    if  i == 2 and j == 2 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % express)

    if  i == 3 and j == 1 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % csr) 
    if  i == 3 and j == 1 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % cs) 
    if  i == 3 and j == 2 and b == 1:
        print('Всего времени на стрирку уйдет: %s минут' % cr) 
    if  i == 3 and j == 2 and b == 2:
        print('Всего времени на стрирку уйдет: %s минут' % cotton)


calc()