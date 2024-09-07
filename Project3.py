import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

def print_board():
    """Prints the Tic-Tac-Toe board."""
    print('---------')
    for i in range(3):
        print('| ' + ' | '.join(board[i*3:(i+1)*3]) + ' |')
        print('---------')

def check_winner(board, player):
    """Checks if a player has won the game."""
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board

def player_move():
    """Gets the player's move and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. The cell is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def computer_move():
    """Generates a random move for the computer."""
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        computer_move()
        print("Computer's move:")
        print_board()
        if check_winner(board, 'O'):
            print("Sorry, the computer wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
