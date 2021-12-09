#!/usr/bin/python
#Filename: func_return.py

def maximum(x, y):
    if x > y:
        print(x)

    elif x== y:
        return 'ravno'

    else:
        print(y)
print(maximum(3, 3))