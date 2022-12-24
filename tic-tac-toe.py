"""
Project:  Tic Tac Toe
Author: Giuseppe Brandi
Time: 4 January 2023
Purpose: Write a program that will simulate a Tic-Tac-Toe game in which two
players seek in alternate turns to complete a row, a column, or a diagonal with
either three x's or three o's drawn in the spaces of a grid of nine squares.

Requirements:
The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.
"""

#########################
# FUNCTIONAL REQUIREMENTS
#########################
# FR1. Print instructions
# FR2. Display the game board
# FR3. Ask player to enter the position of the marker on the board
# FR4. Validate the marker position
# FR5. Place the marker on the board
# FR6. Check if there is a winner
# FR7. Check if there is a tie
# FR8. Switch player
# FR9. Print a message if there is a winner or a tie


##############################
# DESIGN STEPS
##############################
# DS1. print_instructions()
# DS2. display_board()
# DS3. input()
# DS4. validate_marker_position()
# DS5. handle_player_turn()
# DS6. check_for_winner()
# DS7. check_if_tie()
# DS8. flip_player()
# DS9. print()


# Game board
BOARD = list(map(str, range(1, 10)))

# Set game_still_going to True
game_still_going = True

# Set winner to None
winner = None

# Current player
current_player = "X"


def main():
    # DS1. Call print_welcome_message to provide a description of the game
    print_instructions()
    # DS2. Call display_board to display the game board
    display_board()

    while game_still_going:

        # DS3. Ask player to enter the position of the marker on the board
        # as a number between 1 and 9
        position = input(f"\n{current_player}'s "
                         f"turn to choose a square (1-9): ")

        # DS4. Call validate_marker_position to check that the entered number
        # is between 1 and 9 and the position is not already taken
        validate_marker_position(position)

        # DS5. Call the handle_player_turn to place the marker on the board
        handle_player_turn(current_player, int(position))

        # Call the display_board to display the game board
        display_board()

        # DS6. Check for a winner
        check_for_winner()
        # DS7. Check is there is a tie
        check_if_tie()
        # DS8. Call flip_player to change player
        flip_player()

    # The game is over.
    outcome = f"{winner} won." if winner in ("X", "O") else "Tie."
    # Print the winner
    print(outcome)


def print_instructions():
    """
    This function prints a welcome message to the user.
    """
    print(
        "\nWelcome to the Tic Tac Toe Game.",
        "The objective of Tic Tac Toe is to get three in a row.",
        "You will play on a three by three game board.",
        "The first player is known as X and the second is O.",
        "Players alternate placing Xs and Os on the game board until either",
        "opponent has three in a row or all nine squares are filled.",
        "X always goes first, and if no one has three in a row, the stalemate "
        "is called a tie.",
        sep="\n"
    )


def display_board():
    """
    It prints the board
    """
    BOARD_SEPARATOR = "--+---+--"
    print(f"\n{BOARD[0]} | {BOARD[1]} | {BOARD[2]}",
          BOARD_SEPARATOR,
          f"{BOARD[3]} | {BOARD[4]} | {BOARD[5]}",
          BOARD_SEPARATOR,
          f"{BOARD[6]} | {BOARD[7]} | {BOARD[8]}", sep="\n")


# resume
def validate_marker_position(position):
    valid = False

    while not valid:

        # Check that the entered number is between 1 and 9
        while position not in BOARD:
            position = input(f"\nInvalid value. {current_player}"
                             f"'s turn to choose a square (1-9): ")

        if BOARD[int(position) - 1] in BOARD:
            valid = True
        else:
            print("\nYou cannot go there. That spot has already been taken.")


def handle_player_turn(current_player, position):
    """
    DS4. This function takes in the current player and the position they want
    to place their marker in, and then places the marker in that position on
    the board.

    :param current_player: The current player's marker
    :param position: The position that the player wants to place their
    marker in
    """

    BOARD[position - 1] = current_player


def check_for_winner():
    """
    DS5. This function checks for a winner by calling the check_rows,
    check_columns, and check_diagonals functions
    :return: The winner of the game.
    """
    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


def check_rows():
    """
    If any of the rows have the same value, then the game is over and the
    winner is the value of the first element in the row
    :return: The winner of the game.
    """
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same value
    row_1 = BOARD[0] == BOARD[1] == BOARD[2] != 1 != 2 != 3
    row_2 = BOARD[3] == BOARD[4] == BOARD[5] != 4 != 5 != 6
    row_3 = BOARD[6] == BOARD[7] == BOARD[8] != 7 != 8 != 9
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return BOARD[0]
    elif row_2:
        return BOARD[2]
    elif row_3:
        return BOARD[6]
    return


def check_columns():
    """
    If any of the columns have all the same value, flag that there is a win and
    return the winner
    :return: The winner of the game.
    """
    # Set up global variables
    global game_still_going

    column_1 = BOARD[0] == BOARD[3] == BOARD[6] != 1 != 4 != 7
    column_2 = BOARD[1] == BOARD[4] == BOARD[7] != 2 != 5 != 8
    column_3 = BOARD[2] == BOARD[5] == BOARD[8] != 3 != 6 != 9

    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return BOARD[0]
    elif column_2:
        return BOARD[1]
    elif column_3:
        return BOARD[2]
    return


def check_diagonals():
    """
    If any of the diagonals have all the same value (and is not empty), flag
    that there is a win
    :return: The winner of the game.
    """
    # Set up global variables
    global game_still_going
    # check if any of the diagonal rows have all the same value
    diagonal_1 = BOARD[0] == BOARD[4] == BOARD[8] != 1 != 5 != 9
    diagonal_2 = BOARD[6] == BOARD[4] == BOARD[2] != 7 != 5 != 3
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return BOARD[0]
    elif diagonal_2:
        return BOARD[6]
    return


def check_if_tie():
    """
    If all the squares are filled, then the game is over
    :return: Nothing.
    """
    global game_still_going
    if (
        "1" not in BOARD and "2" not in BOARD and "3" not in BOARD and
        "4" not in BOARD and "5" not in BOARD and "6" not in BOARD and
        "7" not in BOARD and "8" not in BOARD and "9" not in BOARD
    ):
        game_still_going = False
    return


def flip_player():
    """
    If the current player is X, then change it to O, and if the current player
    is O, then change it to X
    :return: The current player
    """
    # Set up global variable
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
