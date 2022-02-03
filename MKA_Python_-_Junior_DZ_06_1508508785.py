# Основы программирования на Python
# Wydano 20.01.2022
# Wykonać do: 11.02.2022
# Temat Циклы: while
# Wykładowca _____________________
# Lesson08
#
# Курс:
# Python Junior
#
# Задание 1
# Доработайте игру «Guess my number»,
# добавив следующие функции.
# - Улучшите игру так, чтобы после угадывания числа,
# выводился номер попытки, которую сделал пользователь
# для угадывания магического числа.
# - Улучшите игру так, чтобы после угадывания числа,
# выводилось количество потраченных попыток, которые сделал
# пользователь для угадывания магического числа.
#
# Задание 2
# (Дополнительное, на высокую оценку)
# Добавить возможность играть в игру заново.
# После того как пользователь угадает число, отображается
# сообщение: «Вы хотите сыграть заново? ([Да] или [Нет])».
# Если пользователь отвечает [Да], игра начинается заново,
# если отвечает [Нет] – игра заканчивается.
# »»»»»»»»»»»»»»»»»»»»»»»»» ««««««««««««««««««««««««««««««

# # # pet project
# import random
# initial_board = ' * '
# right_hand = '«««'
# left_hand = '»»»'
# game = True
# money = 0
# extra_life = 0
# lifes = 3
#
# print('|                »»»  Guess  my  number  «««                 |')
# print('| 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 |')
# while game:
#     # initial board
#     board_1 = board_2 = board_3 = board_4 = board_5 = initial_board
#     board_6 = board_7 = board_8 = board_9 = board_10 = initial_board
#     board_11 = board_12 = board_13 = board_14 = board_15 = initial_board
#     board_16 = board_17 = board_18 = board_19 = board_20 = initial_board
#     # show board
#     board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
#     print(board)
#
#     secret_number = random.randint(1,20)
#     guess_number = 0
#     attempt = 0
#
#     while secret_number != guess_number and lifes > 0:
#         guess_number = int(input("  Enter number : "))
#
#         # life decreases every 5 attempts
#         attempt = attempt + 1
#         if attempt % 3 == 0:
#             lifes = lifes - 1
#         print(f'  This is attempt  # {attempt}                            lives: {lifes}')
#
#         if secret_number < guess_number:
#             # board update
#             if guess_number == 2:
#                 board_2 = ' 2 '
#                 board_3 = board_4 = board_5 = right_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 3:
#                 board_3 = ' 3 '
#                 board_4 = board_5 = right_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 4:
#                 board_4 = ' 4 '
#                 board_5 = right_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 5:
#                 board_5 = ' 5 '
#                 board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 6:
#                 board_6 = ' 6 '
#                 board_7 = board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 7:
#                 board_7 = ' 7 '
#                 board_8 = board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 8:
#                 board_8 = ' 8 '
#                 board_9 = board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 9:
#                 board_9 = ' 9 '
#                 board_10 = right_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 10:
#                 board_10 = '10 '
#                 board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 11:
#                 board_11 = '11 '
#                 board_12 = board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 12:
#                 board_12 = '12 '
#                 board_13 = board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 13:
#                 board_13 = '13 '
#                 board_14 = board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 14:
#                 board_14 = '14 '
#                 board_15 = right_hand
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 15:
#                 board_15 = '15 '
#                 board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 16:
#                 board_16 = '16 '
#                 board_17 = board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 17:
#                 board_17 = '17 '
#                 board_18 = board_19 = board_20 = right_hand
#             elif guess_number == 18:
#                 board_18 = '18 '
#                 board_19 = board_20 = right_hand
#             elif guess_number == 19:
#                 board_19 = '19 '
#                 board_20 = right_hand
#             elif guess_number == 20:
#                 board_20 = '20 '
#             # Show board
#             board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
#             print(board)
#             print(f'  Secret number is less (<) than {guess_number}!')
#
#         elif secret_number > guess_number:
#             # board update
#             if guess_number == 1:
#                 board_1 = ' 1 '
#             elif guess_number == 2:
#                 board_1 = left_hand
#                 board_2 = ' 2 '
#             elif guess_number == 3:
#                 board_1 = board_2 = left_hand
#                 board_3 = ' 3 '
#             elif guess_number == 4:
#                 board_1 = board_2 = board_3 = left_hand
#                 board_4 = ' 4 '
#             elif guess_number == 5:
#                 board_1 = board_2 = board_3 = board_4 = left_hand
#                 board_5 = ' 5 '
#             elif guess_number == 6:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = ' 6 '
#             elif guess_number == 7:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = left_hand
#                 board_7 = ' 7 '
#             elif guess_number == 8:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = left_hand
#                 board_8 = ' 8 '
#             elif guess_number == 9:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = left_hand
#                 board_9 = ' 9 '
#             elif guess_number == 10:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = left_hand
#                 board_10 = ' 10'
#             elif guess_number == 11:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = ' 11'
#             elif guess_number == 12:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = left_hand
#                 board_12 = ' 12'
#             elif guess_number == 13:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = left_hand
#                 board_13 = ' 13'
#             elif guess_number == 14:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = left_hand
#                 board_14 = ' 14'
#             elif guess_number == 15:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = board_14 = left_hand
#                 board_15 = ' 15'
#             elif guess_number == 16:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
#                 board_16 = ' 16'
#             elif guess_number == 17:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
#                 board_16 = left_hand
#                 board_17 = ' 17'
#             elif guess_number == 18:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
#                 board_16 = board_17 = left_hand
#                 board_18 = ' 18'
#             elif guess_number == 19:
#                 board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
#                 board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
#                 board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
#                 board_16 = board_17 = board_18 = left_hand
#                 board_19 = ' 19'
#             # show board
#             board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
#             print(board)
#             print(f'  Secret number is greater (>) than {guess_number}!')
#
#     if lifes > 0:
#         print('  YOU WIN!!!')
#         money = money + 5
#         extra_life = (9 - attempt)//3
#         if extra_life > 0:
#             print(f'  You get {extra_life} extra lives.')
#         lifes = lifes + extra_life
#     else:
#         print('  YOU LOSE.')
#         lifes = 3
#     print(f'  You have {money} coins')
#     print()
#     print()
#

