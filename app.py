import random 

# welcome
print('Welcome to Tic Tac Toe!')

# print out a board

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board( board ):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

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

def space_check(board, position):
    
    return board[position] == ' '

# check if the board is full or not

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# player's choice of position

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
        
# ask player if they want to play again

def replay():
    
    choice = ''
    
    while choice not in ['yes', 'no']:
        
        choice = input("Do you wish to play again? (Yes or No): ").lower()
        
    return choice == 'yes'

play = replay()

print('Welcome to Tic Tac Toe!')

while play:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = random_start()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    print("player 2 turn")
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    print("player 1 turn")
                    turn = 'Player 1'

    if not replay():
        break