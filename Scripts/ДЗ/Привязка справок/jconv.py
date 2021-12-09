dictFAFB = {}
dictFAFB_fakt = []

with open('FB_FA.txt', 'r') as file:
    for i in file:
        key, value = i.rstrip('\n').split('	')
        dictFAFB[key] = value

with open('FB_fakt.txt', 'r') as file:
    for i in file:
        data = i.rstrip('\n')
        dictFAFB_fakt.append(data)

for i in dictFAFB_fakt:
    with open('FB_FINAL.txt', 'a', encoding='UTF-8') as file:
        if i in dictFAFB.values():
            for k, v in dictFAFB.items():
                if i == v:
                    file.write(f'{i}:{k} \n')
        else:
            file.write(f'{i}:нет на остатках\n')

with open('FB_FINAL.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    c = content.count('нет')
    fb = content.count('FB-')
    for i in content:
        if i in content:
            print('Призявка справок выполнена успешно')
            print(f'Есть нулевые остатки - {c} штук')
            print(f'Всего справок: {fb}, привязано: {fb-c}')
            break
        else:
            print('Призявка справок выполнена успешно')
            print(f'Всего справок: {fb}, привязано: {fb - c}')

