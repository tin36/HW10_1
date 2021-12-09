# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
#
# Какое число является 10001-м простым числом?

def prime_number(n):
    d = 2

    while n % d != 0:
        if n < 2 and n > 0:
            n = 2
            return n

        else:
            d += 1
            if (n == d):
                return n


def prime_list(n):
    number_list = []
    index = 0
    while len(number_list) < n:
        index += 1
        number = prime_number(index)
        if number != None:
            number_list.append(number)
    return number_list[-1]


position = int(input("Введите номер числа: "))
print(f'На {position} позиции, находится число - {prime_list(position)}!')
