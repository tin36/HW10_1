import sys

normal = 90     #Обычная стирка
express = 20    #Быстрая стирка
cotton = 120    #Хлопок
spinning = 10   #Отжим 
rinsing = 10    #Полоскание

def calc():
    print("""Выбери режим стрики:
        N - Обычный
        E - Быстрый
        C - Хлопок""")
    i = int(sys.stdin.readline())

    print("""Включить отжим?
                    Y/N""")
    j = int(sys.stdin.readline())

    print("""Включить полоскание?
                    Y/N""")
    b = int(sys.stdin.readline())

    print(i, j, b)

calc()