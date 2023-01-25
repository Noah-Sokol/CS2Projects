class user_input():
    def __init__(self,var,board) -> None:
        self.var = var
        self.board = board
    def works(self) -> int:
        for i in range(len(self.board[self.var])):
            if self.board[self.var][i] == 'o': return i
        return False



    



    



def get_user_input():
    row = int(input('which row would you like to chose'))
    board = [['x','x','x','x','o'],['o','o','o','o','o']]
    x=user_input(row,board)
    collumn = x.works()
    print(board[row][collumn])


def main():
    get_user_input()


main()

#check for a win
#loop until win
