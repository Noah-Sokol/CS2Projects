class user_input():
    def __init__(self,var,board) -> None:
        self.var = var
        self.board = board
    def drops_at(self) -> int:
        for i in range(len(self.board[self.var])):
            if self.board[self.var][i] == 'o': return i
        return False    


def printboard(board):
    print('1 2 3 4 5 6')
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
                    return int(column), int(i)
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






def main():

    print('🔴🔵')
    board = [[' x ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o '],[' x ',' o ',' o ',' o ',' o ',' o '],[' o ',' o ',' o ',' o ',' o ',' o ']]
    printboard(board)
    get_user_turn(board)



main()

#get user's choice
#check for win
#computer's turn
#check for win
#loop until win
