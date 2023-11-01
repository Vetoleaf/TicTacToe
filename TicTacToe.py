# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]
current_player = "X"


# Display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Take user input
def take_user_input():
    user_input = input(f"Player '{current_player}' select a number from 1-9 (or 'exit' to quit): ").upper()
    return user_input


display_board(board)

# Main Game Loop
while True:
    user_input = take_user_input()

    if user_input == "EXIT":
        break
    # Convert user input into int
    if user_input.isdigit():
        move = int(user_input) - 1
        # Validate input and place symbol
        if 0 <= move < 9 and board[move] == " ":
            board[move] = current_player
            display_board(board)

            # Check if the game is over
            if (board[0] == board[1] == board[2] != " " or
                    board[3] == board[4] == board[5] != " " or
                    board[6] == board[7] == board[8] != " " or
                    board[0] == board[3] == board[6] != " " or
                    board[1] == board[4] == board[7] != " " or
                    board[2] == board[5] == board[8] != " " or
                    board[0] == board[4] == board[8] != " " or
                    board[2] == board[4] == board[6] != " "):
                print(f"Player '{current_player}' wins!")
                break
            elif " " not in board:
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Please try again.")
    else:
        print("Invalid input. Please enter a number from 1-9 (or 'exit' to quit).")
