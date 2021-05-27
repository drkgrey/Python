# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# создание базы товаров
def check(text):
    a = input(f'введите {text}')
    while not a.isdigit():
        print('неверный ввод, повторите попытку')
        a = input(f'введите {text}')
    return a


i = 1
goods_list = []
while True:
    goods_list.append(tuple((i, {"название": input('введите название товара'),
                                 "цена": check('цену'),
                                 "количество": check('количество'),
                                 "ед": input('введите единицу измерения')})))
    i += 1
    if input('ввести еще товар? Нажмите N чтобы выйти') == 'n':
        break
print(goods_list)

# реализация словаря с исключением повторов параметров через List
analytics_dict = {"название": [], "цена": [], "количество": [], "ед": []}
param_list = analytics_dict.keys()
for good in goods_list:
    for param in param_list:
        analytics_dict[param].append(good[1].get(param))
for par in analytics_dict.keys():
    for param in analytics_dict[par]:
        while analytics_dict[par].count(param) != 1:
            analytics_dict[par].remove(param)
print(analytics_dict)

# реализация словаря без исключения повторов (кроме "ед") через List
analytics_dict = {"название": [], "цена": [], "количество": [], "ед": []}
param_list = analytics_dict.keys()
for good in goods_list:
    for param in param_list:
        analytics_dict[param].append(good[1].get(param))
for param in analytics_dict["ед"]:
    while analytics_dict["ед"].count(param) != 1:
        analytics_dict["ед"].remove(param)
print(analytics_dict)


# реализация через set
analytics_dict = {"название": set(), "цена": set(), "количество": set(), "ед": set()}
param_list = analytics_dict.keys()
for good in goods_list:
    for param in param_list:
        analytics_dict[param].add(good[1].get(param))
print(analytics_dict)

