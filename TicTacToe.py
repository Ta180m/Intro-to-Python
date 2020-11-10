import random

def print_board(myarray):  # function to display the tic-tac-toe board
    print("       Collumn")
    print("        0 1 2")
    print("       ------- ")
    row_number = 0
    for rows in myarray:
        if row_number == 0:
            row = "    " + str(row_number) + " | "
        elif row_number == 1:
            row = "Row " + str(row_number) + " | "
        elif row_number == 2:
            row = "    " + str(row_number) + " | "

        for element in rows:
            if element == 0:
                row += "_"
            elif element == 1:
                row += "X"
            elif element == 2:
                row += "O"

            row += " "
        row = row + "|"
        print(row)

        row_number = row_number + 1
    print("       ------- ")


def player_input(board, row, collum, player):  # function to change a tile in the board
    if board[row][collum] == 0:
        board[row][collum] = player  # looks at a specific element in the board and changes the element to a plyer number
    else:
        print("That space is occupied!")

    return board  # returns the changed board


def check_draw(board):  # returns False if game is a tie, return true if there is still open space
    for row_number in range(3):
        for column_number in range(3):
            element = board[row_number][column_number]
            if element == 0:
                return False
    return True


def check_win(board):
    # check rows for win
    for row_number in range(3):
        row = board[row_number]
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # check vertical lines
    for collumn_number in range(3):
        if board[0][collumn_number] == board[1][collumn_number] == board[2][collumn_number] != 0:
            return board[0][collumn_number]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return -1


def AI_check(board):
    empty_spaces = []

    for row in range(3):
        for column in range(3):
            element = board[row][column]
            if element == 0:
                empty_spaces.append([row,column])

    return empty_spaces


def AI_move(board, player):
    empty_spaces = AI_check(board)
    number_of_empty_spaces = len(empty_spaces)
    rand = random.randint(0,number_of_empty_spaces-1)
    return empty_spaces[rand]


player_turn = 1
board = [[0,0,0],  # we are using an array of arrays to store what the board looks like
         [0,0,0],  # (and array that contains 3 arrays that contains 3 elements. This makes a 3x3 board)
         [0,0,0]]

print_board(board)  # we are calling the print_board to print what the board looks like

while True:  # this "while True" allows for code to repeat forever
    if_draw = check_draw(board)
    if if_draw:
        print("It's a draw!")
        break

    print("Player " + str(player_turn) + " turn!")

    if player_turn == 1:
        row = input("Which row do you want to place your piece?") # input is used to allow the user to enter data
        column = input("Which column do you want to place you piece?")
    if player_turn == 2:
        board_coordinate = AI_move(board,player_turn)
        row = board_coordinate[0]
        column = board_coordinate[1]


    board = player_input(board,int(row),int(column), int(player_turn))  # we have to change row, column, and player to an int
    print_board(board)

    if_win = check_win(board)
    if if_win != -1:
        print("Player " + str(if_win) + " has won.")
        break

    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1
