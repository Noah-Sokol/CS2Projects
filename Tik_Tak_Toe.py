import random


def print_board(boardlist):
    '''
    prints board

    Arg: 
        boardlist - board - list
    
        '''
    for row in range(0,3):
        col = 0
        for col in range(0,3):
            print(boardlist[row][col], ('|'), end = " ")
        print("")

def inteligent_computer_possible_win(boardlist):
    '''
    checks if either player or computer can win win for the ai

    Arg:
        boardlist - board - list(array)
    
    Returns:
        True if wither the computer or player could or will win

    '''
    for i in range(0,2):
        if i == 0: winner = 'computer win'
        else: winner = 'player win'
        for i in range(0,3):
            for y in range(0,3):
                if boardlist[i][y] == '-':
                    aiboard = [boardlist[0].copy(),boardlist[1].copy(),boardlist[2].copy()] #Done to combat bug where anything done to ai board would happen to original board
                    if winner == 'computer win': aiboard[i][y] = 'x'
                    else: aiboard[i][y] = 'o'
                    if win_check(aiboard) == winner:
                        if boardlist[i][y] == '-':
                            boardlist[i][y] = 'x'
                            return True
 
def inteligent_computer(boardlist, turn):
    '''
    Smart computer that makes an informed turn and if no good make make a random one

    Arg:
        Boardlist - board
        Turn - which turn it is used to make the right move
    
    Returns:
        Changes the board to do whats best
    
    '''
    if turn == 1:
        if boardlist[1][1] == '-': boardlist[1][1] = 'x'
        else: boardlist[0][0] = 'x'
        return 0         
    elif turn >= 2: 
        possible_win = inteligent_computer_possible_win(boardlist)
        if possible_win == True: return 0
    if turn == 2:
        if boardlist[0][0] == '-':
            boardlist[0][0] = 'x'
            return 0
        elif boardlist[2][2] == '-':
            boardlist[2][2] = 'x'
            return 0
    if turn > 2:
        if boardlist[0][0]!= 'x' and boardlist[0][0] !='o':
            boardlist[0][0] = 'x'
            return 0
        elif boardlist[2][2]!= 'x' and boardlist[2][2]!= 'o':
            boardlist[2][2] = 'x'
            return 0
        for i in range(0,3):
            if boardlist[i][2]!= 'x' and boardlist[i][2] !='o':
                boardlist[i][2] = 'x'
                return 0
        for i in range(0,3):
            if boardlist[i][0]!= 'x' and boardlist[i][0]!='x':
                boardlist[i][2] = 'x'
                return 0
    while True:
        computer_randomr = random.randint(0,2)
        computer_randomc = random.randint(0,2)
        if boardlist[computer_randomc][computer_randomr]!= 'x' and boardlist[computer_randomc][computer_randomr] !='o':
            boardlist[computer_randomc][computer_randomr] = 'x'
            break
    return 0

def get_user_choice(userchoice,boardlist):
    '''
    gets the user's choice and make sure it works

    Arg:
        userchoice - the user's input 

    Returns:
        changes the board if it works    
    '''
    userchoicer = int(userchoice.split(',')[0])-1
    userchoicec = int(userchoice.split(",")[1])-1
    if (userchoice == '1,1' or userchoice == '1,2' or userchoice == '1,3' or userchoice == '2,1' or userchoice == '2,2' or userchoice == '2,3' or userchoice == '3,1' or userchoice == '3,2' or userchoice == '3,3') and boardlist[userchoicer][userchoicec] == '-':        boardlist[userchoicer][userchoicec] = 'o'
    else:
        print("please enter 1,1 to 3,3 or make sure the spot you chose isn't full already")
        return False

def end_game(boardlist):
    '''
    sees if the game should end

    Arg:
        boardlist - the board
    
    Returns:
        True if the game should end    
    '''
    if win_check(boardlist) == 'computer win':
        print('computer wins')
        return 'computer win', True
    elif win_check(boardlist) == 'player win':
        print('player wins')
        return True
    elif win_check(boardlist) == 'tie':
        print('tie')
        return True

def win_possibilities(x, usedboard):
    '''
    the possible wins

    Arg:
        x - either X or O to see what to look for on the board
        usedboard - the board to check
    
    Return: 
        True if a win is possible    
    '''
    for i in range(0,3):
        if usedboard[i][0] == usedboard[i][1] == usedboard[i][2] == x or usedboard[0][i] == usedboard[1][i] == usedboard[2][i] == x or usedboard[0][0] == usedboard[1][1] == usedboard[2][2] == x or usedboard[0][2] == usedboard[1][1] == usedboard[2][0] == x:
            return True

def win_check(usedboard):
    '''
    runs the function win_possibilities to see if the game should be over and why

    Arg:
        usedboard - the board being checked
    
    Returns: 
        computer win (str) - if the computer won
        player win (str) - if the player won
        tie (str) - if it's a tie    
    '''
    if win_possibilities('x', usedboard) == True: return 'computer win'
    elif win_possibilities('o',usedboard) == True: return 'player win'
    while usedboard[0][0] != '-' and usedboard[0][1] != '-' and usedboard[0][2] != '-' and usedboard[1][0] != '-' and usedboard[1][1] != '-' and usedboard[1][2] != '-' and usedboard[2][0] != '-' and usedboard[2][1] != '-' and usedboard[2][2] != '-': return 'tie'

def player_turn(boardlist):
    '''
    does the player's turn

    Arg:
        boardlist - the board

    Returns - the altered board
    
    '''
    while True:
        try:
            userchoiceinput = input('what spot would you like to fill')
            get_user_choice(userchoiceinput,boardlist)
            break
        except ValueError: print('please enter in number , number form please')
        except IndexError: print('please make sure both rows and collomns are between 1-3')
    print_board(boardlist)


def main(): 
    turn = 0
    boardlist = [['-', '-', '-',],['-', '-', '-',],['-', '-', '-',]]
    if random.randint(0,1) == 1: player_goes_first = True
    else: player_goes_first = False
    for turn in range(1,10):
        if player_goes_first == False:
            inteligent_computer(boardlist, turn)
            print_board(boardlist)
            if end_game(boardlist) == True: break
            player_turn(boardlist)
            if end_game(boardlist) == True: break
            print ("\n\n")

        else:
            if end_game(boardlist) == True: break
            player_turn(boardlist)
            if end_game(boardlist) == True: break
            print ("\n\n")
            inteligent_computer(boardlist, turn)
            print_board(boardlist)


main()
