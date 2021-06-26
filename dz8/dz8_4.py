# 4.Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    total_items = []


class OfficeEquipment:
    price = 0
    weight = 0
    product_name = ''
    product_id = 0


class Printer(OfficeEquipment):
    colors = []


class Scanner(OfficeEquipment):
    paper_size = 0


class Xerox(OfficeEquipment):
    number_of_copies = 0
