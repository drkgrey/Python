# 5.Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

my_f = open("dz5_5.txt", 'w')
count = 0
"""Запись чисел в файл"""
while count < 10:
    my_f.write(str(randint(0, 100)) + ' ')
    count += 1
my_f.close()
"""Считывание и подсчет"""
my_f = open("dz5_5.txt", 'r')
total = 0
for line in my_f:
    numbers = line.split()
    for n in numbers:
        total += int(n)
my_f.close()
print(f"Сумма чисел: {total}")
