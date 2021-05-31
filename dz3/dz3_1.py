# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_input():
    while True:
        a = input('введите первое число')
        if a.isdigit():
            break
        else:
            print('неверный формат ввода')
    return int(a)


try:
    print((lambda a, b: a/b)(my_input(), my_input()))
except ZeroDivisionError:
    print('на ноль делить нельзя')
