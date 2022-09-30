# Gloabals
playing = True
#winner = None
turn = "X"  # X is default

# Board Setup
board = [
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#display_board()


# Turn Management
def turn_management(turn):
    print("Player " + turn + " turn")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        # Always check for valid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid number. Choose a position from 1-9: ")

        position = int(position) - 1  # Minus 1 because the board starts at 0

        if board[position] == "-":
            valid = True
        else:
            print("Pick another position")

    board[position] = turn
    display_board()


# Win Conditions
def game_over():
    win_condition()
    tie()


def win_condition():

    global winner

    # Check Row
    row_winner = row()
    # Check Column
    column_winner = column()
    # Check Diagonal
    diagonal_winner = diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def row():

    global playing

    # Check For Winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # When there is a winner, stop playing
    if row1 or row2 or row3:
        playing = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]


def column():

    global playing

    # Check For Winner
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    # When there is a winner, stop playing
    if column1 or column2 or column3:
        playing = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]


def diagonal():

    global playing

    # Check For Winner
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    # When there is a winner, stop playing
    if diagonal1 or diagonal2:
        playing = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]


def tie():
    if "-" not in board:
        global playing
        playing = False

def change_player():
    global turn

    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"


# Play Game
def play_game():

    display_board()

    while playing:
        turn_management(turn)
        game_over()
        change_player()

        if winner == "X" or winner == "O":
            print("Winner: " + winner)
        elif winner == None:
            print("Tie!")


play_game()
