from random import randint
import time
import os
from colorama import Fore

# Initialize boards
hidden_board = [["_"] * 9 for x in range(9)]
guess_board = [["_"] * 9 for x in range(9)]
player_board = [["_"] * 9 for x in range(9)]

# Maps for letters and numbers
numbers_to_letters = {i: chr(65+i) for i in range(9)}  # A-I
letters_to_numbers = {chr(65+i): i for i in range(9)}  # A-I

continue_game_options = ['ok', 'end game']

def clear():
    """Clear the terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def start_menu():
    """Main menu with loading screen."""
    print('\033[1;32m                   LOADING...')
    print('                  [■■■■■□□□□□] 50%')
    time.sleep(2)
    print('                   LOADING...')
    print('                  [■■■■■■■■■□] 90%')
    time.sleep(2)
    clear()
    print('\033[1;32m_________________________________________')
    print('_________________________________________')
    print('    Hello and Welcome to Battleship Game!\n')
    print('                        ____||__  _____||__')
    print('                ____||_ )________( )_________( ')
    print(' At the beginning, choose one of the options:')
    print('1. Play the game')
    print('2. Read Instructions.')
    start = input('Enter your option here:\n')

    if start == '1':
        choose_difficulty()
    elif start == '2':
        instructions()
    else:
        print(Fore.RED + 'Incorrect!!!')
        print(Fore.RED + f' You entered: {start}. Please enter 1 or 2.\n')
        print('\033[1;32m Please, try again: ')
        start_menu()

def choose_difficulty():
    """Choose difficulty level."""
    clear()
    print("Choose your difficulty level:")
    print("1. Easy (15 turns, 8 ships)")
    print("2. Medium (10 turns, 10 ships)")
    print("3. Hard (7 turns, 12 ships)")
    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == '1':
        start_game(turns=15, ships=8)
    elif difficulty == '2':
        start_game(turns=10, ships=10)
    elif difficulty == '3':
        start_game(turns=7, ships=12)
    else:
        print(Fore.RED + "Invalid choice! Please select 1, 2, or 3.")
        choose_difficulty()

def start_game(turns, ships):
    """Start game with chosen difficulty."""
    clear()
    create_random_ships(hidden_board, ships)
    create_random_ships(player_board, ships)
    print(f"Game Mode: {'Easy' if turns == 15 else 'Medium' if turns == 10 else 'Hard'}")
    print(f"You have {turns} turns to find {ships} ships.")
    play_game(turns)

def instructions():
    """Show game instructions."""
    print('Welcome to BATTLESHIP!')
    print("You have a set number of turns to find the computer's ships.")
    print("Use row numbers (1-9) and column letters (A-I) to guess ship locations.")
    print("Good luck and have fun!")
    input("Press Enter to start the game.")
    choose_difficulty()

def create_random_ships(board, num_ships):
    """Place random ships on the board."""
    for _ in range(num_ships):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "✩":
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = "✩"

def computer_guess():
    """Simulate computer guessing player’s board."""
    computer_row, computer_column = randint(0, 8), randint(0, 8)
    if player_board[computer_row][computer_column] in ["-", "★"]:
        computer_row = randint(0, 9)
        computer_column = randint(0, 9)
    elif player_board[computer_row][computer_column] == "✩":
        print(f"The computer guessed row {computer_row+1} and column {numbers_to_letters[computer_column]}")
        print("Your battleship has been hit!")
        player_board[computer_row][computer_column] = "★"
    else:
        print(f"The computer guessed row {computer_row+1} and column {numbers_to_letters[computer_column]}")
        print("The computer missed!")
        player_board[computer_row][computer_column] = "-"

def ship_location():
    """Get player's guess for ship location."""
    row = input('Choose a row (1-9): ')
    while row not in "123456789" or len(row) > 1:
        print(Fore.RED + 'Invalid input! Choose a number between 1 and 9.')
        row = input('Choose a row (1-9): ')

    column = input('Choose a column (A-I): ')
    while column not in "ABCDEFGHI" or len(column) > 1:
        print(Fore.RED + 'Invalid input! Choose a letter between A and I.')
        column = input('Choose a column (A-I): ')

    return int(row) - 1, letters_to_numbers[column]

def hit_ships(board):
    """Count the number of hits on the board."""
    return sum(row.count("★") for row in board)

def play_game(turns):
    """Main game loop."""
    while turns > 0:
        print("\nYour Board:")
        print_board(player_board)
        print("\nComputer's Board:")
        print_board(guess_board)

        row, column = ship_location()
        if guess_board[row][column] in ["-", "★"]:
            print(Fore.RED + "You already guessed that location!")
        elif hidden_board[row][column] == "✩":
            print(Fore.GREEN + "You hit a ship!")
            guess_board[row][column] = "★"
            turns -= 1
        else:
            print(Fore.YELLOW + "You missed!")
            guess_board[row][column] = "-"
            turns -= 1

        computer_guess()
        if hit_ships(guess_board) == 10:
            print(Fore.GREEN + "Congratulations! You've sunk all the ships!")
            break
        print(f"You have {turns} turns remaining.")

        if turns == 0:
            print(Fore.RED + "Game over! You've run out of turns.")
            break

def print_board(board):
    """Display the current board."""
    print("  A B C D E F G H I")
    for idx, row in enumerate(board, start=1):
        print(f"{idx} " + " ".join(row))

def play_again():
    """Option to replay the game."""
    answer = input("Play again? (y/n): ")
    if answer.lower() == 'y':
        start_menu()
    else:
        exit()

if __name__ == "__main__":
    start_menu()
