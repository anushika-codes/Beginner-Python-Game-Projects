# Tic Tac Toe game in Python

# Create board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check for win
def check_win(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print("Positions are from 1 to 9 as follows:")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")

    while True:
        print_board()
        move = input(f"Player {current_player}, choose your move (1-9): ")
        
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input. Please choose a number from 1 to 9.")
            continue
        
        move = int(move) - 1

        if board[move] != ' ':
            print("That spot is already taken. Try again.")
            continue

        board[move] = current_player

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()

