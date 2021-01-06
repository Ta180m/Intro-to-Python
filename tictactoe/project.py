'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
TIC-TAC-TOE PROJECT

Use the template below to write your tic-tac-toe project!

If you need help, feel free to ask your group leader.
'''


# The game board
# The board list contains 3 lists representing the rows of the board
# We can use board[0][0] to access the value in the top left corner
# Or board[2][2] to access the value in the bottom right corner
# ' ' represents an empty space
# 'X' represents player 1's X of course
# 'O' represents player 2's O
board = [[' ', ' ', ' '],
		 [' ', ' ', ' '],
		 [' ', ' ', ' ']]



def print_board():
	# Print the board


def check_draw():
	# check if there is a draw
	# return True if there is a draw
	# and False otherwise


def check_win():
	# check if there is a win
	# return 1 if player 1 won
	# return 2 if player 2 won
	# return 0 otherwise


def add_piece(row, column, player):
	# Add a new piece at the coordinates row, column
	# Add 'X' if it's player 1
	# And 'O' if it's player 2



player_turn = 1 # the player whose current turn it is


# Main game loop
while True: # loop forever
	if_draw = check_draw(board)
    if if_draw:
        # It's a draw!
		# Print something out!

        break


	if player_turn = 1:
		print("It's player 1's turn")
	else:
		print("It's player 2's turn")


	# ask for input
	row = input("Which row do you want to place your piece?")
    column = input("Which column do you want to place you piece?")
	

	if_win = check_win(board)
    if if_win != 0:
		# Someone won!
		# Print something out!

        break


	# Switch the player_turn
    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1

