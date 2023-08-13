import random

# Board for computer

def computer_board():
    board = {
        '1A':' ', '2A':' ', '3A':' ', '4A':' ', '5A':' ',
        '1B':' ', '2B':' ', '3B':' ', '4B':' ', '5B':' ',
        '1C':' ', '2C':' ', '3C':' ', '4C':' ', '5C':' ',
        '1D':' ', '2D':' ', '3D':' ', '4D':' ', '5D':' ',
        '1E':' ', '2E':' ', '3E':' ', '4E':' ', '5E':' ',
        }
    fleet_battle = random.sample(board.keys(), 5)
    for battle in fleet_battle:
        board[battle] = '@'
    return board

#Board for player

def player_board():
    board = {
        '1A':' ', '2A':' ', '3A':' ', '4A':' ', '5A':' ',
        '1B':' ', '2B':' ', '3B':' ', '4B':' ', '5B':' ',
        '1C':' ', '2C':' ', '3C':' ', '4C':' ', '5C':' ',
        '1D':' ', '2D':' ', '3D':' ', '4D':' ', '5D':' ',
        '1E':' ', '2E':' ', '3E':' ', '4E':' ', '5E':' ',
        }

    fleet_battle = []
    print('Where do you want to place your fleet of ships? You have 5 ships!\n')
    print('You must choose a number(1 to 5) and a letter(A to E)')
    while len(fleet_battle) < 6:
        battle = input()
        if battle not in board.keys():
            print('That\'s outside the battle zone')
        if battle in fleet_battle:
            print('This slot is already taken')
        else: 
            fleet_battle.append(battle)
    for battle in fleet_battle:
        board[battle] = '@'
    return board

## function to display the board 
def display_board(board):

    print('---A---B---C---D---E---')
    print('1| ' + board['1A'] + ' | ' + board['2A'] + ' | ' + board['3A'] + ' | ' + board['4A'] + ' | ' + board['5A'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('2| ' + board['1B'] + ' | ' + board['2B'] + ' | ' + board['3B'] + ' | ' + board['4B'] + ' | ' + board['5B'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('3| ' + board['1C'] + ' | ' + board['2C'] + ' | ' + board['3C'] + ' | ' + board['4C'] + ' | ' + board['5C'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('4| ' + board['1D'] + ' | ' + board['2D'] + ' | ' + board['3D'] + ' | ' + board['4D'] + ' | ' + board['5D'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('5| ' + board['1E'] + ' | ' + board['2E'] + ' | ' + board['3E'] + ' | ' + board['4E'] + ' | ' + board['5E'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')


# function to play the game
def battleship_game():
    
    # computer's and player's boards
    ai_board = computer_board()
    user_board = player_board()

    # display player's board
    display_board(user_board)


battleship_game()