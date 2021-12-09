def printmax(x, y):
    '''vyvodit max iz 2 chisel

    oba znach dolzhny byt chiskami'''

    x = int(x) #konvertiruem celye chisla
    y = int(y)

    if x > y:
        print(x, 'naib')

    else:
        print(y, 'naib')

printmax(3,5)
print(printmax)