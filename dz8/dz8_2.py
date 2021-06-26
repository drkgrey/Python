# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroException(Exception):
    pass

try:
    a = int(input('введите числитель'))
    b = int(input('введите знаменатель'))
    if b == 0:
        raise DivisionByZeroException
    c = a/b
    print(c)
except ValueError:
    print('Error')
except DivisionByZeroException:
    print('деление на ноль')
else:
    print('')
finally:
    print('end')

print('continue')
