# print(5)
# print(5)
# print(5)

# print(5, 7)
# print(5)

# print(5, 8)
# print(5)

# a = 5
# b = 6.78
# c = 'hello'

# print("{} - {} - {}".format(a, b, c))
#print(f"{a} - {b} - {c}")
#print(a,' - ', b, ' - ', c)
#print(a, b, c)

#print('Введите первую строку')
#print('Введите первое число: ')
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

#v = 'string'

#c = 8.96
# c = 5
# print(c)
# print(type(c))
# #c = int(c)
# c = bool(c)
# print(c)
# print(type(c))

# a = 6.89554
# b = 5.23421

# print(round(a*b, 2))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 5
# print(a)
# a = 1 < 4 and 5 > 3
# print(a)
# a = 2 == 3
# print(a)
# a = 3 != 4
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 2 < 5 < 10
# print (a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша !')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина !')
# elif username == 'Роман':
#     print('Роман - точно !)')
# else:
#     print('Привет, ', username)       

# i =  0
# while i < 5:
#     #if i == 3:
#         #break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('Хватит !')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введённое число, делённое на 2
#         print(n)
#         flag = False
#         i += 1

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)    

text = 'Съешь ещё этих мягких французких булочек'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё','ЕЩЁ'))
