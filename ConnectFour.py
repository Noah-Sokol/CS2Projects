def printboard(board):
    print('1   2   3   4   5   6  ')
    for x in range(5):
        for i in range(6):
            print(board[i][4-x],end = " ")
        print('')

def get_user_turn(board):
    while True:
        try:
            column = int(input('which column would you like to chose'))-1
            for i in range(len(board[column])):
                if board[column][i] == ' o ':
                    return (str(column) + ','+ str(i))
            raise NameError
        except ValueError:print('value error')
        except IndexError:print('please input a number 1-6')
        except NameError:print('the column you chose was full')

def playerchoice():
    try: 
        r_or_b = input('input r to be red and b to be blue').lower()
        if r_or_b == 'r': return '🔵'
        elif r_or_b == 'b': return '🔴'
        else: raise NameError
    except NameError: print('please input either r or b')

def win_check(board,position):
    if verticle_win_check(board,position) == True or horizontal_win_check(board,position) == True:
        print('you win')

def horizontal_win_check(board,position):
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





def main():

    print('🔴🔵')
    board = [[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o ']]
    x = playerchoice()
    while True:
        printboard(board)
        position = get_user_turn(board)
        board[int(position[0])][int(position[2])] = ' x '
        if win_check(board,position) == True:
            print('win')
            break



main()

#get user's choice
#check for win
#computer's turn
#check for win
#loop until win
