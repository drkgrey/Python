# 2.Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(**kwargs):
    """ Вывод только введеных данных"""
    output_string = 'info: '
    for el in kwargs.values():
        output_string += str(el) + ' '
    print(output_string)


my_func(el1='name', el2='sur', el3=1900, el4='city', el5='mail', el6='phone')
my_func(name='ewq', sur='1', dob=123, city='rr', mail='#', ph='1')


