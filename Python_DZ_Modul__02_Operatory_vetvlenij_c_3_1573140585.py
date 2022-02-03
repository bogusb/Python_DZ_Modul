# Основы программирования на Python
# Wydano 18.01.2022
# Wykonać do: 1.02.2022
# Temat Условия. and, or, not
# Wykładowca _____________________
#

# Курс: «Введение в язык программирования Python
# Модуль 2. Операторы ветвлений Часть 3
# Lesson05

# ---------------------------------
# Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.
# Если пользователь ввел значение не в диапазоне от 1 до 100
# требуется вывести сообщение об ошибке.
#
# Задание 2
# Написать программу, которая по выбору пользователя возводит
# введенное им число в степень от нулевой до седьмой включительно.
#
# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит.
# Вывести стоимость на экран.
#
# Задание 4
# Зарплата менеджера составляет 200$ + процент от про-
# даж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.





# # ---------------------------------
# # Задание 1
# # Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
# # Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# # Если число кратно 5 нужно вывести слово Buzz.
# # Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# # Если число не кратно не 3 и 5 нужно вывести само число.
# # Если пользователь ввел значение не в диапазоне от 1 до 100
# # требуется вывести сообщение об ошибке.

# number = int(input("Enter a number in the range 1-100 : "))
# if 1 <= number and number <= 100:
#     if number % 3 != 0 and number % 5 != 0:
#         print(number)
#     elif number % 3 == 0 and number % 5 == 0:
#         print('Fizz Buzz')
#     elif number % 3 == 0:
#         print ("Fizz")
#     elif number % 5 == 0:
#         print ("Buzz")
# else:
#     print("The number is not in the range 1-100 !")








# # ---------------------------------
# # Задание 2
# # Написать программу, которая по выбору пользователя возводит
# # введенное им число в степень от нулевой до седьмой включительно.
# #
# number = float(input("Enter a number :  "))
# power_of = float(input(f"To which power (range 0-7)\nto raise the number '{number}' ? "))
# if 0 <= power_of and power_of <= 7:
#     print(f"{number}  ^  {power_of}  =  {number**power_of}")
# else:
#     print("The step of the power is not in the range of 0-7 !")








# # # ----------------------------------
# # Задание 3
# # Написать программу подсчета стоимости разговора
# # для разных мобильных операторов. Пользователь вводит
# # стоимость разговора и выбирает с какого на какой оператор он звонит.
# # Вывести стоимость на экран.

# tariff = 0
# tariff_name = ''
# tariff_multiplier = 0

# mobile_limit = 4
# mobile_1 = '1.Vodafone'
# mobile_2 = '2.KyivStar'
# mobile_3 = '3.Lifecell'
# mobile_4 = '4.BlaBlaBla'
# mobile_5 = mobile_6 = ''

# cost_input = float(input('Enter the COST of the call:  '))

# mobile_from = int(input(f'Enter number operator you are calling FROM:\n{mobile_1}  {mobile_2}  {mobile_3}  {mobile_4}  ?  '))
# if 1 <=  mobile_from <= mobile_limit:
#     if mobile_from == 1:
#         tariff_name = mobile_1
#     elif mobile_from == 2:
#         tariff_name = mobile_2
#     elif mobile_from == 3:
#         tariff_name = mobile_3
#     elif mobile_from == 4:
#         tariff_name = mobile_4

#     tariff = 10 * mobile_from + int(input(f'You call from  {tariff_name}  to which operator :\n{mobile_1}  {mobile_2}  {mobile_3}  {mobile_4}  ?  '))

#     if tariff % 10 == 1:
#         tariff_name = tariff_name + ' <--> ' + mobile_1
#     elif tariff % 10 == 2:
#         tariff_name = tariff_name + ' <--> ' + mobile_2
#     elif tariff % 10 == 3:
#         tariff_name = tariff_name + ' <--> ' + mobile_3
#     elif tariff % 10 == 4:
#         tariff_name = tariff_name + ' <--> ' + mobile_4
#     # print(f'Call tariff:  {tariff_name}\n')
#     print()

