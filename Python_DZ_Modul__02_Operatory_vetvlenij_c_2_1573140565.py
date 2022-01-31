# Курс: Введение в язык программирования Python
# Модуль 2. Операторы ветвлений Часть 2
# Lesson 04
# --------------------------------------
#
# Задание 1
# Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели. Например, если 1,
# то на экране надпись понедельник, 2 — вторник и т.д.
#
# Задание 2
# Пользователь вводит с клавиатуры номер месяца (1-12).
# Необходимо вывести на экран название месяца. # Например, если 1,
# то на экране надпись январь, 2 — февраль и т.д.
#
# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»
#
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания

# --------------------------------------
# Задание 1
# Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели. Например, если 1,
# то на экране надпись понедельник, 2 — вторник и т.д.
#
# day_of_week = int(input('Enter the day number (1-7) : '))
# if day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')
# elif day_of_week == 3:
#     print('Wednesday')
# elif day_of_week == 4:
#     print('Thursday')
# elif day_of_week == 5:
#     print('Friday')
# elif day_of_week == 6:
#     print('Saturday')
# elif day_of_week == 7:
#     print('Sunday')
# else:
#     print('Incorrect entered the day number!')

# --------------------------------------
# Задание 2
# Пользователь вводит с клавиатуры номер месяца (1-12).
# Необходимо вывести на экран название месяца. # Например, если 1,
# то на экране надпись январь, 2 — февраль и т.д.
#
# month_number = int(input('Enter the month number (1-12) : '))
# if month_number == 1:
#     print('January')
# elif month_number == 2:
#     print('February')
# elif month_number == 3:
#     print('March')
# elif month_number == 4:
#     print('April')
# elif month_number == 5:
#     print('May')
# elif month_number == 6:
#     print('June')
# elif month_number == 7:
#     print('July')
# elif month_number == 8:
#     print('August')
# elif month_number == 9:
#     print('September')
# elif month_number == 10:
#     print('October')
# elif month_number == 11:
#     print('November')
# elif month_number == 12:
#     print('December')
# else:
#     print('Incorrect entered the month number!')


# --------------------------------------
# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

# number_pos_neg = float(input('Enter a number : '))
# if number_pos_neg > 0:
#     print('Number is positive')
# elif number_pos_neg < 0:
#     print('Number is negative')
# else:
#     print('Number is equal to zero')


# --------------------------------------
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания

number1 = int(input('Enter the first number : '))
number2 = int(input('Enter the second number : '))

if number1 != number2:
    if number1 < number2:
        print(number1, number2, sep=", ")
    else:
        print(number2, number1, sep=", ")
