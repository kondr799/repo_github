# Задача № 9. По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while

print('Введите число N: ')

n = int(input())
fact = 1
if n < 0:
    print('Введите отрицательное число: ')
    print('Введите неотрицательное число: ')
    n = input()
else:
    while n > 1:
        fact = fact * n
        n = n - 1
print(f'Факторил заданного числа: {fact}') #Проверка на == 0 не обязательна, т.к. фаториал == 1.       