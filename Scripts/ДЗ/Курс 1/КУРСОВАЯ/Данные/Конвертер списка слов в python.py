def read_word():
    with open('Список слов.txt', 'r', encoding='UTF-8') as f:

        for i in f:
            l = "".join(i for i in f if not i.isspace())
            s = l.split('\n')
            return s





print(read_word())

