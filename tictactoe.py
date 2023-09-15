import random

board = [' ' for _ in range(9)]

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def is_board_full(board):
    return ' ' not in board


def is_game_over(board):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return True
    return is_board_full(board)


def evaluate_board(board):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == 'X':
            return 1
        elif board[combination[0]] == board[combination[1]] == board[combination[2]] == 'O':
            return -1
    return 0


def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return evaluate_board(board)

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    best_eval = float('-inf')
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move


while not is_game_over(board):
    print_board(board)

    human_move = int(input("Enter your move (0-8): "))
    if board[human_move] == ' ':
        board[human_move] = 'O'
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(board):
        break

    ai_move = find_best_move(board)
    board[ai_move] = 'X'

print_board(board)

if evaluate_board(board) == 1:
    print("AI wins!")
elif evaluate_board(board) == -1:
    print("Human wins!")
else:
    print("It's a tie!")
