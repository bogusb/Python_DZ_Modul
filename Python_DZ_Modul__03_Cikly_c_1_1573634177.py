# Основы программирования на Python
# Wydano 20.01.2022
# Wykonać do: 31.01.2022
# Temat Циклы: while
# Wykładowca Буйлук Андрей
# Lesson07
#
# Курс: «Введение в язык программирования Python
# Модуль 3. Циклы. Часть 1
#
# Задание 1
# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.
#
# Задание 2
# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.
#
# Задание 3
# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.

# ------------------------------------------------------
# # Задание 1
# # Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# # Требуется проанализировать все числа в этом диапазоне по следующему правилу:
# # если число кратно 7, его надо выводить на экран.
#
# number_1 = -12 #int(input('Enter the start of the range : '))
# number_2 = 123 #int(input('Enter the end of the range : '))
#
# while number_1 <= number_2:
#     if number_1 % 7 == 0:
#         print(number_1, end=' ')
#     number_1 = number_1 + 1

# # ------------------------------------------------------
# # Задание 2
# # Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# # Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# # 1. Все числа диапазона;
# # 2. Все числа диапазона в убывающем порядке;
# # 3. Все числа, кратные 7;
# # 4. Количество чисел, кратных 5.
#
# number_1 = -9 #int(input('Enter the start of the range : '))
# number_2 = 23 #int(input('Enter the end of the range : '))
# origin_number_1 = number_1
# origin_number_2 = number_2
#
# # ad 1. Все числа диапазона;
# number_1 = origin_number_1
# number_2 = origin_number_2
# while number_1 <= number_2:
#     print(number_1, end=' ')
#     number_1 = number_1 + 1
# print()
#
# # ad 2. Все числа диапазона в убывающем порядке;
# number_1 = origin_number_1
# number_2 = origin_number_2
# while number_1 <= number_2:
#     print(number_2, end=' ')
#     number_2 = number_2 - 1
# print()
#
# # ad 3. Все числа, кратные 7;
# number_1 = origin_number_1
# number_2 = origin_number_2
# while number_1 <= number_2:
#     if number_1 % 7 == 0:
#         print(number_1, end=' ')
#     number_1 = number_1 + 1
# print(f"These are all multiples of the number 7 in the range ({origin_number_1} to {origin_number_2}).")
#
# # ad 4. Количество чисел, кратных 5.
# number_1 = origin_number_1
# number_2 = origin_number_2
# multiples_of_5 = 0
# while number_1 <= number_2:
#     if number_1 % 5 == 0:
#         multiples_of_5 = multiples_of_5 + 1
#         # print(number_1, end=' ')
#     number_1 = number_1 + 1
# print(f"There are '{multiples_of_5}' multiples of the number 5 in the range ({origin_number_1} to {origin_number_2}).")

# ------------------------------------------------------
# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне.
# Вывод на экран должен проходить по правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.

number_1 = -9 #int(input('Enter the start of the range : '))
number_2 = 23 #int(input('Enter the end of the range : '))

while number_1 <= number_2:
    if number_1 % 3 == 0 and number_1 % 5 != 0:
        print('(Fizz)', end=' ')
    elif number_1 % 3 != 0 and number_1 % 5 == 0:
        print('(Buzz)', end=' ')
    elif number_1 % 3 == 0 and number_1 % 5 == 0:
        print('(Fizz Buzz)', end=' ')
    elif number_1 % 3 != 0 and number_1 % 5 != 0:
        print(number_1, end=' ')
    number_1 = number_1 + 1
