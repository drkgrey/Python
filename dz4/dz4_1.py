# 1.Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, hours_param, salary_param, bonus_param = argv
print("Выработка в часах: ", hours_param)
print("Ставка в час: ", salary_param)
print("Премия: ", bonus_param)
print("ЗП =", int(hours_param)*int(salary_param)+int(bonus_param))
