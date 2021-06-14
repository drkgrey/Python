# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
import random


class Car:
    speed = int()

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.color} {self.name} поехала и разогналась до скорости {self.speed}')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'максимальная скорость {self.color} {self.name} на данном участке - {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'водитель {self.color} {self.name}  нарушил правила - превышение скорости')


class SportCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'водитель {self.color} {self.name}  нарушил правила - превышение скорости')


class PoliceCar(Car):
    def __init__(self, name, color='штатная', is_police=True):
        super().__init__(color, name, is_police)


town_car_1 = TownCar('черная', 'Mazda')
town_car_2 = TownCar('белый', 'Ford')
work_car_1 = WorkCar('желтый', 'Man')
work_car_2 = WorkCar('желтый', 'Ford')
racing_car_1 = SportCar('красная', 'Ferrari')
police_car_1 = PoliceCar('Falcon-1')
cars = [town_car_1, town_car_2, work_car_2, work_car_1, racing_car_1, police_car_1]
for el in cars:
    print(vars(el))
    el.go(random.randint(0, 200))
    el.show_speed()
racing_car_1.turn('налево')
police_car_1.turn('направо')
for el in cars:
    el.stop()
