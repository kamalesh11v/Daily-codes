import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -10 + depth
    elif check_winner(board, "O"):
        return 10 - depth
    elif not get_available_moves(board):
        return 0
    
    if is_maximizing:
        max_eval = float("-inf")
        for i, j in get_available_moves(board):
            board[i][j] = "O"
            eval_score = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_available_moves(board):
            board[i][j] = "X"
            eval_score = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval_score)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i, j in get_available_moves(board):
        board[i][j] = "O"
        eval_score = minimax(board, 0, False)
        board[i][j] = " "
        if eval_score > best_eval:
            best_eval = eval_score
            best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)
    
    while True:
        player_move = tuple(map(int, input("Enter your move (row column): ").split()))
        if board[player_move[0]][player_move[1]] == " ":
            board[player_move[0]][player_move[1]] = "X"
            print_board(board)
            if check_winner(board, "X"):
                print("You win!")
                break
            elif not get_available_moves(board):
                print("It's a draw!")
                break
            
            print("AI is making a move...")
            ai_move = get_best_move(board)
            board[ai_move[0]][ai_move[1]] = "O"
            print_board(board)
            if check_winner(board, "O"):
                print("AI wins!")
                break
            elif not get_available_moves(board):
                print("It's a draw!")
                break
        else:
            print("Invalid move, try again.")

play_game()
