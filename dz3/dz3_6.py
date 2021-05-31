# 6. Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    """Функция возвращает словот с заглавной буквы"""
    if text[0].isdigit():
        print('слово начинается с цифры')
    new_text = text.capitalize()
    return new_text


print(int_func(input('введите слово')))

