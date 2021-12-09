

with open('text.txt', 'rt') as file:
    gue = len(file.readlines())
    for line in file:
        print(line)
        gue+=1

print(gue)