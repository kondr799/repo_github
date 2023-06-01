# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = list = [2, 3, 5, 9, 3]
b = list = [2, 3, 4, 5, 6]
print(sum(list[1::2]))

# a = list(map(int, input(
#     'Введите числа строки через пробел: ').split()))

# sum = 0
# for i in range(1, len(a)):
#     if i % 2 != 0:
#         sum += a[i]

# print(f"{a} -> {sum}")

# Пример идеального решения
# Задача 10

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)

# Задача 12

# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
# Задача 14

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1