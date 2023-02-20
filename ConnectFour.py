'''
@author: NSokol25
Created on Sep 12, 2022
desc: Connect Four game using a 6x7 board using blue and red characters as the pieces
last edited: 12/30/22
Bugs: computer win check returns True when circles wraps around the board
'''

import random as rd
def printboard(board):
    print(' 1   2   3   4   5   6   7')
    for x in range(5):
        for i in range(7):
            print(board[i][4-x],end = " ")
        print('')

def get_user_turn(board):
    '''
    user's turn
Args:
    board - list - 6x7 array of board
Return: 
    position - str - column,row
    '''
    while True:
        try:
            column = int(input('which column would you like to chose'))-1
            for i in range(len(board[column])):
                if board[column][i] == ' o ':
                    return (str(column) + ','+ str(i))
            raise NameError                             #raise error if column is full
        except (IndexError,ValueError):print('please input a number 1-7')
        except NameError:print('the column you chose was full')

def computer_turn(board):
    '''
    gets the computer's random pick
Args: 
    board - list - 6x7 array of board
Return:
    position - str - column,row
    '''
    while True:
        try:
            column = rd.randint(0,6)
            for i in range(len(board[column])):
                if board[column][i] == ' o ':
                    return (str(column) + ','+ str(i))
            raise NameError                             #raise error if column is full
        except: continue

def playerchoice():
    '''
    asks user if they want to be red or blue
Returns:
    player - str - the color of the player
    computer - str - the color of the computer    
    '''
    print('🔴🔵')
    while True:
        try: 
            r_or_b = input('input r to be red and b to be blue').lower()
            if r_or_b == 'r': return '🔴 ','🔵 '
            elif r_or_b == 'b': return '🔵 ','🔴 '
            else: raise NameError
        except NameError: print('please input either r or b')

def win_check(board,position):
    '''
    checks for every type of win
Args:
    board - list - 6x7 array of board
    position - tuple - column,row used to get column and row
Returns: 
    True - bool - if there is a win
    Fasle - bool - if there is not a win
    '''
    return True if verticle_win_check(board,position) == True or horizontal_win_check(board,position) == True or diagnal_win_check(board,position) == True else False

def horizontal_win_check(board,position):
    '''
    Checks for a horizontal win
Args: 
    board - list - 6x7 array of board
    position - tuple - column,row used to get column and row
Returns: 
    True - if horizontal win is True
    False - if horizontal win is False
        '''
    horizontal = 1
    try:
        for i in range(1,4):
            if board[int(position[0])][int(position[2])] == board[int(position[0])+i][int(position[2])] != ' o ':
                horizontal+=1
            else:break
    except IndexError: pass
    for i in range(1,4):
        if board[int(position[0])][int(position[2])] == board[int(position[0])-i][int(position[2])] != ' o ':
            horizontal+=1
        else:break
    return True if horizontal >= 4 else False

def verticle_win_check(board,position):
    '''
    checks for a win vertically
Args:
    Board - list - 6x7 array of board
Returns:
    True - bool - if verticle win is True
    False - bool -  if verticle win is False
    '''
    verticle = 1
    try:
        for i in range(1,4):
            if board[int(position[0])][int(position[2])] == board[int(position[0])][int(position[2])+i] != ' o ':
                verticle+=1
            else:break
    except IndexError: pass
    for i in range(1,4):
        if int(position[2])<i:break 
        elif board[int(position[0])][int(position[2])] == board[int(position[0])][int(position[2])-i] != ' o ':
            verticle+=1
        else:break
    return True if verticle >= 4 else False

def diagnal_win_check(board,position):
    '''
    Checks for a diagnal win
Args:
    board - list - 6x7 array of board
    position - tuple - column,row used to get column and row
Returns: 
    True - Bool - when diagnal win is True
    False - Bool - when diagnal win is not True
    '''
    counted = 1
    try:
        for i in range(1,4):
            if board[int(position[0])][int(position[2])] == board[int(position[0])+i][int(position[2])-i] != ' o ':
                counted+=1
            else:break
    except IndexError: pass
    for i in range(1,4):
        if board[int(position[0])][int(position[2])] == board[int(position[0])-i][int(position[2])+i] != ' o ':
            counted+=1
        else:break
    if counted >= 4: return True
    counted = 1
    try:
        for i in range(1,4):
            if board[int(position[0])][int(position[2])] == board[int(position[0])+i][int(position[2])+i] != ' o ':
                counted+=1
            else:break
    except IndexError: pass
    for i in range(1,4):
        if board[int(position[0])][int(position[2])] == board[int(position[0])-i][int(position[2])-i] != ' o ':
            counted+=1
        else:break
    return True if counted >= 4 else False

def main():
    board = [[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o ']]
    player,computer = playerchoice()
    for turn in range (42):
        printboard(board)
        position = get_user_turn(board)
        board[int(position[0])][int(position[2])] = player
        if win_check(board,position) == True:
            printboard(board)
            print('You win')
            break
        computer_position = computer_turn(board)
        board[int(computer_position[0])][int(computer_position[2])] = computer
        if win_check(board,computer_position) == True:
            printboard(board)
            print('Computer wins')
            break



main()
