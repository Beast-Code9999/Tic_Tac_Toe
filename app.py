import random 

# welcome
print('Welcome to Tic Tac Toe!')

# print out a board

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board( board ):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

display_board( test_board )

# assign player marker 

def player_input():
    choice = ""
    while choice not in ['X', 'O', 'x', 'o']:
        choice = input("Please choose a sign (X or O): ").upper()
    player1 = choice
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

# place marker on board, aka a list

def place_marker( board, marker, position ):
    board[position] = marker

place_marker( test_board, "$", 1 )
display_board( test_board )

# check for win 

def win_check( board, mark ):
    return ((board[7] == board[8] == board[9] == mark) or # top horizontal
           (board[4] == board[5] == board[6] == mark) or # middle horizontal
           (board[1] == board[2] == board[3] == mark) or # bottom horizontal
           (board[9] == board[6] == board[3] == mark) or # right vertical
           (board[8] == board[5] == board[2] == mark) or # middle vertical
           (board[7] == board[4] == board[1] == mark) or # left vertical
           (board[7] == board[5] == board[3] == mark) or # backslash diagonal
           (board[1] == board[5] == board[9] == mark))   # forwardslash diagonal

# randomize which player goes first

def random_start():  
    flip = random.randint(0,1)   
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'


# check if the space on the board is empty

def check_empty_space( board, position ):
    return board[position] == ' '

# check if the board is full or not

def full_board_check( board ):
    for i in range(1,10):
        if check_empty_space( board, i):
            return False 
    return True



# player's choice of position

def player_choice( board ):

    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not check_empty_space( board, position ):
        
        position = int(input("Choose a position (1-9): "))
        
    return position
        
# ask player if they want to play again

def replay():
    
    choice = ''
    
    while choice not in ['yes', 'no']:
        
        choice = input("Do you wish to play again? (Yes or No): ").lower()
        
    return choice == 'yes'

play = replay()

print("Welcome to Tic Tac Toe")

while play: 
    # create an empty board to display later
    the_board = [' '] * 10
    # ask the user to choose a player sign and assign them respetively
    player1_marker, player2_marker = player_input()

    turn = random_start() # give a random start to either sign

    print( turn + ' will go first') 

    play_game = input("Are you ready to play? (y or n)") # to check if player is ready to plat
    # addign whether game_on is True or Not based on play_game
    if play_game in ['y', 'Y', 'Yes', 'YES']: 
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'player 1':
            # show board
            display_board(the_board)
            # choose a position
            position = player_choice( the_board )
            # place a marker
            place_marker( the_board, player1_marker, position )
            # check if player1 won or a tie
            if win_check( the_board, player1_marker ):
                display_board( the_board )
                print( "player 1 has won ")
                game_on = False
            else: 
                if full_board_check( the_board ):
                    display_board( the_board )
                    print("it is a tie")
                    game_on = False
                else: 
            # if no tie or win, then next player turn
                    turn = 'player 2'

        else:
            # show board
            display_board(the_board)
            # choose a position
            position = player_choice( the_board )
            # place a marker
            place_marker( the_board, player2_marker, position )
            # check if player1 won or a tie
            if win_check( the_board, player2_marker ):
                display_board( the_board )
                print( "player 2 has won ")
                game_on = False
            else: 
                if full_board_check( the_board ):
                    display_board( the_board )
                    print("it is a tie")
                    game_on = False
                else: 
            # if no tie or win, then next player turn
                    turn = 'player 1'
    if not play:
        break
