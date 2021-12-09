# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

import math


def compute():
    answer = 1
    for i in range(1, 21):
        answer *= i // math.gcd(i, answer)
    return answer


if __name__ == "__main__":
    print(compute())
