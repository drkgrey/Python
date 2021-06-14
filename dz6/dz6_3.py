# 3.Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = {'Wage': wage, 'Bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'ФИО: {self.name} {self.surname}'

    def get_total_income(self):
        return f'доход с учетом премии: {sum(self._income.values())}'


a = Position('Ivan', 'Surname', 'it', 10000, 2000)
print(vars(a))
print(a.get_full_name())
print(a.get_total_income())
