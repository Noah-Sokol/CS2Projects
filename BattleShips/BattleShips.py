'''
Created on Sep 12, 2022
desc: battle ships game where the user can input how many guesses they want, how many ships they want,
plays sound when ship is sunk (not when misses because that is annoying) using four board(5x5 arrays) and changes two of those boards
last edited: 12/30/22
Bugs: None
@author: NoahSokol
'''
import random as rd
import winsound



def print_board(board):
    '''
        Prints the board 
    args: 
        board - list - board that is being printed
    '''
    print('   A B C D E')
    for row in range(0,5):
        print(row +1, end = "  ")
        for col in range(0,5):
            print(board[row][col], end = " ")
        print("")

def computer_turn(player_ships_board, computer_guesses_board, computer_shots, player_cumulative_ships):
    '''
        The computer's turn
    Args:
        player_ships_board - list - the board of the player's original ships
        computer_guesses_board - list - the board of the computer's guesses so far
        computer shots - list - the shots the computer has already made
        player_cumulative_ships - list - coordinates of all the players double dot ships

    Returns: 
        computer_guesses_board - the board of all of the computer's guesses updated for the main
    '''
    while True:
        try:
            random1 = rd.randint(0,4)
            random2 = rd.randint(0,4)
            if computer_guesses_board[random1][random2] != 'x': raise NameError
            break
        except NameError: continue
        except IndexError: continue
    computer_shots += [[random1, random2]]
    if player_ships_board[random1][random2] == 'c': computer_guesses_board[random1][random2] = 'h'
    elif player_ships_board[random1][random2] == 'o': computer_guesses_board[random1][random2] = 's'
    else: computer_guesses_board[random1][random2] = 'm'
    computer_guesses_board = check_sunk(computer_guesses_board,player_cumulative_ships,computer_shots)
    if computer_guesses_board[random1][random2] == 's': print('computer sunk your ship')

    return computer_guesses_board

def user_turn(computer_ships_board,player_guesses_board,computer_cumulative_ships, player_shots):
    '''
        The user's turn, also plays sound for hits
    Args:
        computer_ships_board - list - the original board of where all the computer ships are
        player_guesses_board - list - a board of all the player's guesses
        computer_cumulative_ships - list - the coordiantes of all of the cumputer's ships
        player_shots - list - a list of the the player's shots so far

    returns:
        player_guesses_board - a board of the player's guesses    
        player_shots - a list of all the player's shots so far
    '''
    player_guesses_board_copy = player_guesses_board[0].copy(), player_guesses_board[1].copy(), player_guesses_board[2].copy(), player_guesses_board[3].copy(), player_guesses_board[4].copy()
    while True:
        try:
            first_input = int(input('first: '))-1 
            player_guesses_board_copy[first_input]        #doesn't do anything just tests if its in the range and would raise an Index error if not
            second_input = ord((input('second: ').lower()))-97
            player_guesses_board_copy[first_input][second_input]
            if player_guesses_board_copy[first_input][second_input] != 'x': raise NameError
            break
        except IndexError:print('please enter 1-5 for first and a-e for second')
        except ValueError:print("please make sure first is an int")
        except NameError: print("please enter a spot that is not taken")
    player_shots += [[first_input, second_input]]

    if computer_ships_board[first_input][second_input] == 'c':  
        player_guesses_board[first_input][second_input] = 'h'
        winsound.PlaySound("mi_explosion_03_hpx.wav",winsound.SND_ALIAS)
        print('Hit')
    elif computer_ships_board[first_input][second_input] == 'o': 
        player_guesses_board[first_input][second_input] = 's'
        winsound.PlaySound("mi_explosion_03_hpx.wav",winsound.SND_ALIAS)
        print('Hit')
    else:
        player_guesses_board[first_input][second_input] = 'm'
        print('miss')
    player_guesses_board = check_sunk(player_guesses_board,computer_cumulative_ships,player_shots)
    if computer_ships_board[first_input][second_input] == 's': print("you sunk the computer's ship")

    return player_guesses_board, player_shots

def starting_board(computer_ships_board, x, y):
    '''
        Places the specified ships for a board by randomly selecting where to place the ships, Ran twice for the players starting board and the computer's starting board
    Args:
        computer_ships_board - list - the original list of the computers ships
        x - int - how many 2 dot long ships the user wants
        y - int - how many 1 dot ships the user wantes
    Returns:
        cumulative_ships - list - a list of the coordinates where the ships are
        computer_ships_board - list - the original computer's ships board
    '''
    cumulative_ships = []
    for i in range(x):
        while True:
            try:
                randomnumber1 = rd.randint(0,4)
                randomnumber2 = rd.randint(0,4)
                if randomnumber1 == 4 or randomnumber1 == 0: continue
                if randomnumber2 == 4 or randomnumber2 == 0: continue

                if computer_ships_board[randomnumber1][randomnumber2] == 'x':
                    if rd.randint(0,1) == 0:
                        if rd.randint(0,1) == 0:
                            if computer_ships_board[randomnumber1+1][randomnumber2] == 'x':
                                computer_ships_board[randomnumber1][randomnumber2] = 'c'
                                computer_ships_board[randomnumber1+1][randomnumber2] = 'c'
                                cumulative_ships += [[[randomnumber1,randomnumber2],[(randomnumber1+1),randomnumber2]]]
                                break
                        else: 
                            if computer_ships_board[randomnumber1-1][randomnumber2] == 'x':
                                computer_ships_board[randomnumber1][randomnumber2] = 'c'
                                computer_ships_board[randomnumber1-1][randomnumber2] = 'c'
                                cumulative_ships += [[[randomnumber1,randomnumber2],[(randomnumber1-1),randomnumber2]]]
                                break
                    else:
                        if rd.randint(0,1) == 0:
                            if computer_ships_board[randomnumber1][randomnumber2+1] == 'x':
                                computer_ships_board[randomnumber1][randomnumber2] = 'c'
                                computer_ships_board[randomnumber1][randomnumber2+1] = 'c'
                                cumulative_ships += [[[randomnumber1,randomnumber2],[(randomnumber1),randomnumber2+1]]]
                                break
                        else: 
                            if computer_ships_board[randomnumber1][randomnumber2-1] == 'x':
                                computer_ships_board[randomnumber1][randomnumber2] = 'c'
                                computer_ships_board[randomnumber1][randomnumber2-1] = 'c'
                                cumulative_ships += [[[randomnumber1,randomnumber2],[(randomnumber1),randomnumber2-1]]]
                                break
            except IndexError:  pass
    for i in range(0,y):
        while True:
            randomnumber1 = rd.randint(0,4)
            randomnumber2 = rd.randint(0,4)
            if computer_ships_board[randomnumber1][randomnumber2] == 'x':
                computer_ships_board[randomnumber1][randomnumber2] = 'o'
                break

    return cumulative_ships, computer_ships_board

