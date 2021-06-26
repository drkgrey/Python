# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:

    def __init__(self, ratio, ir):
        self.ratio = ratio
        self.ir = ir

    def __str__(self):
        if self.ir < 0:
            return f"{self.ratio} - {self.ir}i"
        return f"{self.ratio} + {self.ir}i"

    def __add__(self, other):
        return Complex(self.ratio + other.ratio, self.ir + other.ir)

    def __mul__(self, other):
        return Complex(self.ratio * other.ratio - self.ir * other.ir, self.ratio * other.ir + self.ir * other.ratio)


a = Complex(2, 1)
b = Complex(-1, 2)
print(a)
print(b)
print(a + b)
print(a * b)
