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


# # ------------------------------------------
# # Задание 1
# # Пользователь вводит с клавиатуры строку. Проверьте
# # является ли введенная строка палиндромом. Палин-
# # дром — слово или текст, которое читается одинаково
# # слева направо и справа налево. Например, кок; А роза
# # упала на лапу Азора; доход; А буду я у дуба.
# #
#
# #Variables
# text_entered = ''
# text_reversed = ''
# text_entered_lower = ''
# text_entered_alnum = ''
# text_reversed_alnum = ''
#
# # Enter data
# # text_entered = str(input('Enter some text :  '))
# # text_entered = 'Madam in Eden, I’m Adam'
# text_entered = 'A Toyota! Race fast... safe car: a Toyota'
#
# # Compare data
# text_entered_lower = text_entered.lower()
# # print(text_entered_lower)
# for i in text_entered_lower:
#     if i.isalnum() == True:
#         text_entered_alnum = text_entered_alnum + i
# for i in text_entered_alnum:
#     text_reversed_alnum = i + text_reversed_alnum
#
# # Final result
# # for i in text_entered:
# #     text_reversed = i + text_reversed
# print(f'>>> original text:\n{text_entered}')
# # print(text_reversed)
# print(f'\n>>> alphanumeric characters only, in normal order:\n{text_entered_alnum}')
# print(f'{text_reversed_alnum}\n^^^ alphanumeric characters only, in order from end to beginning.\n')
# if text_entered_alnum == text_reversed_alnum:
#     print('>>> YES! The entered string is a palindrome.')
# else:
#     print('>>> NO! The string entered is not a palindrome.')


# ------------------------------------------
# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.
#

# Variables
text_entered = ''
text_changed = ''
# text_entered_upper = ''
list_reserved_words = []
reserved_word = ''
len_res = 0

# Enter data
# text_entered = str(input('Type some text :  '))
text_entered = "Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type."
list_reserved_words = ['DATA', 'LIST', 'TYP']
append_word = False # True / False

while append_word:
    append_word = str(input('Type reserved word,  blank [Enter] to exit :  '))
    if append_word != '':
        append_word = append_word.upper()
        list_reserved_words.append(append_word)

print(text_entered)
print(list_reserved_words)

# Compare data
text_changed = text_entered

for reserved_word in list_reserved_words:
    len_res = len(reserved_word)

    for i in range(len(text_changed) - len_res + 1):
        if text_changed[i:i + len_res].upper() == reserved_word:
            print(f'{i}: {text_changed[i:i + len_res].upper()}  ', end='')
            text_changed = text_changed[:i] + reserved_word + text_changed[i + len_res:]
    print()

# Final result
print(text_changed)

input()