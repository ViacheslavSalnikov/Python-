# print('Введите первое число: 1')
# a = int(input())

# b = int(input('Введите второе число: '))2

# print(a, '+', b, '=', a + b)

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = 5.8744534616
# b = 4.555556658
# print(round(a*b, 3))

# a = 1 > 4     false
# print(a)

# a = 1 < 4 and 5 > 2     true
# print(a)

# a = 1 == 2   false
# print(a)


# a = 1 != 2     true
# print(a)

# a = 'cwq'      true
# b = 'cwq'
# print(a == b)

# a = 1 < 3 < 3 < 10    false
# print(a)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Марина, мы тебя так ждали')
# elif username == 'Ксюша':
#     print('Ксюша, ТОП!!!!')
# else:
#     print('Привет, ', username)

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# a = 'qwerty'

# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for J in range(5):
#         line += "*"
#     print(line)

# print(len(text)) подсчет символов
# print('ещё' in text) true
# print(text.lower())  опускает в нижний регистр
# print(text.upper())   поднимает всё в верхний регистр
# print(text.replace('ещё' , 'ЕЩЁ')) меняет сочетание символов в нашей строке 1 аргумент какой есть, 2 аргумент на какой поменять

# n = int(input('Введите число: '))
# print(n * 5)

# n1 = 21
# n2 = 21
# n3 = 21
# print((n1 + 1) // 2 + (n2 + 1) // 2 + (n3 + 1) // 2)

# n = int(input('Введите число: '))
# if n > 5:
#     print('Число больше 5')
# elif n == 5:
#     print('Число равно 5')
# else:
#     print('Число меньше 5')

# m = 5
# n = 10
# if m == 5 and n == 10:
#     print('ok')

# m = 5
# n = 10
# if m == 5 or n == 11:
#     print('ok')

# year = int(input('Введите число: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# n = int(input('Введите число: '))

# res = 1
# while n > 0:
#     res *= n
#     n -= 1

# print(res)

# a = int(input('Введите число: '))   #Фибонначи
# n0 = 0
# n1 = 1
# n2 = None
# i = 1

# while n0 < a:
#     n2 = n0 + n1
#     n0 = n1
#     n1 = n2
#     i += 1
#     if n0 > a:
#         i = -1
# print(i)

# n = int(input('Введите число: '))
# max_day = 0
# temp_max = 0

# for i in range(n):
#     x = int(input('Введите число: '))
#     if x > 0:
#         temp_max += 1
#     else:
#         temp_max = 0
#     if temp_max > max_day:
#         max_day = temp_max

# print(max_day)


# n = int(input('Введите кол-во арбузов: '))
# x = int(input('Введите вес арбуза: '))
# min = x
# max = x
# for i in range(n - 1):
#     x = int(input('Введите вес арбуза: '))
#     if x > max:
#         max = x
#     if x < min:
#         min = x 
    
# print(min, max)

# list_1 = []
# list_1 = list()
# list_1 = [1, 8, 7, 9]
# print(list_1) # если поставить перед list знак *, то уберутся все скобки и запятые

# for i in list_1:
#     print(i)   # поочередно принимать определение из списка

# print(len(list_1))  # узнать размер нашего списка

# print(list_1[2]) # обращение к списку по элементно

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)   #функция append позволяет добавить какой-то элемент в конец нашего списка
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):     #c помощью цикла for мы добавляем к циклу какие-то значения
#     list_1.append(i)
#     print(list_1) 

# list_1 = [12, 7, -1, 12, 0]
# print(list_1.pop())   #функция pop - это функция удаления последнего элемента, но так же эта функция возвращает последний элемент , если создать переменную
# print(list_1)

# list_1 = [12, 7, -1, 12, 0]
# print(list_1.pop(1))   #удаление конкретного элемента из списка
# print(list_1)

# list_1 = [12, 7, -1, 12, 0]
# print(list_1.insert(2, 11)) #добавление элемента на нужную позицию (1ый аргумент - это позиция на который нужно втсавить элемент, 2ой аргумент - это значение)
# print(list_1)

# list_1 = [1, 2, 3, 5, 10, -14, -5, 8]
# print(list_1[0])
# print(list_1[1])
# print(list_1[-1])
# print(list_1[-5])
# print(list_1[: ])
# print(list_1[:2])
# print(list_1[len(list_1)-2:])
# print(list_1[0:len(list_1):6])  # c шагом 6
# print(list_1[::6])   # с шагом 6

#Кортежи
# t = ()
# print(type(t))

# t = (1)
# print(type(t))

# t = (1, 2, 1990)
# print(type(t))

# v = [21, 2, 1990]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a, b, c)

# t = (1, 2, 3, 4, 5)
# print(t[2])
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])
# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

#Cловари
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# del dictionary['left']
# for item in dictionary:
    # print(item) 
    # print('{}: {}'.format(item, dictionary[item])) #выводится значение по славарю и по ключу
# print(dictionary.items()) # При вводе dictionary.items каждый элемент будет являтся картежем

#Множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('black')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red') #проверяет есть ли это значение в нашем множестве
# colors.clear()  #очищает все множества из функции
# print(colors)  #выводится пустое множество set()

# Операция со множеством в Python
# a = {1, 2, 7, 5, 8, 10}
# b = {3, 8, 7, 9, 10, 12}
# c = a.copy()     # копирование(дублирование таких же значений, что и в а)
# u = a.union(b) # объединение
# i = a.intersection(b)   #пересечения
# d1 = a.difference(b)  #разность
# q = a.union(b).difference(a.intersection(b)) #сначала в скобках идет пересечение, потом по порядку (объединение и следом разностть)
# a = {1, 8, 5}
# b = frozenset(a)  #замороженное множество. Используем в тех случаях, когда мы точно уверены, что нельзя изменять изначальное множествро
 
# list1 = [1, 1, 2, -1, 5, 4, 8]
# print(set(list1))
# print(len(set(list1)))

# list1 = [1, 2, 3, 4, 5]
# k = 3
# k %= len(list1)
# res_list = list()
# for i in range(k):
#     res_list.append(list1[len(list1) - k + i])
# for i in range(len(list1) - k):
#     res_list.append(list1[i])
# print(res_list)

# list1 = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {"VIII":"S007"}

# res_set = set()
# for dict in list1:
#     for key in dict:
#         res_set.add(dict[key])
# print(res_set)

# list1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(list1)):
#     if list1[i - 1] < list1[i]:
#         count += 1

# print(count)

