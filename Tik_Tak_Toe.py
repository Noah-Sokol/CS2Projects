import random

def print_board(boardlist):
    for row in range(0,3):
        col = 0
        for col in range(0,3):
            print(boardlist[row][col], ('|'), end = " ")
        print("")

def inteligent_computer(boardlist, turn):
    if turn == 1:
        boardlist[2][2] = 'x'
    #going to work on more


def computer_random_picker(boardlist):
    while True:
        computer_randomr = random.randint(0,2)
        computer_randomc = random.randint(0,2)
        if boardlist[computer_randomc][computer_randomr]!= 'x' and boardlist[computer_randomc][computer_randomr] !='o':
            boardlist[computer_randomc][computer_randomr] = 'x'
            break
def get_user_choice(userchoice,boardlist):
    userchoicer = int(userchoice.split(',')[0])-1
    userchoicec = int(userchoice.split(",")[1])-1
    if (userchoice == '1,1' or userchoice == '1,2' or userchoice == '1,3' or userchoice == '2,1' or userchoice == '2,2' or userchoice == '2,3' or userchoice == '3,1' or userchoice == '3,2' or userchoice == '3,3') and boardlist[userchoicer][userchoicec] == '-':        boardlist[userchoicer][userchoicec] = 'o'
    else:
        print("please enter 1,1 to 3,3 or make sure the spot you chose isn't full already")
        return False

def end_game(boardlist):
    if win_check(boardlist) == 'computer win':
        print('computer wins')
        return True
    elif win_check(boardlist) == 'player win':
        print('player wins')
        return True
    elif win_check(boardlist) == 'tie':
        print('tie')
        return True


def win_check(boardlist):
    if boardlist[0][0] == 'x' and boardlist[0][1] == 'x' and boardlist[0][2] == 'x' or boardlist[1][0] == 'x' and boardlist[1][1] == 'x' and boardlist[1][2] == 'x' or boardlist[2][0] == 'x' and boardlist[2][1] == 'x' and boardlist[2][2] == 'x' or boardlist[0][0] == 'x' and boardlist[1][0] =='x' and boardlist[2][0]=='x' or boardlist[1][0]=='x' and boardlist[1][1]=='x' and boardlist[1][2]=='x' or boardlist[2][0]=='x' and boardlist[2][1]=='x' and boardlist[2][2]=='x' or boardlist[0][0]=='x' and boardlist[1][1]=='x' and boardlist[2][2]=='x':return 'computer win' 
    elif (boardlist[0][0] == 'o' and boardlist[0][1] == 'o' and boardlist[0][2] == 'o') or (boardlist[1][0] == 'o' and boardlist[1][1] == 'o' and boardlist[1][2] == 'o') or (boardlist[2][0] == 'o' and boardlist[2][1] == 'o' and boardlist[2][2] == 'o') or (boardlist[0][0] == 'o' and boardlist[1][0] =='o' and boardlist[2][0]=='o') or (boardlist[1][0]=='o' and boardlist[1][1]=='o' and boardlist[1][2]=='o') or (boardlist[2][0]=='o' and boardlist[2][1]=='o' and boardlist[2][2]=='o') or (boardlist[0][0]=='o' and boardlist[1][1]=='o' and boardlist[2][2]=='o'):return 'player win'
    while boardlist[0][0] != '-' and boardlist[0][1] != '-' and boardlist[0][2] != '-' and boardlist[1][0] != '-' and boardlist[1][1] != '-' and boardlist[1][2] != '-' and boardlist[2][0] != '-' and boardlist[2][1] != '-' and boardlist[2][2] != '-': return 'tie'

def main(): 
    run = True
    boardlist = [['-', '-', '-',],['-', '-', '-',],['-', '-', '-',]]
    while run == True:
        computer_random_picker(boardlist)
        print_board(boardlist)
        if end_game(boardlist) == True: break
        while True:
            userchoiceinput = input('what spot would you like to fill')
            userchoiceresult = get_user_choice(userchoiceinput,boardlist)
            if userchoiceresult != False: break
        print_board(boardlist)
        if end_game(boardlist) == True: break
        print ("\n\n")



main()
