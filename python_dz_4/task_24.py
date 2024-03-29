# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

input: 4
output: 9

import random
bush = int(input("ввести количество кустов: "))
count = list(random.randint(0, 10) for i in range(bush))
result = []
i = 0
sum = 0

print(count)

while (i < bush):
    if (i == bush - 1):
        sum = count[i] + count[i - 1] + count[0]
    else:
        sum = count[i] + count[i - 1] + count[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"максимальное число ягод за одну итерацию {result[-1]}")