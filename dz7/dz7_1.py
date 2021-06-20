# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, list_of_lists):
        """создание матрицы с заполнением нулями по величине максимальной длины строки из исходных"""
        self.col = max([len(x) for x in list_of_lists])
        self.row = len(list_of_lists)
        for el in list_of_lists:
            while len(el) != self.col:
                el.append(0)
        self.numbers = list_of_lists

    def __str__(self):
        out = ''
        for i in self.numbers:
            out += ' '.join([str(x) for x in i]) + '\n'
        return out

    def __add__(self, other):
        res = []
        if (self.row == other.row) and (self.col == other.col):
            for i in range(len(self.numbers)):
                res.append([])
                for j in range(len(self.numbers[i])):
                    res[i].append(self.numbers[i][j] + other.numbers[i][j])
            return Matrix(res)
        else:
            return 'сложение не имеет смысла'


a = Matrix([[1, 2], [2, 3], [23, 10, 5]])
b = Matrix([[0, 0], [1, 1], [0, 1]])
c = Matrix([[1, 1, 1], [32, 8], [1]])
print(a)
print(b)
print(c)
print(a + b)
print(a + c)
print(b + c)
