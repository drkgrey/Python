# 2.Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
from string import punctuation
from re import sub


def my_print(di):
    """ Функция для красивого вывода"""
    for x in di:
        print("слов в строке ", x, " - ", di[x])


def clean_line_with_re(line):
    """ Функция для замены знаков препинания пробелами через регулярки"""
    #return sub('[' + punctuation + ']', ' ', line)
    return sub(r'\W|_', ' ', line)

def clean_line_with_replace(line):
    """ Функция для замены знаков препинания пробелами через replace"""
    return line.translate(str.maketrans(punctuation, " " * len(punctuation)))


with open("dz5_2.txt") as base_f:
    line_count = 0
    words_in_line_count = dict()
    for line in base_f:
        line_count += 1
        words_count = 0
        """ Реформат строки"""
        line = clean_line_with_re(line)
        # line = clean_line_with_replace(line)
        """ Подсчет слов"""
        for it in line.split():
            if it.isalnum():
                words_count += 1
        """ Составление словаря вида № строки - количество слов в строке"""
        words_in_line_count.update({line_count: words_count})
    print(f"общее количество строк: {line_count}\n")
    my_print(words_in_line_count)
