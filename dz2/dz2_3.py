# 3.Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['зима', 'весна', 'лето', 'осень']
season_dist = dict.fromkeys([1, 12, 2], 'зима')
season_dist.update(dict.fromkeys([3, 4, 5], 'весна'))
season_dist.update(dict.fromkeys([6, 7, 8], 'лето'))
season_dist.update(dict.fromkeys([10, 9, 11], 'осень'))

# цикл для проверки значений
while True:
    input_sen = input('введите месяц в виде целого числа от 1 до 12\n для выхода намите - s\n')
    if input_sen == 's':
        break
    while not input_sen.isdigit():
        print('введен неверный формат, повторите ввод')
        input_sen = input('введите месяц в виде целого числа от 1 до 12\n')
    month = int(input_sen)

    # решение через dist
    print(f'сезон указанного месяца - {season_dist[month]}')

    # решение через list
    if month in range(3, 6):
        print(f'{season_list[1]}')
    elif month in range(6, 9):
        print(f'{season_list[2]}')
    elif month in range(9, 12):
        print(f'{season_list[3]}')
    else:
        print(f'{season_list[0]}')
