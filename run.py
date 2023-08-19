import random
import time

        print("""
Welcome To Battleship Captain!\n
We've spotted enemies Captain on the horizon... Go sink them!
""")


def get_playername():
    """
    Function to input the user name in the game
    """
    playername = input('Enter your name: \n')
    print('========================================================')
    return playername


def computer_board():
    """
    Function for the computer that places 5 ships randomly on the board
    """
    board = {
        '1A': ' ', '2A': ' ', '3A': ' ', '4A': ' ', '5A': ' ',
        '1B': ' ', '2B': ' ', '3B': ' ', '4B': ' ', '5B': ' ',
        '1C': ' ', '2C': ' ', '3C': ' ', '4C': ' ', '5C': ' ',
        '1D': ' ', '2D': ' ', '3D': ' ', '4D': ' ', '5D': ' ',
        '1E': ' ', '2E': ' ', '3E': ' ', '4E': ' ', '5E': ' ',
        }
    fleet_battle = random.sample(board.keys(), 5)
    for fleet in fleet_battle:
        board[fleet] = '@'
    return board


def player_board():
    """
    Function to create a board for the user where to place the ships
    """
    board = {
        '1A': ' ', '2A': ' ', '3A': ' ', '4A': ' ', '5A': ' ',
        '1B': ' ', '2B': ' ', '3B': ' ', '4B': ' ', '5B': ' ',
        '1C': ' ', '2C': ' ', '3C': ' ', '4C': ' ', '5C': ' ',
        '1D': ' ', '2D': ' ', '3D': ' ', '4D': ' ', '5D': ' ',
        '1E': ' ', '2E': ' ', '3E': ' ', '4E': ' ', '5E': ' ',
        }
    fleet_battle = []
    print('Where do you want to place your ships? You have 5 ships!\n')
    print('You must choose a number(1 to 5) and a letter(A to E). Example: 2D')
    while len(fleet_battle) < 5:
        fleet = input('\n')
        if fleet not in board.keys():
            print('Pay attention that\'s outside the battle zone')
        elif fleet in fleet_battle:
            print('This slot is already taken')
        else:
            fleet_battle.append(fleet)
    for fleet in fleet_battle:
        board[fleet] = '@'
    return board


def scoring_board():
    """
    Function to create a third board where the input of the user will display a hit or miss
    """
    board = {
        '1A': ' ', '2A': ' ', '3A': ' ', '4A': ' ', '5A': ' ',
        '1B': ' ', '2B': ' ', '3B': ' ', '4B': ' ', '5B': ' ',
        '1C': ' ', '2C': ' ', '3C': ' ', '4C': ' ', '5C': ' ',
        '1D': ' ', '2D': ' ', '3D': ' ', '4D': ' ', '5D': ' ',
        '1E': ' ', '2E': ' ', '3E': ' ', '4E': ' ', '5E': ' ',
        }
    return board


def display_board(board):
    """
    Function to display the ships on the board once the user
    has selected 5 slots for 5 ships.
    """
    print('---1---2---3---4---5---')
    print('A| ' + board['1A'] + ' | ' + board['2A'] + ' | \
' + board['3A'] + ' | ' + board['4A'] + ' | ' + board['5A'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('B| ' + board['1B'] + ' | ' + board['2B'] + ' | \
' + board['3B'] + ' | ' + board['4B'] + ' | ' + board['5B'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('C| ' + board['1C'] + ' | ' + board['2C'] + ' | \
' + board['3C'] + ' | ' + board['4C'] + ' | ' + board['5C'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('D| ' + board['1D'] + ' | ' + board['2D'] + ' | \
' + board['3D'] + ' | ' + board['4D'] + ' | ' + board['5D'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('E| ' + board['1E'] + ' | ' + board['2E'] + ' | \
' + board['3E'] + ' | ' + board['4E'] + ' | ' + board['5E'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    return board


def battleship_game():
    """
    Function to start the battle between the user and the computer
    inputting the slots chosen by the user to make a guess on where the
    computer's ships could be.
    """
    # Variables with computer's and player's boards
    name = get_playername()
    ai_board = computer_board()
    user_board = player_board()
    hit_board = scoring_board()
    # Variable to display the player's board
    time.sleep(0.5)
    display_board(user_board)
    print('====================================')
    turn = f'{name}'
    player_fleet = 5
    ai_fleet = 5

    user_choice = []
    ai_choice = []
    while player_fleet <= 5 or ai_fleet <= 5:
        for i in user_board:
            if turn == f'{name}':
                print('Your Turn')
                hit = input('\n')
                time.sleep(1)
                if hit not in ai_board.keys():
                    print('You fired outside the war-zone. Concentrate!\n')
                elif hit in user_choice:
                    print('You hit that slot already! Concentrate!\n')
                elif ai_board[hit] == '@':
                    ai_fleet -= 1
                    print('Great shot! Ship destroyed!\n')
                    hit_board[hit] = 'X'
                else:
                    print('You missed! \n')
                    hit_board[hit] = '0'
                user_choice.append(hit)
                time.sleep(1)
                display_board(hit_board)
                break
        time.sleep(1.5)
        for i in ai_board:
            if turn == 'Computer':
                print('Computer Turn')
                hit = random.sample(user_board.keys(), 1)
                print(hit[0])
                time.sleep(1)
                if hit in ai_choice:
                    print('Computer has hit that slot already!\n')
                elif user_board[hit[0]] == '@':
                    player_fleet -= 1
                    print('Computer has destoyed your ship!\n')
                else:
                    print('Computer has missed your ships!\n')
                ai_choice.append(hit)
                break
        if ai_fleet == 0:
            print('You Won The Battle\n')
            break
        if player_fleet == 0:
            print('You Lost The Battle\n')
            break
        if turn == f'{name}':
            turn = 'Computer'
        else:
            turn = f'{name}'
            time.sleep(0.7)
        print()
        print(f'{name} ships:{player_fleet}|Computer ships:{ai_fleet}\n')
        print('====================================')
    # Variable to start the game again or to end it once the battle between
    #  the user and the computer has ended.
    time.sleep(1)
    play_again = input('Do you want to play again? (y/n)\n')
    if play_again == 'y':
        print()
        battleship_game()
    else:
        print('Thanks for Playing!')


battleship_game()
