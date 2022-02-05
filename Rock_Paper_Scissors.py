# Основы программирования на Python
# Wydano 27.01.2022
# Wykonać do: 17.02.2022
# Temat Практическая работа. Камень Ножницы Бумага
# Wykładowca ______________
# Lesson11
#
# Курс: Python Junior
#
# ------------------------------------------
# Задание 1
# Доработайте игру, которую мы делали на уроке.
# - Добавьте возможность после окончания игры поиграть
# в игру заново. После окончания игры пользователю
# предлагается сыграть еще раз, если он этого хочет –
# игра начинается заново, иначе заканчивается.
# - Если пользователь вводит что-то неправильно – его
# просят ввести свой выбор еще раз, пока он не будет
# правильным.
#
# # Камень Ножницы Бумага
# # Rock Paper Scissors
# import random
#
# game = True
# global_player1_score = 0
# global_player2_score = 0
# game_type = 'pvp'  # pve or pvp
# while game:
#     # Variables
#     player1_choice = ''
#     player2_choice = ''
#     player1_score = 0
#     player2_score = 0
#     player1_name = str(input("Enter your name player 1 : "))
#     player2_name = 'Unknown'
#     if game_type == 'pvp':
#         player2_name = str(input("Enter your name player 2 : "))
#     elif game_type == 'pve':
#         player2_name = 'Bot'
#     rounds = 3
#
#     # Start of game
#     for i in range(1, rounds + 1):
#         player1_choice = ''
#         player2_choice = ''
#         # Enter data
#         while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's':
#             player1_choice = str(input(f"Enter your choice {player1_name}: [r],[p],[s] : "))
#         while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's':
#             if game_type == 'pvp':
#                 player2_choice = str(input(f"Enter your choice {player2_name}: [r],[p],[s] : "))
#             elif game_type == 'pve':
#                 player2_choice = random.choice('rps')  # Выбирает 1 символ l - lizard, k - Spock
#
#         # Compare data
#         if player1_choice == player2_choice:
#             print('Draw round')
#         elif player1_choice == 'r':
#             if player2_choice == 's':
#                 print(f'{player1_name} win the round!')
#                 player1_score = player1_score + 1
#             else:
#                 print(f'{player2_name} win the round!')
#                 player2_score = player2_score + 1
#         elif player1_choice == 'p':
#             if player2_choice == 'r':
#                 print(f'{player1_name} win the round!')
#                 player1_score = player1_score + 1
#             else:
#                 print(f'{player2_name} win the round!')
#                 player2_score = player2_score + 1
#         elif player1_choice == 's':
#             if player2_choice == 'p':
#                 print(f'{player1_name} win the round!')
#                 player1_score = player1_score + 1
#             else:
#                 print(f'{player2_name} win the round!')
#                 player2_score = player2_score + 1
#
#     # Compare score
#     if player1_score > player2_score:
#         print(f'{player1_name} win the game!')
#         global_player1_score = global_player1_score + 1
#     elif player2_score > player1_score:
#         print(f'{player2_name} win the game!')
#         global_player2_score = global_player2_score + 1
#     else:
#         print('Draw game!')
#     # Another game?
#     # game = bool(input("If you want continue press any key : "))
#     another_game = ''
#     while another_game != 'y' and another_game != 'n':
#         another_game = str(input(f"Another game?  [y] yes,  [n] no  ? "))
#     if another_game == 'n':
#         game = False
#

# ------------------------------------------
# Задание 2
# (Дополнительное, на высокую оценку)
# Есть другие варианты игры, которые содержат большее
# количество вариантов – «Камень, ножницы, бумага, ящерица,
# Спок». Переделайте игру по такому принципу.

# Ножницы Бумага Камень Ящерица Спок
# Scissors Paper Rock Lizard Spock
print('      »»»»»»  Scissors Paper Rock Lizard Spock  ««««««\n')
print('''      The rules:

   «Scissors cuts paper, 
   paper covers rock, 
   rock crushes lizard, 
   lizard poisons Spock, 
   Spock smashes scissors, 

   scissors decapitates lizard, 
   lizard eats paper, 
   paper disproves Spock, 
   Spock vaporizes rock, 
       and as it always has, 
   rock crushes scissors».
''')

import random

game = True
global_player1_score = 0
global_player2_score = 0
game_type = 'pvp'  # pve or pvp
while game:
    # Variables
    player1_choice = ''
    player2_choice = ''
    round_choice = ''
    player1_score = 0
    player2_score = 0
    player1_name = str(input("Enter your name player 1 : "))
    player2_name = 'Unknown'
    if game_type == 'pve':
        player2_name = 'Computer_Bot'
    elif game_type == 'pvp':
        player2_name = str(input("Enter your name player 2:  [Bot] = play with computer  : "))
        if player2_name == 'Bot' or player2_name == 'bot':
            game_type = 'pve'
            player2_name = 'Computer_Bot'
    rounds = 3

    # Start of game
    for i in range(1, rounds + 1):
        player1_choice = ''
        player2_choice = ''
        round_choice = ''
        # Enter data
        while player1_choice != 's' and player1_choice != 'p' and player1_choice != 'r' and player1_choice != 'l' and player1_choice != 'k':
            player1_choice = str(input(f"Enter your choice {player1_name}: [s] [p] [r] [l] [k] : "))
        while player2_choice != 's' and player2_choice != 'p' and player2_choice != 'r' and player2_choice != 'l' and player2_choice != 'k':
            if game_type == 'pvp':
                player2_choice = str(input(f"Enter your choice {player2_name}: [s] [p] [r] [l] [k] : "))
            elif game_type == 'pve':
                player2_choice = random.choice('sprlk')  # Выбирает 1 символ l - lizard, k - Spock
                print(f'{player2_name}  choice is  [{player2_choice}].')

        # Compare data
        round_choice = player1_choice + player2_choice
        if player1_choice == player2_choice:
            print('Draw round')
        elif round_choice == 'sp' or round_choice == 'pr' or round_choice == 'rl' or round_choice == 'lk' or round_choice == 'ks':
            print(f'{player1_name}  win the round!')
            player1_score = player1_score + 1
        elif round_choice == 'sl' or round_choice == 'lp' or round_choice == 'pk' or round_choice == 'kr' or round_choice == 'rs':
            print(f'{player1_name}  win the round!')
            player1_score = player1_score + 1
        else:
            print(f'{player2_name}  win the round!')
            player2_score = player2_score + 1

    # Compare score
    if player1_score > player2_score:
        print(f'{player1_name}  win the game!')
        global_player1_score = global_player1_score + 1
    elif player2_score > player1_score:
        print(f'{player2_name}  win the game!')
        global_player2_score = global_player2_score + 1
    else:
        print('Draw game!')
    print()
    # Another game?
    # game = bool(input("If you want continue press any key : "))
    another_game = ''
    while another_game != 'y' and another_game != 'n':
        another_game = str(input(f"Another game?  [y] yes  [n] no  ? "))
    print()
    if another_game == 'n':
        game = False
