# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

i = int(input('введите целое положительное число\n'))
max_i = 0
while i != 0:
    max_i = max(max_i, i % 10)
    i = i // 10
print(max_i)


