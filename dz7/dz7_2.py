# 2.Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def calc_consumption(self):
        print('расчет расхода ткани')


class Coat(Cloth):

    def __init__(self, v):
        self._consumption = v / 6.5 + 0.5

    @property
    def consumption(self):
        return self._consumption

    def calc_consumption(self):
        super().calc_consumption()
        print(f'{self.consumption:.2f}')


class Suit(Cloth):

    def __init__(self, h):
        self._consumption = h * 2 + 0.3

    @property
    def consumption(self):
        return self._consumption

    def calc_consumption(self):
        super().calc_consumption()
        print(f'{self.consumption:.2f}')


a = Suit(2)
b = Coat(45)
c = Suit(2.1)
d = Coat(38)
sm_list = [a, b, c, d]
for el in sm_list:
    el.calc_consumption()
print(f'{sum([x.consumption for x in sm_list]):.2f}')
