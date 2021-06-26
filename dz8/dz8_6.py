# 6.Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from dz8_1 import Data


class Mistaken(Exception):
    pass


class Warehouse:
    items = dict()
    history = []

    @staticmethod
    def add_product(product, count, time):
        count = Warehouse._validate(count)
        if product.product_id == 0 or count == 0:
            return
        Warehouse.history.append(f'{product.product_name}({product.product_id}) в количестве {count}'
                                 f' был внесен на склад :{time}')
        if product in Warehouse.items.keys():
            count += Warehouse.items.get(product)
        Warehouse.items.update({product: count})

    @staticmethod
    def move_product_to(product, count, local, time):
        count = Warehouse._validate(count)
        if product.product_id == 0:
            return
        if product in Warehouse.items.keys() and count <= Warehouse.items.get(product):
            Warehouse.items.update({product: Warehouse.items.get(product) - count})
        else:
            print('данного товара нет на складе в нужном объеме')
        Warehouse.history.append(f'{product.product_id} в количестве {count} был отправлен со склада в {local}'
                                 f': {time}')

    @staticmethod
    def _validate(count):
        try:
            if type(count) != int:
                raise Mistaken
        except Mistaken:
            print('количество задано не верно')
            return 0
        else:
            return count


class OfficeEquipment:

    def __str__(self):
        return f'{self.product_name} ({self.product_id}) вес:{self.weight} цена:{self.price}'

    def __init__(self, price, weight, product_name, product_id):
        self.price = price
        self.weight = weight
        self.product_name = product_name
        self.product_id = product_id

    @classmethod
    def create(cls, *args):
        args = cls._validate(*args)
        return cls(*args)

    @staticmethod
    def _validate(*args):
        return args


class Printer(OfficeEquipment):

    def __init__(self, price, weight, product_name, product_id, colors):
        super().__init__(price, weight, product_name, product_id)
        self.colors = colors

    def _validate(*args):
        price, weight, product_name, product_id, colors = args
        try:
            if type(price) != (int or float) or type(weight) != (int or float) or type(product_id) != (int or float):
                raise Mistaken
        except Mistaken:
            print('данные введены не корректно')
            price, weight, product_id = 0, 0, 0
        finally:
            return price, weight, product_name, product_id, colors


class Scanner(OfficeEquipment):
    def __init__(self, price, weight, product_name, product_id, paper_size):
        super().__init__(price, weight, product_name, product_id)
        self.paper_size = paper_size

    def _validate(*args):
        price, weight, product_name, product_id, paper_size = args
        try:
            if type(price) != (int or float) or type(weight) != (int or float) or type(product_id) != (int or float):
                raise Mistaken
        except Mistaken:
            print('данные введены не корректно')
            price, weight, product_id = 0, 0, 0
        finally:
            return price, weight, product_name, product_id, paper_size


class Xerox(OfficeEquipment):
    def __init__(self, price, weight, product_name, product_id, number_of_copies):
        super().__init__(price, weight, product_name, product_id)
        self.number_of_copies = number_of_copies

    def _validate(*args):
        price, weight, product_name, product_id, number_of_copies = args
        try:
            if type(price) != (int or float) or type(weight) != (int or float) or type(product_id) != (int or float):
                raise Mistaken
        except Mistaken:
            print('данные введены не корректно')
            price, weight, product_id = 0, 0, 0
        finally:
            return price, weight, product_name, product_id, number_of_copies


zn1 = Xerox.create(1000, 23, 'zx', 123332, 1)
print(zn1)
pr1 = Printer.create(1200, 15, 'pr', 123992, 3)
print(pr1)
pr2 = Printer.create(1500, '14', 'pr2', 128992, 5)
print(pr2)
Warehouse.add_product(zn1, 4, Data.create('32-02-2000'))
Warehouse.add_product(pr1, '', Data.create('15-04-2021'))
Warehouse.add_product(pr1, 2, '15-04-2021 21:20')
Warehouse.add_product(pr2, 2, '15-04-2021 21:20')
print(Warehouse.history)
for el in Warehouse.items:
    print(el)
Warehouse.move_product_to(pr1, 3, "склад2", '15-04-2021 21:20')
print(Warehouse.history)
