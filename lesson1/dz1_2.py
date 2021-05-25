# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

input_time = int(input('введите время в секундах\n'))
hours = input_time // 3600
minutes = (input_time % 3600) // 60
seconds = input_time % 60

print('время - {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
