import random

WIDTH = 7
HEIGHT = 6
AI = 2
HUMAN = 1
EMPTY = 0
PROBABILITY = [0.6, 0.4]  # Probability of disc falling in chosen column and adjacent columns

# Create an empty board
def create_board():
    board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]
    return board

# Check if a column is full
def is_column_full(board, col):
    return board[0][col] != EMPTY

# Drop a disc in a column
def drop_disc(board, col, disc):
    for row in range(HEIGHT - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = disc
            return True
    return False

# Get the available columns to drop a disc
def get_available_columns(board):
    return [col for col in range(WIDTH) if not is_column_full(board, col)]

# Check if the board is full
def is_board_full(board):
    return all(is_column_full(board, col) for col in range(WIDTH))

# Check if a player has won
def is_winner(board, player):
    # Check rows
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True
    # Check columns
    for col in range(WIDTH):
        for row in range(HEIGHT - 3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(HEIGHT - 3):
        for col in range(WIDTH - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, HEIGHT):
        for col in range(WIDTH - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True
    return False

# Evaluate the heuristic value of the board for the AI player
def evaluate(board):
    ai_score = 0
    human_score = 0

    # Check rows
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            window = board[row][col:col+4]
            ai_score += evaluate_window(window, AI)
            human_score += evaluate_window(window, HUMAN)

    # Check columns
    for col in range(WIDTH):
        for row in range(HEIGHT - 3):
            window = [board[row+i][col] for i in range(4)]
            ai_score += evaluate_window(window, AI)
            human_score += evaluate_window(window, HUMAN)

    # Check diagonal (top-left to bottom-right)
    for row in range(HEIGHT - 3):
        for col in range(WIDTH - 3):
            window = [board[row+i][col+i] for i in range(4)]
            ai_score += evaluate_window(window, AI)
            human_score += evaluate_window(window, HUMAN)

    # Check diagonal (bottom-left to top-right)
    for row in range(3, HEIGHT):
        for col in range(WIDTH - 3):
            window = [board[row-i][col+i] for i in range(4)]
            ai_score += evaluate_window(window, AI)
            human_score += evaluate_window(window, HUMAN)

    return ai_score - human_score

# Evaluate a window of 4 cells
def evaluate_window(window, player):
    score = 0
    opponent = HUMAN if player == AI else AI

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
       score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

# Get the best column for the AI player to play
def get_best_column(board, depth, maximizing_player):
    available_columns = get_available_columns(board)

    if depth == 0 or is_board_full(board) or is_winner(board, AI) or is_winner(board, HUMAN):
        return None, evaluate(board)

    if maximizing_player:
        max_value = float('-inf')
        best_column = random.choice(available_columns)

        for col in available_columns:
            new_board = [row[:] for row in board]
            drop_disc(new_board, col, AI)
            _, value = get_best_column(new_board, depth - 1, False)

            if value > max_value:
                max_value = value
                best_column = col

        return best_column, max_value
    else:
        min_value = float('inf')
        best_column = random.choice(available_columns)

        for col in available_columns:
            new_board = [row[:] for row in board]
            drop_disc(new_board, col, HUMAN)
            _, value = get_best_column(new_board, depth - 1, True)

            if value < min_value:
                min_value = value
                best_column = col

        return best_column, min_value

# Play the game
def play_game():
    board = create_board()
    print_board(board)
    turn = HUMAN

    while not is_board_full(board):
        if turn == HUMAN:
            col = int(input("Choose a column to play (0-6): "))
            if col not in get_available_columns(board):
                print("Invalid column. Please choose a different column.")
                continue
        else:
            col, _ = get_best_column(board, 5, True)
            print("AI plays column", col)

        drop_disc(board, col, turn)
        print_board(board)

        if is_winner(board, turn):
            print("Player", turn, "wins!")
            return

        turn = AI if turn == HUMAN else HUMAN

    print("It's a tie!")

# Print the board
def print_board(board):
    for row in board:
        print(row)
    print()

# Start the game
play_game()