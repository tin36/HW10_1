dict = {'n12345678': ["1", "2", "3"],
        'n2': ["4", "5", "6"]}

for i in dict:
 
    print(f'{i.ljust(5)} {" ".join(dict[i])}')