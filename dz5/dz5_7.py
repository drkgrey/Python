# 7.Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open("dz5_7.txt", encoding='utf-8') as base_f:
    firms_dict = dict()
    average_profit_dict = dict()
    final_list = []
    total_profit = 0
    count = 0
    for line in base_f:
        split = line.split()
        profit = int(split[2]) - int(split[3])
        if profit > 0:
            total_profit += profit
            count += 1
        firms_dict.update({split[0]: profit})
    average_profit_dict = {'average profit': '{:.2f}'.format(total_profit/count)}
    final_list.append(firms_dict)
    final_list.append(average_profit_dict)
    print(final_list)
with open("result.json", 'w') as write_f:
    json.dump(final_list, write_f)
