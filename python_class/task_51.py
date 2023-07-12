# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by (func, array):
#     result_list = []
#     for i in range(len(array)):
#         result_list.append(func(array[i]))
#     result_set=set(result_list) 
#     if len(result_set)>1:
#         return False
#     else:
#         return True

# def same_by(func, array):
#     for i in range(len(array)):
#         answer = func(array[i])
#         if answer != 0
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False


def char(x):
    return x % 2 == 0


values = [2, 4, 5]
print(same_by(char, values))