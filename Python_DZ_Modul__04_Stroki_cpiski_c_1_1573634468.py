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
text_alnum = ''
text_reversed = ''

# Enter data
text_entered = str(input('Enter some text :  '))
# text_entered = 'Kobyła ma mały bok'
# text_entered = 'А роза упала на лапу Азора'
# text_entered = 'Madam in Eden, I’m Adam'
# text_entered = 'A Toyota! Race fast... safe car: a Toyota'

# Compare data
for i in text_entered.lower():
    if i.isalnum() == True:
        text_alnum = text_alnum + i
for i in text_alnum:
    text_reversed = i + text_reversed

# Final result
print(f'>>> original text:\n{text_entered}')
print(f'\n>>> alphanumeric characters only, in normal order:\n{text_alnum}')
print(f'{text_reversed}\n^^^ alphanumeric characters only, in order from end to beginning.\n')

if text_alnum == text_reversed:
    print('>>> YES! The entered string is a palindrome.')
else:
    print('>>> NO! The string entered is not a palindrome.')

input()

# # ------------------------------------------
# # Задание 2
# # Пользователь вводит с клавиатуры некоторый текст,
# # после чего пользователь вводит список зарезервированных
# # слов. Необходимо найти в тексте все зарезервированные
# # слова и изменить их регистр на верхний. Вывести на
# # экран измененный текст.
# #
#
# # Variables
# text_entered = ''
# text_changed = ''
# list_reserved_words = []
# reserved_word = ''
# len_res = 0
#
# # Enter data
# # text_entered = str(input('Type some text :  '))
# text_entered = "Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. Oh! Yes? No."
# print(text_entered)
# # list_reserved_words = ['DATA', 'LIST', 'TYP']
# append_word = True  # True / False
#
# while append_word:
#     append_word = str(input('Type reserved word,  blank [Enter] to exit :  '))
#     if append_word != '':
#         append_word = append_word.upper()
#         list_reserved_words.append(append_word)
#
# print(list_reserved_words)
#
# # Finding and changing data
# text_changed = text_entered
# for reserved_word in list_reserved_words:
#     print(f"'{reserved_word}' in:  ", end='')
#     len_res = len(reserved_word)
#
#     for i in range(len(text_changed) - len_res + 1):
#         if text_changed[i:i + len_res].upper() == reserved_word:
#             print(i, end='  ')
#             text_changed = text_changed[:i] + reserved_word + text_changed[i + len_res:]
#     print()
#
# # Final result
# print(text_changed)
#
# input()


# # ------------------------------------------
# # Задание 3
# # Есть некоторый текст. Посчитайте в этом тексте ко-
# # личество предложений и выведите на экран полученный
# # результат.
#
# # Variables
# initial_text = ''
# sentence = ''
# start_sentence = 0
# sentences = []
# endings = ['. ', '! ', '? ']
#
# # Enter data
# # initial_text = str(input('Type some text :  '))
# initial_text = "Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. Oh! Yes? No."
# # initial_text = "Python. Known!?"
# initial_text = initial_text + ' '
# print(initial_text)
# print()
#
# # Finding and cutting data
# for i in range(len(initial_text) - 2 + 1):  # 2 is len of sentence_ending
#     if initial_text[i:i + 2] == endings[2] or initial_text[i:i + 2] == endings[1] or initial_text[i:i + 2] == endings[0]:
#         sentence = initial_text[start_sentence: i + 2]
#         print(f"{start_sentence} - {i + 1} :  {sentence}")
#         sentences.append(sentence)
#         start_sentence = i + 2
#
# # Final result
# print(sentences)
# print(f"\nThe text includes sentences : {len(sentences)}.")
#
# input()

# -------------------------------------------------