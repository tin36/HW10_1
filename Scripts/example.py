from math import *
n = input('vvedi diapazon - ')
p = [2, 3]
count = 2
a = 5
while (count < n):
    b=0
    for i in range(2, a):
        if (i <= sqrt(a)):
            if (a % 1 == 0):
                print ('a neprost', a)
                b = 1
            else:
                pass

    if (b != 1):
        print('a prost', a)
        p = p + [a]
    count = count + 1
    a = a + 2
