# To create an imaginary opponent.

from random import randint

game_board = []


player = "player"

# Creates the 5x5 matrix.

def build_game_board(board):
    for i in range(5):
        board.append(["O"] * 5)


def show_board(board):
    print("Find and sink the ship!")
    for row in board:
        print(" ".join(row))


# Assigning the generated random numbers to ship_row and ship_col.

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
total_turns = 0

def player_turns():

    if total_turns %2 == 0:
        return player
   

# Allows new game to start


def play_again():
    answer = str(input("Would you like to play again? y/n"))
    if answer == "yes" or answer == "y":
       ship_points = load_game(game_board)
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
        print("Congratulations! you got it!")
        print("Thanks for playing!")
        play_again()
    elif not match:
        if not_on_game_board:
            print("Out of range")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed!")
            board[guess_row][guess_col] = "X"
        show_board(game_board)
    else:
        return 0

for attempt in range(total_turns):
 
  guess_row = int(raw_input("Guess Row:"))
  guess_col = int(raw_input("Guess Col:"))

  if guess_row == ship_row and guess_col == ship_col:
      print ("Congratulations! You sunk my battleship!")
      break
  else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
          print "Oops, that's not even in the ocean."
      elif(board[guess_row][guess_col] == "X"):
          print "You guessed that one already!!!"
      else:
          print "You missed my battleship!"
          board[guess_row][guess_col] = "X"

      print "Turn %d \n" % (turn + 1) 
      print_board(board)
      turn = turn + 1
      
      if turn == NO_USER_GUESS:
          print "Game Over"
