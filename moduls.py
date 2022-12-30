#1 импортировать сам модуль
# import lesson_7
# print(lesson_7.get_time)

#2 импортировать отднльное из модуля
# from lesson_7 import get_time,hello
# print(get_time())
# print(hello())
##################################################
# #3 импортип=ровать все содержимое модуля сразу
# from lesson_7 import*
# print(get_time())
# print(hello())
# print(it())
##################################################
from lesson_7 import numbers, chet


def chet_nechet(num : list) -> list:
    for i in num:
        if i % 2 == 0:
            chet.append(i)
    return num 
print(chet_nechet(numbers))           