# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    """Поиск и удаление минимального значения, возврат суммы 2х других"""
    check_list = [x, y, z]
    check_list.remove(min(x, y, z))
    my_sum = 0
    for el in check_list:
        my_sum += el
    return my_sum


def check(text):
    """Проверка на ввод числа"""
    while True:
        a = input(f'{text}\n')
        if a.isdigit():
            return int(a)
        else:
            print('неверный формат ввода')


a = check('введите первое число')
b = check('введите второе число')
c = check('введите третье число')
print(f'сумма двух наибольших аргументов: {my_func(a, b, c)}')
