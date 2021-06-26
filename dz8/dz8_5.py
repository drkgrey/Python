# 5.Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class Warehouse:
    items = dict()
    history = []

    @staticmethod
    def add_product(product, count, time):
        Warehouse.history.append(f'{product.product_name}({product.product_id}) в количестве {count}'
                                 f' был внесен на склад :{time}')
        if product in Warehouse.items.keys():
            count += Warehouse.items.get(product)
        Warehouse.items.update({product: count})

    @staticmethod
    def move_product_to(product, count, local, time):
        if product in Warehouse.items.keys() and count <= Warehouse.items.get(product):
            Warehouse.items.update({product: Warehouse.items.get(product) - count})
        else:
            print('данного товара нет на складе в нужном объеме')
        Warehouse.history.append(f'{product.product_id} в количестве {count} был отправлен со склада в {local}'
                                 f': {time}')


class OfficeEquipment:

    def __str__(self):
        return f'{self.product_name} ({self.product_id}) вес:{self.weight} цена:{self.price}'

    def __init__(self, price, weight, product_name, product_id):
        self.price = price
        self.weight = weight
        self.product_name = product_name
        self.product_id = product_id


class Printer(OfficeEquipment):

    def __init__(self, price, weight, product_name, product_id, colors):
        super().__init__(price, weight, product_name, product_id)
        self.colors = colors


class Scanner(OfficeEquipment):
    def __init__(self, price, weight, product_name, product_id, paper_size):
        super().__init__(price, weight, product_name, product_id)
        self.paper_size = paper_size


class Xerox(OfficeEquipment):
    def __init__(self, price, weight, product_name, product_id, number_of_copies):
        super().__init__(price, weight, product_name, product_id)
        self.number_of_copies = number_of_copies


zn1 = Xerox(1000, 10, 'zn1', 183432, 15)
pr1 = Printer(1200, 15, 'pr', 123992, 3)
pr2 = Printer(1500, 14, 'pr2', 128992, 5)
Warehouse.add_product(zn1, 4, '15-04-2021 21:20')
Warehouse.add_product(pr1, 5, '15-04-2021 21:20')
Warehouse.add_product(pr1, 2, '15-04-2021 21:20')
Warehouse.add_product(pr2, 2, '15-04-2021 21:20')
for el in Warehouse.items:
    print(el)
print(Warehouse.history)
Warehouse.move_product_to(pr1, 3, "склад2", '15-04-2021 21:20')
print(Warehouse.items)
print(Warehouse.history)
