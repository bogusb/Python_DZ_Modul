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
list_3 = []
ad2_list = []

import random
for i in range(12):
    list_of_integers_1.append(random.randint(-30, 30))
for i in range(8):
    list_of_integers_2.append(random.randint(-20, 20))

# Original two lists
print('Original:')
print(f'List 1 ({len(list_of_integers_1)} elements): {list_of_integers_1}')
print(f'List 2 ({len(list_of_integers_2)} elements): {list_of_integers_2}')

# ad 1 - Сформировать третий список, содержащий элементы обоих списков;
list_3 = list_of_integers_1 + list_of_integers_2
print('   - List, containing elements from both lists:')
print(f'({len(list_3)} elements): {list_3}')
list_3.sort()
print(f'Sorted:\n({len(list_3)} elements): {list_3}')

# ad 2 - Сформировать третий список, содержащий элементы обоих списков без повторений;
print('   - List containing elements of both lists without repetitions:')

for i in range(1, len(list_3)+1):
    if list_3[i] != list_3[i-1]:
        ad2_list.append(list_3[i-1])

print(f'({len(ad2_list)} elements): {ad2_list}')


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

# input()
