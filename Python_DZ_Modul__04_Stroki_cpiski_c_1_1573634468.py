# Основы программирования на Python
# Wydano 1.02.2022
# Wykonać do: 20.02.2022
# Temat Методы строк
# Wykładowca ___________________
# Lesson13

# Курс: «Введение в язык
# программирования Python
# Модуль 4. Строки. Списки.
# Часть 1

# ------------------------------------------

# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.
#
# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.
#
# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.

# ------------------------------------------
# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.
#

#Variables
text_entered = ''
text_reversed = ''
text_entered_lower = ''
text_entered_alnum = ''
text_reversed_alnum = ''

# Enter data
text_entered = str(input('Enter some text :  '))
# text_entered = 'А роза упала на лапу Азора'
# text_entered = 'А буду я у дуба'

# Compare data
text_entered_lower = text_entered.lower()
# print(text_entered_lower)
for i in text_entered_lower:
    if i.isalnum() == True:
        text_entered_alnum = text_entered_alnum + i
for i in text_entered_alnum:
    text_reversed_alnum = i + text_reversed_alnum

# Final result
# for i in text_entered:
#     text_reversed = i + text_reversed
print(f'>>> Text original:\n{text_entered}')
# print(text_reversed)
# print()
# print(text_entered_alnum)
print(f'>>> Alphanumeric characters only, in order from end to beginning:\n{text_reversed_alnum}')
if text_entered_alnum == text_reversed_alnum:
    print('>>> YES! The entered string is a palindrome.')
else:
    print('>>> NO! The string entered is not a palindrome.')