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
ad2_list = list_of_integers_1 + list_of_integers_2

for i in list_of_integers_1 + list_of_integers_2:
    if ad2_list.count(i) > 1:
        ad2_list.remove(i)

# ad 3 - Сформировать третий список, содержащий элементы
# общие для двух списков
ad3_list2 = list_of_integers_2[:]

for i in list_of_integers_1:
    if ad3_list2.count(i) >= 1:
        ad3_list2.remove(i)
        ad3_list.append(i)

# ad 4 - Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;

for i in list_of_integers_1:
    if list_of_integers_1.count(i) == 1:
        ad4_list.append(i)

for i in list_of_integers_2:
    if list_of_integers_2.count(i) == 1:
        ad4_list.append(i)

# ad 5 - Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из списков.

# # wariant z .sort()
# ad5_list1 = list_of_integers_1[:]
# ad5_list1.sort()
# ad5_list2 = list_of_integers_2[:]
# ad5_list2.sort()
#
# ad5_list.append(ad5_list1[0])
# ad5_list.append(ad5_list1[-1])
# ad5_list.append(ad5_list2[0])
# ad5_list.append(ad5_list2[-1])

# # wariant z 'for'
minimum_element = list_of_integers_1[0]
maximum_element = list_of_integers_1[0]

for i in list_of_integers_1:
    if minimum_element > i:
        minimum_element = i
    if maximum_element < i:
        maximum_element = i

ad5_list.append(minimum_element)
ad5_list.append(maximum_element)

minimum_element = list_of_integers_2[0]
maximum_element = list_of_integers_2[0]

for i in list_of_integers_2:
    if minimum_element > i:
        minimum_element = i
    if maximum_element < i:
        maximum_element = i

ad5_list.append(minimum_element)
ad5_list.append(maximum_element)


# Final result:
print('Initial lists:')
print(f'List 1 ({len(list_of_integers_1)} elements): {list_of_integers_1}')
print(f'List 2 ({len(list_of_integers_2)} elements): {list_of_integers_2}')

print('\nad 1 - List, containing elements from both lists:')
print(f'({len(ad1_list)} elements): {ad1_list}')

print('\nad 2 - List containing elements of both lists without repetitions:')
print(f'({len(ad2_list)} elements): {ad2_list}')

print('\nad 3 - List that contains items common to the two lists:')
print(f'({len(ad3_list)} elements): {ad3_list}')

print('\nad 4 - List containing only unique elements of each of the lists:')
print(f'({len(ad4_list)} elements): {ad4_list}')

print('\nad 5 - List containing only minimum and maximum values of each of the lists:')
print(f'({len(ad5_list)} elements): {ad5_list}')

# input()