def start_game(computer_ships_board, player_ships_board):
    '''
        function to start the game, user input how many guesses they want,
        how many ships of each varient they want and creates the starting board
    Args: 
        computer_ships_board/player_ships_board - list - both are the board where the original ships are
    Returns:
        player_cumulative_ships/computer_cumulative_ships - list - lists of the coordinates of the ships
        number_of_guesses - int - how many guesses the user wants aka how many time the user wants to iterate
    
    '''
    while True:
        try:
            number_of_guesses = int(input('how many guesses would you like to have (must be less than 25): '))
            if number_of_guesses >= 25: raise NameError 
            break
        except ValueError: print('please enter a number')
        except NameError: print('you must enter a number under 25')
    while True:
        try:
            x = int(input('how many 2 block wide ships would you like there to be (max 3): '))
            y = int(input('how many 1 block wide ships would you like there to be (max 4): '))
            if x > 3 or y > 4: raise NameError
            break

        except ValueError: print('please enter a number')
        except NameError: print ('there can only be 3 of the 2 block wide ships and 4 of the 1 block wide ships')
    computer_cumulative_ships, computer_ships_board = starting_board(computer_ships_board, x, y)
    player_cumulative_ships, player_ships_board = starting_board(player_ships_board, x, y)
    return player_cumulative_ships, computer_cumulative_ships, number_of_guesses


def check_sunk(player_guesses_board, cumulative_ships, shots):
    '''
        checks if any two dot length ships are sunk and if they are sunk, changes them to an s rather than an h on the board
    Args: 
        player_guesses_board - list - where all of the player's guesses are
        cumulative_ships - list - a list of the ship's coordinates
        shots - list - list of the shots taken so far
    Returns: player_guesses_board - updated board
    '''
    for ship in cumulative_ships:
        inship = False
        memory = ''
        for point in ship:
            if point not in shots:
                inship = False
                break
            else: 
                inship = True
                memory += str(point)
        if inship == True:
            for i in range(int(len(memory)/4)-1):
                player_guesses_board[int(str(memory).replace(' ','')[1])][int(str(memory).replace(' ','')[3])] = 's'
                memory = memory.replace(' ','')[5:]
    return player_guesses_board


def check_game_over(shipsboard, guessesboard):
    '''
        Sees if the ammount of ships sunk matches the ammount of ships, if so, returns true and ends the game
    Args:
        shipsboard - list - local variable for the original board with the loactions of the ships
        guessesboard - list - local variable for the original board with the location of the guesses
    Returns: 
        True - Bool -  if game is over
        False - Bool - if game is not over
    
    '''
    shipspaces = 0
    shipssunk = 0
    for i in shipsboard: 
        for j in i: 
            if j == 'o' or j == 'c': shipspaces +=1
    for x in guessesboard:
        for y in x:
            if j == 's': shipssunk+=1
    if shipspaces == shipssunk:return True
    else:return False









def main():
    endgame = False
    computer_ships_board = [['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x']]
    player_ships_board = [['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x']]
    player_guesses_board = [['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x']]
    computer_guesses_board = [['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x'],
            ['x','x','x','x','x']]
    player_shots = []
    computer_shots = []
    player_cumulative_ships, computer_cumulative_ships, number_of_guesses = start_game(computer_ships_board, player_ships_board)
    print('Your ships are located:')
    print_board(player_ships_board)
    while endgame == False:
        for i in range(number_of_guesses): 
            computer_guesses_board = computer_turn(player_ships_board, computer_guesses_board, computer_shots, player_cumulative_ships)
            print('the computer has guessed: ')
            print_board(computer_guesses_board)
            print('your guesses so far:')
            print_board(player_guesses_board)
            print('you have ', number_of_guesses-i, ' guesses left')
            player_guesses_board, player_shots = user_turn(computer_ships_board, player_guesses_board,computer_cumulative_ships, player_shots)
            if check_game_over(computer_guesses_board, player_ships_board) == True: endgame = 'player win'
            elif check_game_over(player_guesses_board, computer_guesses_board) == True: endgame = 'computer win'
        print('you have run out of moves')
        endgame = 'tie'
    if endgame == 'player win': print('You win!')
    elif endgame == 'computer win':
        print('the computer won \nyour oppenents board looked like: ')
        print_board(computer_ships_board)
    elif endgame == 'tie':
        print('the game ended in a tie\nyour oppenents board looked like: ')
        print_board(player_ships_board)






    
main()
