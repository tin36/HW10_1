def shift_encode(string):
    abc = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()

    words = []
    for i in string:
        if i == 'я':
            words.append('а')
        elif i == ' ':
            words.append(' ')
        else:
            for z in abc:
                if z == i:
                    abc_index = abc.index(z)
                    words.append(abc[abc_index + 1])

    print(''.join(words))


def shift_decode(string):
    abc = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()

    words = []
    for i in string:
        if i == 'а':
            words.append(abc[(abc_index + 1)])
        elif i == ' ':
            words.append(' ')
        else:
            for z in abc:
                if z == i:
                    abc_index = abc.index(z)
                    words.append(abc[abc_index - 1])

    print(''.join(words))


shift_encode('ваня')

