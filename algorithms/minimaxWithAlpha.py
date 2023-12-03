# Import necessary library
import random

# Function to initialize the game state
def initialize_game():
    return [0]*42  # Initialize the empty board

# Function to check if the board is full
def is_full(state):
    return 0 not in state

# Function to get available moves in the current state
def get_available_moves(state):
    available_moves = []
    for i in range(7):
        if state[i] == 0:
            available_moves.append(i)
    return available_moves

# Function to apply a move on the board
def apply_move(state, move, player):
    new_state = state[:]
    for i in range(5, -1, -1):
        if new_state[i * 7 + move] == 0:
            new_state[i * 7 + move] = player
            break
    return new_state

# Function to count sequences of a player in the current state
def count_sequences(state, player):
    sequences = 0
    for i in range(3):
        for j in range(7):
            if state[i * 7 + j] == state[(i + 1) * 7 + j] == state[(i + 2) * 7 + j] == state[(i + 3) * 7 + j] == player:
                sequences += 1  # Vertical sequence
    for i in range(6):
        for j in range(4):
            if state[i * 7 + j] == state[i * 7 + j + 1] == state[i * 7 + j + 2] == state[i * 7 + j + 3] == player:
                sequences += 1  # Horizontal sequence
    for i in range(3, 6):
        for j in range(4):
            if state[i * 7 + j] == state[(i - 1) * 7 + j + 1] == state[(i - 2) * 7 + j + 2] == state[(i - 3) * 7 + j + 3] == player:
                sequences += 1  # Diagonal sequence (from bottom-left to top-right)
    for i in range(3):
        for j in range(4):
            if state[i * 7 + j] == state[(i + 1) * 7 + j + 1] == state[(i + 2) * 7 + j + 2] == state[(i + 3) * 7 + j + 3] == player:
                sequences += 1  # Diagonal sequence (from top-left to bottom-right)
    return sequences

# Function to calculate heuristic value of the state
def heuristic(state):
    ai_sequences = count_sequences(state, 2)
    human_sequences = count_sequences(state, 1)

    # Potential future sequences
    ai_potential = count_potential_sequences(state, 2)
    human_potential = count_potential_sequences(state, 1)

    # Evaluate the state based on sequences and potential future sequences
    ai_score = ai_sequences * 100 + ai_potential * 10
    human_score = human_sequences * 100 + human_potential * 10

    return ai_score - human_score

def count_potential_sequences(state, player):
    potential_sequences = 0
    for i in range(6):
        for j in range(7):
            if state[i * 7 + j] == player:
                # Check horizontally
                if j < 4:
                    if state[i * 7 + j + 1] == state[i * 7 + j + 2] == state[i * 7 + j + 3] == 0:
                        potential_sequences += 1
                # Check vertically
                if i < 3:
                    if state[(i + 1) * 7 + j] == state[(i + 2) * 7 + j] == state[(i + 3) * 7 + j] == 0:
                        potential_sequences += 1
                # Check diagonally (bottom-left to top-right)
                if j < 4 and i < 3:
                    if state[(i + 1) * 7 + j + 1] == state[(i + 2) * 7 + j + 2] == state[(i + 3) * 7 + j + 3] == 0:
                        potential_sequences += 1
                # Check diagonally (top-left to bottom-right)
                if j < 4 and i > 2:
                    if state[(i - 1) * 7 + j + 1] == state[(i - 2) * 7 + j + 2] == state[(i - 3) * 7 + j + 3] == 0:
                        potential_sequences += 1
    return potential_sequences

# Function to calculate the expected minimax value and return the states list
def expected_minimax(state, depth, player):
    state_list = []
    state_list.append(state)
    
    if depth == 0 or is_full(state):
        return heuristic(state), state_list

    available_moves = get_available_moves(state)
    if player:
        max_eval = float('-inf')
        for move in available_moves:
            next_player = not player
            new_state = apply_move(state, move, player + 1)
            eval, new_states = expected_minimax(new_state, depth - 1, next_player)
            if eval > max_eval:
                max_eval = eval
                state_list.extend(new_states)
        return max_eval, state_list
    else:
        min_eval = float('inf')
        for move in available_moves:
            next_player = not player
            new_state = apply_move(state, move, player + 1)
            eval, new_states = expected_minimax(new_state, depth - 1, next_player)
            if eval < min_eval:
                min_eval = eval
                state_list.extend(new_states)
        return min_eval, state_list

# Function to get the best move using minimax with alpha-beta pruning
def get_best_move(state, depth):
    best_move = None
    max_eval = float('-inf')
    available_moves = get_available_moves(state)
    for move in available_moves:
        next_player = False  # The AI is playing

        new_state = apply_move(state, move, 2)  # AI's move
        eval = expected_minimax(new_state, depth - 1, next_player)[0]
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

# Function to print the board
def print_board(state):
    for i in range(6):
        row = state[i * 7: (i + 1) * 7]
        print(row)
    print()

# Main function to play the game
def play_game():
    state_list = []
    current_state = initialize_game()
    print("Initial Board:")
    print_board(current_state)
    state_list.append(current_state)

    while not is_full(current_state):
        # AI's turn
        ai_move = get_best_move(current_state, 4)
        current_state = apply_move(current_state, ai_move, 2)
        print("\nAfter AI's Move:")
        print_board(current_state)
        state_list.append(current_state)

        if is_full(current_state):
            break

        # Human's turn
        while True:
            try:
                human_move = int(input("Your turn - Enter column (0-6): "))
                if human_move < 0 or human_move > 6:
                    raise ValueError("Column number out of range. Please enter a number between 0 and 6.")
                if human_move not in get_available_moves(current_state):
                    raise ValueError("Column is full. Choose another column.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        current_state = apply_move(current_state, human_move, 1)
        print("\nAfter Your Move:")
        print_board(current_state)
        state_list.append(current_state)

    final_state = current_state
    ai_sequences = count_sequences(final_state, 2)
    human_sequences = count_sequences(final_state, 1)

    print("\nGame Over!")
    print(f"AI Sequences: {ai_sequences}")
    print(f"Human Sequences: {human_sequences}")
    if ai_sequences > human_sequences:
        print("AI Wins!")
    elif ai_sequences < human_sequences:
        print("Human Wins!")
    else:
        print("It's a Tie!")

    return state_list, final_state

# Main function to run the game
def main():
    states_list, final_state = play_game()
    ai_sequences_final = count_sequences(final_state, 2)
    human_sequences_final = count_sequences(final_state, 1)
    print("\nFinal State:")
    print_board(final_state)
    print(f"AI Sequences in Final State: {ai_sequences_final}")
    print(f"Human Sequences in Final State: {human_sequences_final}")
    if ai_sequences_final > human_sequences_final:
        print("AI Wins!")
    elif ai_sequences_final < human_sequences_final:
        print("Human Wins!")
    else:
        print("It's a Tie!")

    return states_list

if __name__ == "__main__":
    final_states_list = main()