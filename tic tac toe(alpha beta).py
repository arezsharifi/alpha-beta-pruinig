"""
Tic-Tac-Toe AI using Alpha-Beta Pruning
"""

PLAYER = 'X'
AI = 'O'
EMPTY = ' '


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_winner(board, player):
    wins = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player] * 3 in wins


def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def evaluate(board):
    if is_winner(board, AI):
        return 1
    if is_winner(board, PLAYER):
        return -1
    return 0


def alpha_beta_ttt(board, depth, alpha, beta, maximizing):
    score = evaluate(board)

    if score != 0:
        return score
    if is_full(board):
        return 0

    if maximizing:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, alpha_beta_ttt(board, depth + 1, alpha, beta, False))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = min(best, alpha_beta_ttt(board, depth + 1, alpha, beta, True))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
        return best


def best_move(board):
    best_val = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                val = alpha_beta_ttt(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = EMPTY
                if val > best_val:
                    best_val = val
                    move = (i, j)
    return move


def play():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Tic-Tac-Toe — You are X, AI is O")
    print_board(board)

    while True:
        # Player move
        try:
            r, c = map(int, input("Enter row col (0-2): ").split())
            if board[r][c] != EMPTY:
                print("Cell taken!")
                continue
        except (ValueError, IndexError):
            print("Invalid input!")
            continue

        board[r][c] = PLAYER
        print_board(board)

        if is_winner(board, PLAYER):
            print("🎉 You win!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break

        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI
            print(f"AI plays {move}")
            print_board(board)

        if is_winner(board, AI):
            print("💻 AI wins!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break


if __name__ == '__main__':
    play()