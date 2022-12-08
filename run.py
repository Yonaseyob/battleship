from random import randint

game_board = []
player_one = {
    "name": "Player 1"
    
}
player_two = {
    "name": "computer"
}
TOTAL_TURNS = 0

# Building our 5 x 5 board


def build_game_board(board):
    for i in range(5):
        board.append(["O"] * 5)


def show_board(board):
    print("Find and sink the ship!")
    for row in board:
        print(" ".join(row))

# Defining ships locations


def load_game(board):
    print("WELCOME TO BATTLESHIP!")
    print("START")
    build_game_board(board)
    show_board(board)
    ship_col = randint(1, len(board))
    ship_row = randint(1, len(board[0]))
    return {
        'ship_col': ship_col,
        'ship_row': ship_row,
    }


ship_points = load_game(game_board)

# Players will alternate turns.


def player_turns():
    if total_turns % 2 == 0:
        return player_two
    else:
        return player_one

# Allows new game to start


def play_again():
    answer = str(input("Would you like to play again?"))
    if answer == "yes" or answer == "y":
        
      else:
    print("Thanks for playing!")
    exit()

# What will be done with players guesses


def input_check(ship_row, ship_col, player, board):
    guess_col = 0
    guess_row = 0
    while True:
        try:
            guess_row = int(input("Guess Row:")) - 1
            guess_col = int(input("Guess Col:")) - 1
        except ValueError:
            print("Enter a number only.")
            continue
        else:
            break
    match = guess_row == ship_row - 1 and guess_col == ship_col - 1
    not_on_game_board = (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)

    if match:
        player["wins"] += 1
        print("Congratulations! You sunk my battleship!")
        print("Thanks for playing!")
        play_again()
    elif not match:
        if not_on_game_board:
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        show_board(game_board)
    else:
        return 0

# GAME - 3 games in total

for games in range(3):
    games += 1
    for turns in range(6):
        total_turns += 1
        if player_turns() == player_one:
            print("Player One")
            input_check(
                ship_points['ship_row'],
                ship_points['ship_col'],
                player_one, game_board
            )
        elif player_turns() == player_two:
            print("Player Two")
            input_check(
                ship_points['ship_row'],
                ship_points['ship_col'],
                player_two, game_board
            )
        else:
            continue
        if total_turns == 6 and player_turns() == player_one:
            print("The game is a draw")
            play_again()
        elif total_turns == 6 and player_turns() == player_two:
            print("The game is a draw")
            play_again()
        else:
            continue