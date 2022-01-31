# Курс: Введение в язык программирования Python
# Модуль 2. Операторы ветвлений Часть 1
# Lesson 03
# --------------------------------------
# Задание 1
# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

# print("Задание 1\n")
# number_1 = float(input("Enter number_1 : "))
# number_2 = float(input("Enter number_2 : "))
# number_3 = float(input("Enter number_3 : "))
#
# operation = str(input("\nEnter a mathematical operation   +  or  *  "))
# print()
#
# if operation == '+':
#     print(number_1, '+', number_2, '+', number_3, ' = ', number_1 + number_2 + number_3)
# elif operation == '*':
#     print(number_1, '*', number_2, '*', number_3, ' = ', number_1 * number_2 * number_3)
# else:
#     print("Incorrect operation. Only '+' or '*' allowed.")

# --------------------------------------
# Задание 2
# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх
# или средне арифметическое трёх чисел.
#
print("Задание 2\n")
number_1 = float(input("Enter number_1 : "))
number_2 = float(input("Enter number_2 : "))
number_3 = float(input("Enter number_3 : "))

number_temp = number_1
operation = str(input("\nEnter a mathematical operation\nx    max of\ni    min of\na    arithmetic mean of... ?  "))
print()
if operation == 'x':
    if number_2 > number_temp:
        number_temp = number_2
    if number_3 > number_temp:
        number_temp = number_3
    print('max(', number_1, ', ', number_2, ', ', number_3, ') = ', number_temp, sep='')
elif operation == 'i':
    if number_2 < number_temp:
        number_temp = number_2
    if number_3 < number_temp:
        number_temp = number_3
    print('min(', number_1, ', ', number_2, ', ', number_3, ') = ', number_temp, sep='')
elif operation == 'a':
    print('(', number_1, '+', number_2, '+', number_3, ') / 3   =  ', (number_1 + number_2 + number_3) / 3)
else:
    print("Incorrect operation. Only 'x' or 'i' or 'a'  allowed!")


# --------------------------------------
# Задание 3
# Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

# *** converter METERS => ***
# print("Задание 3\n")
#
# meters = float(input('Enter a count (e.g., 4.5) of meters: '))
# miles = meters / 1609.3123
# inches = meters / 0.0254
# yards = inches / 36 #yard=0.9144m
#
# operation = str(input("Enter a convert operation:\nm    ...to miles,\ni    ...to inches,\ny    ...to yards ?  "))
# print()
# if operation == 'm':
#     print(f'{meters}  meters (m) = (mi) miles:  {miles}')
# elif operation == 'i':
#     print(f'{meters}  meters (m) = (in) inches:  {inches}')
# elif operation == 'y':
#     print(f'{meters}  meters (m) = (yd) yards:  {yards}')
# else:
#     print("Incorrect operation. Only  'm'  or  'i'  or  'y'  allowed!")
