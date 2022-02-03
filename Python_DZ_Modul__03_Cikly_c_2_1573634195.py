# Основы программирования на Python
# Wydano 25.01.2022
# Wykonać do: 16.02.2022
# Temat Цикл for
# Wykładowca _____________________
# Lesson09
#
# Курс: «Введение в язык программирования Python
# Модуль 3. Циклы. Часть 2
#
# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы.
#
# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %
#
# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»
#
# Задание 4
# Пользователь вводит с клавиатуры числа. Програм-
# ма должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»


# --------------------------------------------------
# Задание 1
# Пользователь вводит с клавиатуры два числа.
# Нужно посчитать отдельно сумму четных, нечетных
# и чисел, кратных 9 в указанном диапазоне,
# а также среднеарифметическое каждой группы.
#
# суммa четных (sum of even), суммa нечетных (sum of odd)
# суммa чисел 9 кратных (sum of the numbers 9 multiples)
# среднеарифметическое каждой группы (arithmetic mean of each group)

# sum_all = sum_even = sum_odd = sum_multiple9 = 0
# count_all = count_even = count_odd = count_multiple9 = 0
#
# number1 = int(input('Enter the start of the range : '))
# number2 = int(input('Enter the end of the range : '))
#
# for i in range(number1, number2 + 1):
#     count_all = count_all + 1
#     sum_all = sum_all + i
#
#     if i % 2 == 0:
#         count_even = count_even + 1
#         sum_even = sum_even + i
#
#     if i % 2 != 0:
#         count_odd = count_odd + 1
#         sum_odd = sum_odd + i
#
#     if i % 9 == 0:
#         count_multiple9 = count_multiple9 + 1
#         sum_multiple9 = sum_multiple9 + i
#
# #    print(f'{number1} to {i}:  sum of all: {sum_all}  sum of even: {sum_even}  sum of odd: {sum_odd}  sum of multiples of 9: {sum_multiple9}')
#
# print(f'RANGE:        {number1} to {number2}')
# print(f'sum of  all:  {sum_all}               counter: {count_all}          Arithmetic mean: {sum_all / count_all}')
# print(f'sum of even:  {sum_even}               counter: {count_even}          Arithmetic mean: {sum_even / count_even}')
# print(f'sum of  odd:  {sum_odd}               counter: {count_odd}          Arithmetic mean: {sum_odd / count_odd}')
# print(f'sum of multiples of 9: {sum_multiple9}      counter:  {count_multiple9}          Arithmetic mean: {sum_multiple9 / count_multiple9}')


# --------------------------------------------------
# Задание 2
# Пользователь вводит с клавиатуры длину линии
# и символ для заполнения линии.
# Нужно отобразить на экране вертикальную линию
# из введенного символа, указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %
# line_length = int(input('Enter the line length : '))
# fill_symbol = str(input('Enter a symbol to fill the line : '))
#
# for i in range(line_length):
#     print(fill_symbol)


# --------------------------------------------------
# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

# ent_number = 0
# while ent_number != 7:
#     ent_number = float(input('Enter the number («7» to exit) : '))
#     if ent_number > 0:
#         print('Number is positive')
#     elif ent_number < 0:
#         print('Number is negative')
#     elif ent_number == 0:
#         print('Number is equal to zero')
# else:
#     print('Good bye!')




# --------------------------------------------------
# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна
# подсчитывать сумму, максимум и минимум, введенных чисел.
# Когда пользователь вводит число 7 программа прекращает
# свою работу и выводит на экран надпись «Good bye!»

# Pass: 1st
ent_number = float(input('Enter the number («7» to exit) : '))
sum_numbers = maximum_numbers = minimum_numbers = ent_number
print(f'    SUM of the entered numbers : {sum_numbers}     MAXimum: {maximum_numbers}      MINimum: {minimum_numbers}')

# Pass: 2nd and subsequent
while ent_number != 7:
    ent_number = float(input('Enter the number («7» to exit) : '))

    sum_numbers = sum_numbers + ent_number
    if ent_number > maximum_numbers:
        maximum_numbers = ent_number
    elif ent_number < minimum_numbers:
        minimum_numbers = ent_number

    print(f'    SUM of the entered numbers : {sum_numbers}     MAXimum: {maximum_numbers}      MINimum: {minimum_numbers}')

# «7» to exit
print('Good bye!')
