# Задача №17. Общее обсуждение: дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
my_list_2 = []
for element in my_list:
    if element not in my_list_2:
        my_list_2.append(element)
print(len(my_list_2))



