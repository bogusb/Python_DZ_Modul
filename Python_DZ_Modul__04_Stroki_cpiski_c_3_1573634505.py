# Основы программирования на Python
# Wydano 3.02.2022
# Wykonać do: 20.02.2022
# Temat Списки
# Wykładowca ________________
# Lesson16
#
# Курс: «Введение в язык программирования Python
# Модуль 4. Строки. Списки. Часть 3
#
# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# - Сформировать третий список, содержащий элементы
# обоих списков;
# - Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# - Сформировать третий список, содержащий элементы
# общие для двух списков;
# - Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# - Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

# Variables
list_of_integers_1 = []
list_of_integers_2 = []
ad1_list = []
ad2_list = []
ad3_list = []
ad4_list = []
ad5_list = []

# Original two lists
import random
for i in range(12):
    list_of_integers_1.append(random.randint(-30, 30))
for i in range(8):
    list_of_integers_2.append(random.randint(-20, 20))

# ad 1 - Сформировать третий список, содержащий элементы
# обоих списков;
ad1_list = list_of_integers_1 + list_of_integers_2

# ad 2 - Сформировать третий список, содержащий элементы
# обоих списков без повторений;
ad2_list = ad1_list[:]
for i in ad1_list:
    if ad2_list.count(i) > 1:
        ad2_list.remove(i)

# ad 3 - Сформировать третий список, содержащий элементы
# общие для двух списков
ad3_list1 = list_of_integers_1[:]
# ad3_list1.sort()
ad3_list2 = list_of_integers_2[:]
# ad3_list2.sort()

# ad3_list1 = [-26, -20, -17, -9, -6, -6, 8, 8, 14, 20, 20, 25]
# ad3_list2 = [-15, -9, -7, -6, -6, -1, 8, -9, 15, 20, 20]

for i in ad3_list1:
    if ad3_list2.count(i) > 0:
        ad3_list2.remove(i)
        ad3_list.append(i)








# minimum_element = list_of_integers[0]
# maximum_element = list_of_integers[0]
# counter_negative = 0
# counter_positive = 0
# counter_of_zeros = 0


# for i in list_of_integers:
#     if minimum_element > i:
#         minimum_element = i
#     if maximum_element < i:
#         maximum_element = i
#     if i < 0:
#         counter_negative = counter_negative + 1
#     if i > 0:
#         counter_positive = counter_positive + 1
#     if i == 0:
#         counter_of_zeros = counter_of_zeros + 1
#
#
# print(f'MIN: {minimum_element}')
# print(f'MAX: {maximum_element}')
# print(f'All elements: {len(list_of_integers)}')
# print(f'Negative counter: {counter_negative}')
# print(f'Positive counter: {counter_positive}')
# print(f'Zeros counter: {counter_of_zeros}')

print('Original:')
print(f'List 1 ({len(list_of_integers_1)} elements): {list_of_integers_1}')
print(f'List 2 ({len(list_of_integers_2)} elements): {list_of_integers_2}')

print('\nad 1 - List, containing elements from both lists:')
print(f'({len(ad1_list)} elements): {ad1_list}')

print('\nad 2 - List containing elements of both lists without repetitions:')
print(f'({len(ad2_list)} elements): {ad2_list}')

print('\nad 3 - List that contains items common to the two lists:')
print(f'({len(ad3_list)} elements): {ad3_list}')


# input()


