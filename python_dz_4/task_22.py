# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = (int(input('Ввести кол-во элементов первого множества: ')))
m = (int(input('Ввести кол-во элементов второго множества:')))
array1 = []
array2 = []
for i in range(n):
    array1.append(int(input('Ввести элемент первого массива: ')))
for j in range(m):
    array2.append(int(input('Ввести элемент второго массива: ')))
array3 = []
for i in array1:
    if i in array2 and i not in array3:
            array3.append(i)
array3.sort()
print(array3)        
