#############################
#Autor: Voitov Vladimir     # 
#Date: 28.11.21             #
#Task: HW_6_2  Tic Tac Toe  #
#############################

import time # import module time for module sleep
import random # import module random for randrange
'''
1 2 3
4 5 6
7 8 9
'''

board = [[3*i+j+1 for j in range(3)] for i in range(3)] # function for playground

def display(board): # function for display board
    print()
    print("+-------+-------+-------+")
    for i in range(3):
        time.sleep(0.1)
        print("|       "*3, '|', sep='')
        for j in range(3):
            time.sleep(0.1)
            print("|   "+str(board[i][j])+'   ', end='')
        print('|')
        print('|       '*3,'|', sep='')
        print('+-------'*3,'+', sep='')
    print()


def human_move(board): # function for user move
    print('Ur turn human!', '', sep = '\n', end = '\n') # ask for move
    move = input('Enter the number of the square: ') # where u want to move
    if move.isdigit() and 1<=int(move)<=9: # check for number and range
        step = int(move) - 1 
        g_line = step // 3
        v_line = step % 3
# Put choice number in the corresponding square if it is not occupied.
        if board[g_line][v_line] != 'X' and board[g_line][v_line] != 'O':
            board[g_line][v_line] = 'X'
            time.sleep(0.5)
            display(board)
        else:
            print('The human does not see it is busy!!!') # if square is busy
            human_move(board) # return to start
    else:
        print('U must use only numbers from 1 to 9!!') # if user out of range
        human_move(board)    # return to start

def comp_move(board): # function for computer move
    print('Time to win this!')
    move = random.randrange(1,9) # use random for finding a number in range
    step = int(move) - 1
    g_line = step // 3
    v_line = step % 3

    if board[g_line][v_line] != 'X' and board[g_line][v_line] != 'O':
        board[g_line][v_line] = 'O'
        display(board)
    else:
        comp_move(board)

'''Victory function.\
Searches for a match through a loop.'''

def victory(board):

    for i in range(3):
        # variants of winning combinations
        # if found return 'X' or 'O'
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            return 'X'
        elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            return 'O'
        elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            return 'X'
        elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            return 'O'
        elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            return 'X'
        elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            return 'O'
        elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 'X'
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 'O'

'''Game function.\
Using user and computer move function.\
Ask for playing.'''

def game(board): # function for playing
    answer = input('Let\'s play in TicTacToe? (y/n): ') # ask for answer y or n 
    if answer == 'y': # if 'y'
        print('Get ready!', 'Let\'s go!!!!', sep = '\n')
        count = 0 # end of moves counter
        while victory(board) != 'O' and victory(board) != 'X': # loop 4 play
            if count == 9: # if moves end
                print('Draw', 'U are lucky!', sep = '\n')
                break # end loop
            human_move(board) # users move
            victory(board) # search for a winner
            if victory(board) == 'X':
                break
            count += 1 # counter of a moves +1
            if count == 9: # if moves end
                print('Draw', 'U are lucky!', sep = '\n')
                break # end of loop
            print('Let\'s see...')
            time.sleep(0.2) # delayed operation 0.2 sec
            comp_move(board) # computer move
            victory(board) # search for a winner
            if victory(board) == 'X':
                break
            count += 1 # counter of a moves +1
    if victory(board) == 'X': # if user won
        print('Wretched man won!!!!', 'Madness!!!', sep = '\n')
    if victory(board) == 'O': # if computer won
        print('U loose!!', 'I won', 'Muhahaha!!!', sep = '\n')
        
    elif answer == 'n': # if answer about start was 'n'
        print('Weakling!') 
        exit() # exit from game
    else:
        print('What?', 'y or n.', sep = '\n')
        game(board) # return to start if input was not 'y' or 'n'

while True: # loop for play
    answer = input('Wonna play in TicTacToe? y/n: ')
    if answer == 'y': # if 'y' start play
        display(board) # show playground
        game(board) # start game
    elif answer == 'n': # if answer was 'n' exit
        print('bb')
        exit()
    else:
        break # if answer was abracadabra









        
