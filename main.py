# Checks a location on a 3x3 board for a line of 3 matching values.
def check_location(board, location_i, location_j):
    # Horizontal and vertical
    if (board[location_i][0] == board[location_i][1] and board[location_i][1] == board[location_i][2])\
            or (board[0][location_j] == board[1][location_j] and board[1][location_j] == board[2][location_j]):
        return True
    # Center diagonals
    if location_i == 1 and location_j == 1:
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) \
                or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return True
    # Corner diagonal
    else:
        if board[location_i][location_j] == board[1][1] and board[1][1] == board[2-location_i][2-location_j]:
            return True
    # No lines
    return False


def print_board(board):
    print("The board:")
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
    print()


def get_location(board):
    while True:
        # Get row
        r = 0
        try:
            r = int(input("Row: "))
            if r < 1 or r > 3:
                print("You must enter a number from 1 to 3.")
                continue
        except ValueError:
            print("You must enter a number from 1 to 3.")
            continue
        # Get column
        c = 0
        try:
            c = int(input("Column: "))
            if c < 1 or c > 3:
                print("You must enter a number from 1 to 3.")
                continue
        except ValueError:
            print("You must enter a number from 1 to 3.")
            continue
        # Check if location is available
        if board[r-1][c-1] == ' ':
            break
        else:
            print("That spot is taken.")
    # Return
    return r-1, c-1


wins_o = 0
wins_x = 0

print("Welcome to tic-tac-toe!")
while True:
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    turn = 'O'
    winner = None

    # Run game
    print("\nA game is starting.")
    for i in range(9):
        # Show board
        print("\nTurn " + str(i+1))
        print_board(game_board)
        print(f"It is {turn}'s turn.")

        # Get location and place symbol
        row, column = get_location(game_board)
        game_board[row][column] = turn

        # Check for winning move
        # The first 4 turns can't have a victory, so don't check during them
        if i > 3 and check_location(game_board, row, column):
            winner = turn
            break

        # Flip turn
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'

    # Declare end of game
    print("\nGame over!")
    print_board(game_board)
    if winner is None:
        print("The game ended in a stalemate.")
    else:
        print(winner + " won the game!")
        if winner == 'O':
            wins_o += 1
        else:
            wins_x += 1
    print(f"O has won {wins_o} times.")
    print(f"X has won {wins_x} times.")
    # Run again?
    replay = input("Would you like to play again (y/n)? ").strip().lower()
    while True:
        if replay == 'y' or replay == 'yes' or replay == 'n' or replay == 'no':
            break
        else:
            replay = input("(y/n) ")
    if replay == 'n' or replay == 'no':
        print("Goodbye!")
        break
