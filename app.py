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

player1_marker, player2_marker = player_input()

print('Player 1: ', player1_marker)
print('Player 2: ', player2_marker)

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

win_status = win_check( test_board, player1_marker )
print(win_status)

# randomize which player goes first

def random_start():  
    flip = random.randint(0,1)   
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

print(random_start())

# check if the space on the board is empty

def check_empty_space( board, position ):
    return board[position] == ' '


#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break