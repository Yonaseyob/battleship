# Random module for randomly accepting the values
import random

ROWS = 5
COLUMNS = 5


def create_random_ship():
    """
    Sets the battleship board by importing random row and column strings
    """
    return random.randrange(ROWS), random.randrange(COLUMNS)


def play_again():
    """
    After the given guess chances are finished the player will give 
    another try if the player will play again
    """
    try_again = input("Do you want to play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
    else:
        print("Goodbye!")
        return


print("Welcome to the Battleship game!")

print("Lets play")


def play_game():
    """
    This sets the game board by placing battleships in randomly generated places 
    and defining the rules of the game and how the user should play 
    and same time getting feedback from the input
    """
    game_board = [["O"] * COLUMNS for _ in range(ROWS)]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 3
    guess = 5

    while guess:
        try:
            row = int(input("Enter a row"))
            column = int(input("Enter a column"))
        except ValueError:
            print("Only number between 1-5!")
            continue

        if row not in range(1,6) or column not in range(1, 6):
            print("The numbers must be between 1-5!")
            continue

        row = row - 1 
        column = column - 1 

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("You have already gussed")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print(" You got it that is a hit")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("Congradualations you win")
                play_again()
        else:
            print("You missed!")
            game_board[row][column] = "-"
            guess -= 1

        for i in game_board:
            print(*i)

        print(f"Guess left: {guess} | Ships left: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()