# ------------------------------------------------------

# Задание 2
# (Дополнительное, на высокую оценку)
# Добавить возможность играть в игру заново.
# После того как пользователь угадает число, отображается
# сообщение: «Вы хотите сыграть заново? ([Да] или [Нет])».
# Если пользователь отвечает [Да], игра начинается заново,
# если отвечает [Нет] – игра заканчивается.

import random
initial_board = ' * '
right_hand = '«««'
left_hand = '»»»'
game = True
money = 0
extra_life = 0
lifes = 3

while game:
    # initial board
    board_1 = board_2 = board_3 = board_4 = board_5 = initial_board
    board_6 = board_7 = board_8 = board_9 = board_10 = initial_board
    board_11 = board_12 = board_13 = board_14 = board_15 = initial_board
    board_16 = board_17 = board_18 = board_19 = board_20 = initial_board
    # show board
    print('|                »»»  Guess  my  number  «««                 |')
    print('| 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 |')
    board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
    print(board)

    secret_number = random.randint(1,20)
    guess_number = 0
    attempt = 0

    while secret_number != guess_number and lifes > 0:
        guess_number = int(input("  Enter number : "))

        # life decreases every 5 attempts
        attempt = attempt + 1
        if attempt % 3 == 0:
            lifes = lifes - 1
        print(f'  This is attempt  # {attempt}                            lives: {lifes}')

        if secret_number < guess_number:
            # board update
            if guess_number == 2:
                board_2 = ' 2 '
                board_3 = board_4 = board_5 = right_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 3:
                board_3 = ' 3 '
                board_4 = board_5 = right_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 4:
                board_4 = ' 4 '
                board_5 = right_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 5:
                board_5 = ' 5 '
                board_6 = board_7 = board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 6:
                board_6 = ' 6 '
                board_7 = board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 7:
                board_7 = ' 7 '
                board_8 = board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 8:
                board_8 = ' 8 '
                board_9 = board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 9:
                board_9 = ' 9 '
                board_10 = right_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 10:
                board_10 = '10 '
                board_11 = board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 11:
                board_11 = '11 '
                board_12 = board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 12:
                board_12 = '12 '
                board_13 = board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 13:
                board_13 = '13 '
                board_14 = board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 14:
                board_14 = '14 '
                board_15 = right_hand
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 15:
                board_15 = '15 '
                board_16 = board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 16:
                board_16 = '16 '
                board_17 = board_18 = board_19 = board_20 = right_hand
            elif guess_number == 17:
                board_17 = '17 '
                board_18 = board_19 = board_20 = right_hand
            elif guess_number == 18:
                board_18 = '18 '
                board_19 = board_20 = right_hand
            elif guess_number == 19:
                board_19 = '19 '
                board_20 = right_hand
            elif guess_number == 20:
                board_20 = '20 '
            # Show board
            board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
            print(board)
            print(f'  Secret number is less (<) than {guess_number}!')

        elif secret_number > guess_number:
            # board update
            if guess_number == 1:
                board_1 = ' 1 '
            elif guess_number == 2:
                board_1 = left_hand
                board_2 = ' 2 '
            elif guess_number == 3:
                board_1 = board_2 = left_hand
                board_3 = ' 3 '
            elif guess_number == 4:
                board_1 = board_2 = board_3 = left_hand
                board_4 = ' 4 '
            elif guess_number == 5:
                board_1 = board_2 = board_3 = board_4 = left_hand
                board_5 = ' 5 '
            elif guess_number == 6:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = ' 6 '
            elif guess_number == 7:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = left_hand
                board_7 = ' 7 '
            elif guess_number == 8:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = left_hand
                board_8 = ' 8 '
            elif guess_number == 9:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = left_hand
                board_9 = ' 9 '
            elif guess_number == 10:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = left_hand
                board_10 = ' 10'
            elif guess_number == 11:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = ' 11'
            elif guess_number == 12:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = left_hand
                board_12 = ' 12'
            elif guess_number == 13:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = left_hand
                board_13 = ' 13'
            elif guess_number == 14:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = left_hand
                board_14 = ' 14'
            elif guess_number == 15:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = board_14 = left_hand
                board_15 = ' 15'
            elif guess_number == 16:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
                board_16 = ' 16'
            elif guess_number == 17:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
                board_16 = left_hand
                board_17 = ' 17'
            elif guess_number == 18:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
                board_16 = board_17 = left_hand
                board_18 = ' 18'
            elif guess_number == 19:
                board_1 = board_2 = board_3 = board_4 = board_5 = left_hand
                board_6 = board_7 = board_8 = board_9 = board_10 = left_hand
                board_11 = board_12 = board_13 = board_14 = board_15 = left_hand
                board_16 = board_17 = board_18 = left_hand
                board_19 = ' 19'
            # show board
            board = f'|{board_1}{board_2}{board_3}{board_4}{board_5}{board_6}{board_7}{board_8}{board_9}{board_10}{board_11}{board_12}{board_13}{board_14}{board_15}{board_16}{board_17}{board_18}{board_19}{board_20}|'
            print(board)
            print(f'  Secret number is greater (>) than {guess_number}!')

    if lifes > 0:
        print('  YOU WIN!!!')
        money = money + 5
        extra_life = (9 - attempt)//3
        if extra_life > 0:
            print(f'  You get {extra_life} extra lives.')
        lifes = lifes + extra_life
    else:
        print('  YOU LOSE.')
        lifes = 3
    print(f'  You have {money} coins')
    print()

    # play again ?
    new_game = str(input("  Do you want to play again?\n  [Yes]  y       [No]  n   : "))
    if new_game == 'n':
        game = False
        print(f'  THE END !')
    print()
