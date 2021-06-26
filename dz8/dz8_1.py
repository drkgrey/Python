# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class DateError(Exception):
    pass


class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def create(cls, date):
        day, month, year = [int(el) for el in date.split('-')]
        day, month, year = cls.validate(day, month, year)
        return cls(day, month, year)

    @staticmethod
    def validate(day, month, year):
        try:
            if (year > 2021 or month > 12 or month < 1 or day < 1) or (
                    day > 31 and month in [1, 3, 5, 7, 8, 10, 12] and year <= 2021) or (
                    day > 30 and month in [4, 6, 9, 11] and year <= 2021) or (
                    day > 29 and month == 2 and (year % 4 == 0 and year <= 2021) or (
                    day > 28 and month == 2 and (year % 4 != 0 and year <= 2021))):
                raise DateError()
        except DateError:
            print('в дате ошибка!')
            return 0, 0, 0
        return day, month, year

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'


if __name__ == '__main__':
    a = Data.create('29-02-1980')
    print(vars(a))
    b = Data.create('29-02-1701')
    print(vars(b))
    c = Data.create('31-01-1999')
    print(vars(c))
