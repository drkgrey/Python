# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('введите число\n')
nn = n + n
nnn = nn + n
n_sum = int(n)+int(nn)+int(nnn)
print(n_sum)
