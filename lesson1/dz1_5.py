# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input('сколько выручка?'))
losses = int(input('а издержки?'))
fin_result = income - losses
if fin_result > 0:
    print('есть прибыль')
    rent = fin_result / income
    print('рентабельность - {:.2f}'.format(rent))
    employees = int(input('сколько сотрудников?'))
    result_over_employee = fin_result/employees
    print('прибыль на одного сотрудника - {:.2f}'.format(result_over_employee))
else:
    print('прибыли нет')
