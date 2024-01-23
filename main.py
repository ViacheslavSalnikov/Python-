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

list_1 = []
list_1 = list()
list_1 = [1, 8, 7, 9]
# print(list_1) # если поставить перед list знак *, то уберутся все скобки и запятые

# for i in list_1:
#     print(i)   # поочередно принимать определение из списка

# print(len(list_1))  # узнать размер нашего списка

# print(list_1[2]) # обращение к списку по элементно

