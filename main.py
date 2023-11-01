import random

# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------")
    print(f"{board[3]} | {board[4]} | {board[5]}\n---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_win(board, player):
    for i in range(0, 9, 3):
        if all(board[i + j] == player for j in range(3)):
            return True
    for i in range(3):
        if all(board[i + j] == player for j in range(0, 9, 3)):
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return " " not in board

# AI player's move using a simple random choice
def ai_move(board):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move

# Main game loop
def play_game():
    player = "X"
    ai = "O"

    while True:
        display_board(board)
        if player == "X":
            try:
                move = int(input("Enter your move (0-8): "))
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue
        else:
            print("AI is making a move...")
            move = ai_move(board)

        board[move] = player

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        player, ai = ai, player

if __name__ == "__main__":
    play_game()
