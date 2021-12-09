import validators as fl


def chek():
    '''Проверка каждого поля'''
    if fl.check_name(name) == False:
        print('Некорректное имя')
    if fl.check_pin(pin) == False:
        print('Неккоректный ПИН')
    if fl.check_pass(passw) == False:
        print('Некорректный пароль')
    if fl.check_mail(mail) == False:
        print('Некорректный электронный адрес почты')
    if fl.check_name(name) and fl.check_pin(pin) and fl.check_pass(passw) and fl.check_mail(mail):
        print('Данные приняты')


pin = input('Введите PIN\n')
passw = input('Введите пароль\n')
mail = input('Введите электронный адрес\n')
name = input('Введите имя\n').lower()

chek()
