# .1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов первого массива: "))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго массива: "))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)






# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

# n = int(input())
# a = list(map(int, input().split()))
# x = 0
# for i in range (n):
#     if (a[i]+a[i+1]+a[i-1] > x):
#         x = a[i]+a[i+1]+a[i-1]
# print(x)


## халтура !!!!!!!!!!!