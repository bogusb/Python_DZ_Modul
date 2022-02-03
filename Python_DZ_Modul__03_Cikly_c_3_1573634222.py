# Основы программирования на Python
# Wydano 25.01.2022
# Wykonać do: 15.02.2022
# Temat Цикл for
# Wykładowca _____________________
# Lesson10
#
# Курс: «Введение в язык программирования Python
# Модуль 3. Циклы. Часть 3
#
# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.
#
# Задание 2
# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.
#
# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.
#
# Задание 4
# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.



# ------------------------------------------
# Задание 1
# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.
#
number = int(input("Enter the number :  "))
power_of = int(input(f"To which power to raise the number '{number}' ?  "))
number_to_power_of = number ** power_of
print(f"{number}  to the power of  {power_of}  equals :  {number_to_power_of}")


# # ------------------------------------------
# # Задание 2
# # Подсчитать количество целых чисел в диапазоне от
# # 100 до 999 у которых есть две одинаковые цифры.
# counter = 0
# num_start = 100
# num_end = 999
# for i in range(num_start, num_end + 1):
#     poz_10E2 = i // 100
#     poz_10E1 = (i % 100) // 10
#     poz_10E0 = i % 10
#     if poz_10E2 == poz_10E1 or poz_10E2 == poz_10E0 or poz_10E1 == poz_10E0:
#         counter = counter + 1
#         # print(counter, ':  ', poz_10E2, poz_10E1, poz_10E0)
# print(f'The number of integers in the range from {num_start} to {num_end}\nthat have two identical digits is :  {counter}')
#
#

# # ------------------------------------------
# # Задание 3
# # Подсчитать количество целых чисел в диапазоне от
# # 100 до 9999 у которых все цифры разные.
#
# counter = 0
# num_start = 100
# num_end = 9999
#
# for i in range(num_start, 999 + 1):
#     poz_10E2 = i // 100
#     poz_10E1 = (i % 100) // 10
#     poz_10E0 = i % 10
#     if poz_10E2 != poz_10E1 and poz_10E2 != poz_10E0 and poz_10E1 != poz_10E0:
#         counter = counter + 1
#         # print(counter, ':  ', poz_10E2, poz_10E1, poz_10E0)
#
# for i in range(1000, num_end + 1):
#     poz_10E3 = i // 1000
#     poz_10E2 = (i % 1000) // 100
#     poz_10E1 = (i % 100) // 10
#     poz_10E0 = i % 10
#     if poz_10E3 != poz_10E2 and poz_10E3 != poz_10E1 and poz_10E3 != poz_10E0 and poz_10E2 != poz_10E1 and poz_10E2 != poz_10E0 and poz_10E1 != poz_10E0:
#         counter = counter + 1
#         # print(counter, ':  ', poz_10E3,  poz_10E2, poz_10E1, poz_10E0)
#
# print(f'The number of integers in the range from {num_start} to {num_end}\nthat have all different digits is :  {counter}')
#

# # ------------------------------------------
# # Задание 4
# # Пользователь вводит любое целое число. Необхо-
# # димо из этого целого числа удалить все цифры 3 и 6 и
# # вывести обратно на экран.
# without_3and6 = ''
# enter_number = int(input("Enter the number :  "))
# for i in str(enter_number):
#     if i != '3' and i != '6':
#         without_3and6 = without_3and6 + i
# print(without_3and6)
