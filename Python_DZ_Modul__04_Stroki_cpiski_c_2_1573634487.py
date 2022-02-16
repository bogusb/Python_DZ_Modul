# Основы программирования на Python
# Wydano 3.02.2022
# Wykonać do: 20.02.2022
# Temat Списки
# Wykładowca _______________
# Lesson15
#
# Курс: «Введение в язык программирования Python
# Модуль 4. Строки. Списки. Часть 2
#
# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
#
# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

# # ----------------------------------------
# # Задание 1:
# # Пользователь вводит с клавиатуры арифметическое
# # выражение. Например, 23+12.
# # Необходимо вывести на экран результат выражения.
# # В нашем примере это 35. Арифметическое выражение
# # может состоять только из трёх частей: число, операция,
# # число. Возможные операции: +, -,*,/
# #
# # Variables
# expression_entered = ''
# component = ''
# components = []
# result = 0
#
# # Enter data
# expression_entered = str(input("Enter an arithmetic expression (e.g. 23+12) :  "))
# # expression_entered = '12.45678 + 237'
# # expression_entered = '12/3'
# # expression_entered = ' - '
#
# # Order data
# for i in expression_entered:
#     if i.isnumeric() is True or i == '.':
#         component = component + i
#     elif i == '+' or i == '-' or i == '*' or i == '/':
#         components.append(component)  # 1st component
#         components.append(i)  # +-*/
#         component = ''
#
# components.append(component)  # 2nd component
#
# # Final result
# # print(components)
# if components[0] == '':
#     components[0] = '0'
# if components[2] == '':
#     components[2] = '0'
#
# expression_entered = components[0] + ' ' +  components[1] + ' ' +  components[2] + '  =  '
# components[0] = float(components[0])
# components[2] = float(components[2])
#
# if components[1] == '+':
#     result = (components[0] + components[2])
# elif components[1] == '-':
#     result = (components[0] - components[2])
# elif components[1] == '*':
#     result = (components[0] * components[2])
# elif components[1] == '/':
#     if components[2] != 0:
#         result = (components[0] / components[2])
#     else:
#         expression_entered = expression_entered + 'Divide by zero!  '
#
# if float(result) != int(float(result)):
#     result = float(result)
# else:
#     result = int(result)
#
# print(expression_entered, result)

# input()


# ----------------------------------------
# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

list_of_integers = [32, 57, 57, -80, -66, 58, -71, 38, 16, 17, -90, 59, 60, -31, -67, -86, 57, -44, -58, -34, 58, 64, 19, -9, -57, -31, 17, -87, -10, -55, 47, 98, -71, 78, -65, 73, 66, 14, -68, -43, -5, -22, 0, -44, 18, 21, 89, -77, -26, 15, -46, -35, 31, 67, -28, 70, 42, -5, 17, -69, -74, 92, 12, 83, -1, 77, 39, 67, 92, 37, -18, 49, 72, 0, -22, -85, 58, 92, -7, 9, 94, 32, -90, -9, -68, 96, 5, -89, 66, 59, 58, -30, 74, -16, -5, -35, 97, -48, -28, 66, -74, -82, 4]
# import random
#
# for i in range(300):
#     list_of_integers.append(random.randint(-99, 99))
#
print(list_of_integers)

minimum_element = list_of_integers[0]
maximum_element = list_of_integers[0]
counter_negative = 0
counter_positive = 0
counter_of_zeros = 0

for i in list_of_integers:
    if minimum_element > i:
        minimum_element = i
    if maximum_element < i:
        maximum_element = i
    if i < 0:
        counter_negative = counter_negative + 1
    if i > 0:
        counter_positive = counter_positive + 1
    if i == 0:
        counter_of_zeros = counter_of_zeros + 1


print(f'MIN: {minimum_element}')
print(f'MAX: {maximum_element}')
print(f'All elements: {len(list_of_integers)}')
print(f'Negative counter: {counter_negative}')
print(f'Positive counter: {counter_positive}')
print(f'Zeros counter: {counter_of_zeros}')

# input()