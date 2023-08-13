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
    for fleet in fleet_battle:
        board[fleet] = '@'
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
    print('Where do you want to place your fleet of ships ? You have 5 ships!\n')
    print('You must choose a number(1 to 5) and a letter(A to E)')
    while len(fleet_battle) < 5:
        fleet = input()
    if fleet not in board.keys():
            print('That\'s outside the battle zone')
    elif fleet in fleet_battle:
            print('This slot is already taken')
    else:             fleet_battle.append(fleet)
    for fleet in fleet_battle:
        board[fleet] = '@'
    return board

## function to display the board 

def display_board(board):

    print('---1---2---3---4---5---')
    print('A| ' + board['1A'] + ' | ' + board['2A'] + ' | ' + board['3A'] + ' | ' + board['4A'] + ' | ' + board['5A'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('B| ' + board['1B'] + ' | ' + board['2B'] + ' | ' + board['3B'] + ' | ' + board['4B'] + ' | ' + board['5B'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('C| ' + board['1C'] + ' | ' + board['2C'] + ' | ' + board['3C'] + ' | ' + board['4C'] + ' | ' + board['5C'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('D| ' + board['1D'] + ' | ' + board['2D'] + ' | ' + board['3D'] + ' | ' + board['4D'] + ' | ' + board['5D'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')
    print('E| ' + board['1E'] + ' | ' + board['2E'] + ' | ' + board['3E'] + ' | ' + board['4E'] + ' | ' + board['5E'] + ' |')
    print('-+-+-+-+-+-+-+-+-+-+-+')

    # function to play the game
def battleship_game():
    # computer's and player's boards
    ai_board = computer_board()
    user_board = player_board()
    
    # display player's board
    display_board(user_board)

    turn = 'Player'
    player_fleet = 5
    ai_fleet = 5 

    while player_fleet >= 5 or ai_fleet >= 5:
        for i in user_board:
            if turn == 'Player':
                print('Your Turn')
                hit = input()
                if hit not in user_board.keys():
                    print('You fired outside the war-zone. Try again!')
                elif computer_board()[hit] == '@':
                    ai_fleet -= 1
                    print('Great shot! Ship destroyed!')
                    print(f'Player ships: {player_fleet} | Computer ships: {ai_fleet}')
                else:
                    print('You missed! ')
                    break 
        for i in user_board:       
            if turn == 'Computer':
                print('Computer Turn')
                hit = random.sample(user_board.keys(), 1)
                print(hit[0])
                if user_board[hit[0]] == '@':
                    player_fleet -= 1
                    print('Computer destoyed your ship')
                else:
                    print('Computer missed your ships\n')
                    print(f'Player ships: {player_fleet} | Computer ships; {ai_fleet}')
                    break

        if turn == 'Player':
            turn = 'Computer'
        else:
            turn = 'Player' 





battleship_game()