#     if tariff == 11 or tariff == 22 or tariff == 33 or tariff == 44 or tariff == 55 or tariff == 66:
#         print(f'You are calling within the same network. Call cost remains the same =  {cost_input}')
#     else:
#         if tariff == 12 or tariff == 21:
#             tariff_multiplier = 1.15
#         elif tariff == 13 or tariff == 31:
#             tariff_multiplier = 1.05
#         elif tariff == 14 or tariff == 41:
#             tariff_multiplier = 1.25
#         elif tariff == 23 or tariff == 32:
#             tariff_multiplier = 1.35
#         elif tariff == 24 or tariff == 42:
#             tariff_multiplier = 1.10
#         elif tariff == 34 or tariff == 43:
#             tariff_multiplier = 1.02
#         print(f'You call within DIFFERENT providers  {tariff_name}\nInitial call cost ({cost_input}) is multiplied (* {tariff_multiplier}) and is =  {tariff_multiplier * cost_input}')
# else:
#     print(f'The operator number you are calling from is NOT correct! It must be in range 1-{mobile_limit} !')







# ---------------------------------
# Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж,
# продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры уровень продаж для трех менеджеров.
# Определить их зарплату, определить лучшего менеджера,
# начислить ему премию 200$, вывести итоги на экран.

name_m1 = 'Robert'
name_m2 = 'Paul'
name_m3 = 'Henry'

sales_level_m1 = float(input(f"Manager {name_m1}'s sales level : "))
sales_level_m2 = float(input(f"Manager {name_m2}'s sales level : "))
sales_level_m3 = float(input(f"Manager {name_m3}'s sales level : "))

salary_m1 = salary_m2 = salary_m3 = 200
best_bonus = 200
bonus_m1 = bonus_m2 = bonus_m3 = 0
top_sales = 0
top_manager = ''

# top_sales is
if top_sales < sales_level_m1:
    top_sales = sales_level_m1
if top_sales < sales_level_m2:
    top_sales = sales_level_m2
if top_sales < sales_level_m3:
    top_sales = sales_level_m3

# top_manager is
if top_sales == sales_level_m1:
    top_manager = name_m1 + ', '
    bonus_m1 = best_bonus
if top_sales == sales_level_m2:
    top_manager = top_manager + name_m2 + ', '
    bonus_m2 = best_bonus
if top_sales == sales_level_m3:
    top_manager = top_manager + name_m3
    bonus_m3 = best_bonus

# salary 1. manager's
if sales_level_m1 < 500:
    salary_m1 = salary_m1 + bonus_m1 + sales_level_m1 * 0.03
elif 500 <= sales_level_m1 and sales_level_m1 <= 1000:
    salary_m1 = salary_m1 + bonus_m1 + sales_level_m1 * 0.05
elif 1000 < sales_level_m1:
    salary_m1 = salary_m1 + bonus_m1 + sales_level_m1 * 0.08

# salary 2. manager's
if sales_level_m2 < 500:
    salary_m2 = salary_m2 + bonus_m2 + sales_level_m2 * 0.03
elif 500 <= sales_level_m2 and sales_level_m2 <= 1000:
    salary_m2 = salary_m2 + bonus_m2 + sales_level_m2 * 0.05
elif 1000 < sales_level_m2:
    salary_m2 = salary_m2 + bonus_m2 + sales_level_m2 * 0.08

# salary 3. manager's
if sales_level_m3 < 500:
    salary_m3 = salary_m3 + bonus_m3 + sales_level_m3 * 0.03
elif 500 <= sales_level_m3 and sales_level_m3 <= 1000:
    salary_m3 = salary_m3 + bonus_m3 + sales_level_m3 * 0.05
elif 1000 < sales_level_m3:
    salary_m3 = salary_m3 + bonus_m3 + sales_level_m3 * 0.08

print()
print(f"Manager {name_m1}'s salary :  ${salary_m1}", bool(bonus_m1) * f"\n   (including bonus for best manager: ${bonus_m1})")
print(f"Manager {name_m2}'s salary :  ${salary_m2}", bool(bonus_m2) * f"\n   (including bonus for best manager: ${bonus_m2})")
print(f"Manager {name_m3}'s salary :  ${salary_m3}", bool(bonus_m3) * f"\n   (including bonus for best manager: ${bonus_m3})")
print(f'Top manager is : {top_manager}')
print(f'Top sales is: ${top_sales}')

# ---------------------------------
