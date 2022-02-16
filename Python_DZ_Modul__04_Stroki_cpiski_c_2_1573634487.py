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

# ----------------------------------------
# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
#
# Variables
expression_entered = ''
component = ''
components = []
result = 0

# Enter data
expression_entered = str(input("Enter an arithmetic expression (e.g. 23+12) :  "))
# expression_entered = '12.45678 + 237'
# expression_entered = '12/3'
# expression_entered = ' - '

# Order data
for i in expression_entered:
    if i.isnumeric() is True or i == '.':
        component = component + i
    elif i == '+' or i == '-' or i == '*' or i == '/':
        components.append(component)  # 1st component
        components.append(i)  # +-*/
        component = ''

components.append(component)  # 2nd component

# Final result
# print(components)
if components[0] == '':
    components[0] = '0'
if components[2] == '':
    components[2] = '0'

expression_entered = components[0] + ' ' +  components[1] + ' ' +  components[2] + '  =  '
components[0] = float(components[0])
components[2] = float(components[2])

if components[1] == '+':
    result = (components[0] + components[2])
elif components[1] == '-':
    result = (components[0] - components[2])
elif components[1] == '*':
    result = (components[0] * components[2])
elif components[1] == '/':
    if components[2] != 0:
        result = (components[0] / components[2])
    else:
        expression_entered = expression_entered + 'Divide by zero!  '

if float(result) != int(float(result)):
    result = float(result)
else:
    result = int(result)

print(expression_entered, result)

# input()


# ----------------------------------------
