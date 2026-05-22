import math

# Print board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check winner
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True

    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Check draw
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)

        return best_score

# AI Move
def ai_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = "O"

# Main Game
board = [[" " for _ in range(3)] for _ in range(3)]

print("TIC-TAC-TOE AI")
print("You are X | AI is O")

while True:
    print_board(board)

    # Human Move
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != " ":
        print("Cell already taken!")
        continue

    board[row][col] = "X"

    if check_winner(board, "X"):
        print_board(board)
        print("You win!")
        break

    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI Move
    ai_move(board)

    if check_winner(board, "O"):
        print_board(board)
        print("AI wins!")
        break

    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break