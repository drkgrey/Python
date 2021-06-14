# 1.Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import datetime
from itertools import cycle
from time import sleep
import colorama
from termcolor import colored


class TrafficLight:
    __color = ''
    _colors_rus = {'красный': 7, 'желтый': 2, 'зеленый': 11}
    _colors_eng = {'red': 7, 'yellow': 2, 'green': 11}

    # Конечный цикл с выходом на указанной секунде, вывод цветом. Отрисовка каждую секунду
    def running_cycle_online(self, end):
        colorama.init()
        start = 0
        for col in cycle(self._colors_eng.keys()):
            for i in range(self._colors_eng[col], 0, -1):
                self.__color = col
                start += 1
                print('\r', end='')
                print(colored(' \t ', 'grey', 'on_' + col, attrs=['bold', 'dark']), end='')
                if start >= end:
                    return
                sleep(1)

    # Конечный цикл с выходом на указанной секунде, вывод цветом. Отрисовка через интервал
    def running_cycle_online_v2(self, end):
        colorama.init()
        start = 0
        for col in cycle(self._colors_eng.keys()):
            print(colored(' \t ', 'grey', 'on_' + col, attrs=['bold', 'dark']))
            start += self._colors_eng[col]
            if start >= end:
                return
            sleep(self._colors_eng[col])

    # отсчет цифрами на фоне цвета
    def running_endless_color(self):
        colorama.init()
        for col in cycle(self._colors_eng.keys()):
            for i in range(self._colors_eng[col], 0, -1):
                self.__color = col
                print('\r', end='')
                print(colored(' {:2d}  '.format(i), 'grey', 'on_' + col, attrs=['bold', 'dark']), end='')
                sleep(1)

    # узнать какой цвет будет через заданное количество секунд c посекундным отчетом
    def running(self, end):
        from_start = 0
        for col in cycle(self._colors_rus.keys()):
            for i in range(self._colors_rus[col], 0, -1):
                self.__color = col
                from_start += 1
                if datetime.timedelta(seconds=from_start) == datetime.timedelta(seconds=end):
                    print(self.__color)
                    return

    # узнать какой цвет будет через заданное количество секунд с отсчетом промежутками
    def running_v2(self, end):
        from_start = 0
        for col in cycle(self._colors_rus.keys()):
            self.__color = col
            from_start += self._colors_rus[col]
            if datetime.timedelta(seconds=from_start) >= datetime.timedelta(seconds=end):
                print(self.__color)
                return


a = TrafficLight()
t = int(input('введите количество секунд чтобы узнать какой будет цвет светофора'))
a.running(t)
a.running_v2(t)
# a.running_cycle_online_v2(t)
# a.running_cycle_online(t)
# a.running_endless_color()
