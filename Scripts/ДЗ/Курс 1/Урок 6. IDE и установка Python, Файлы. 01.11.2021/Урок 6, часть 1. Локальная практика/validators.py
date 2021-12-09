def check_pin(pin):
    d = ','.join(pin).split(',')

    if pin.isalpha():
        return False
    if len(pin) != 4:
        return False
    if pin == '1234':
        return False
    if d[0] == d[1] == d[2] == d[3]:
        return False
    else:
        return True


def check_pass(passw):
    d = ','.join(passw).split(',')
    if len(passw) < 8:
        return False
    if passw.isalpha():
        return False
    else:
        return True


def check_mail(mail):
    if mail.count('@') == 0 or mail.count('.') == 0 :
        return False
    else:
        return True


def check_name(name):
    abc = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я ").split()
    abc.append(' ')

    for i in name:
        if i not in abc:
            return False
            break
        else:
            return True
