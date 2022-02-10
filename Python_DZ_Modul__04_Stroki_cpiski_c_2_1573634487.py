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
# component = '0'
# components = []
# result = 0
#
# # Enter data
# expression_entered = str(input("Enter an arithmetic expression (e.g. 23+12) :  "))
# # expression_entered = '12.45678 + 237'
# # expression_entered = '12/3'
#
# # Order data
# for i in expression_entered:
#     if i.isnumeric() == True or i == '.':
#         component = component + i
#     elif i == '+' or i == '-' or i == '*' or i == '/':
#         if float(component) != int(float(component)):
#             components.append(float(component))
#         else:
#             components.append(int(float(component)))
#
#         components.append(i)
#         component = '0'
#
# if float(component) != int(float(component)):
#     components.append(float(component))
# else:
#     components.append(int(float(component)))
#
# # Final result
# print(components, end='    ')
# # print(f"{components[0]} {components[1]} {components[2]}  =  ", end='')
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
#         print("Error: Divide by zero!  ", end='')
#
# if float(result) != int(float(result)):
#     result = float(result)
# else:
#     result = int(result)
#
# print(result)
print(3 * 12.2)
input()

