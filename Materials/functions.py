# Модуль functions для функций


def get_topmgrs(empl):
    return [n for n, s in empl.items() if s >= 100000]  # совмещение for и if 


def divide(dividend: int, divisor: int) -> int:
    """
    Функция divide принимает делимое и делитель в качестве параметров.
    Возвращает целое частное.
    """
    quotient = 0

    while dividend > 0:
        dividend -= divisor
        quotient += 1

    return quotient


def trapezoid_s(a, b, *, h=1):  # * - это явный именованный параметр,
    return h * (a+b) / 2


def sum_all(*args):
    # args - это кортеж
    total = 0
    for i in args:
        total += i

    return total


# import app
# print(app.__name__)