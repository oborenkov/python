# Практическое задание 2. «Циклы(for, while)»

# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)




# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

# a, b = map(int, input(
#     'Введите сумму чисел и их произведение через пробел:').split())
# res = []
# for i in range(a + b):
#     if i == (a * i - b)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)


# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# a = int(input("Введите число: "))
# b = 1
# while b < a:
#     print(b, end=',')
#     b = b * 2

# (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print

# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,








