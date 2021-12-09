import sys
#print(sys.stdin.readline())

def convertCF():
    print('Введи температуру по фаренгейту:')    

    f = int(sys.stdin.readline())
    c = 5/9*(f-32)
    print('%s по фаренгейту, это - %s по цельсию' % (f, round(c, 2)))

convertCF()