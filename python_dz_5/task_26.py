# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
a = int(input('Ввести число: '))
b = int(input('Ввести степень: '))
def calc_power(a, b):
    if b == 0:
        return 1
    return a * calc_power(a, b - 1)
print(calc_power(a, b))
