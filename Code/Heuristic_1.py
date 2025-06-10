import math
from board import Board

import time
start_time = time.time()


def heuristic_function(board, player, opponent):
    """
    A heuristic evaluation function for the board.
    Considers winning moves, blocking opponent, and positional advantage.
    """
    board_size = len(board)
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    score = 0

    def count_consecutive(row, col, dr, dc, target):
        """Counts consecutive pieces and returns the count."""
        count = 0
        open_ends = 0

        # Count in the forward direction
        for step in range(6):
            r, c = row + step * dr, col + step * dc
            if 0 <= r < board_size and 0 <= c < board_size:
                if board[r][c] == target:
                    count += 1
                elif board[r][c] == 0:
                    open_ends += 1
                    break
                else:
                    break
        #
        # # Count in the backward direction
        # for step in range(1, 6):  # Skip the starting cell
        #     r, c = row - step * dr, col - step * dc
        #     if 0 <= r < board_size and 0 <= c < board_size:
        #         if board[r][c] == target:
        #             count += 1
        #         elif board[r][c] == 0:
        #             open_ends += 1
        #             break
        #         else:
        #             break

        return count, open_ends

    # Assign positional weight (favoring center positions)
    def positional_weight(row, col):
        """Returns weight based on proximity to the center."""
        center = board_size // 2
        return (center - abs(center - row)) + (center - abs(center - col))

    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] != 0:
                current_player = board[row][col]
                for dr, dc in directions:
                    count, open_ends = count_consecutive(row, col, dr, dc, current_player)

                    # Assign scores based on patterns
                    if count >= 6:
                        if current_player == player:
                            return 100000  # Immediate win
                        else:
                            return -100000  # Immediate loss
                    elif count == 5:
                        if current_player == player:
                            score += 10000 * open_ends
                        else:
                            score -= 10000 * open_ends
                    elif count == 4:
                        if current_player == player:
                            score += 1000 * open_ends
                        else:
                            score -= 1000 * open_ends
                    elif count == 3:
                        if current_player == player:
                            score += 100 * open_ends
                        else:
                            score -= 100 * open_ends
                    elif count == 2:
                        if current_player == player:
                            score += 10 * open_ends
                        else:
                            score -= 10 * open_ends

            # Add positional weight for the current cell
            if board[row][col] == player:
                score += positional_weight(row, col)
            elif board[row][col] == opponent:
                score -= positional_weight(row, col)

    return score


def get_possible_moves(board):
    """Returns a list of all possible moves (row, col) on the board."""
    board_size = len(board)
    return [(row, col) for row in range(board_size) for col in range(board_size) if board[row][col] == 0]

def minimax(board, depth, is_maximizing, current_player, opponent , alpha, beta):
    """
    Minimax algorithm with enhanced evaluation and threat detection.
    """
    possible_moves = get_possible_moves(board)
    # Terminal conditions
    if depth == 0 or not possible_moves:
        return  heuristic_function(board, current_player, opponent), None

    # Check for immediate wins or blocks
    for move in possible_moves:
        row, col = move
        # Check AI's winning move
        board[row][col] = current_player
        if  heuristic_function(board, current_player, opponent) == 100000:
            board[row][col] = 0
            return 100000, move  # Take winning move
        board[row][col] = 0

        # Check opponent's winning move
        board[row][col] = opponent
        if  heuristic_function(board, opponent, current_player) == -100000:
            board[row][col] = 0
            return -100000, move  # Block opponent's win
        board[row][col] = 0

    best_score = -math.inf if is_maximizing else math.inf
    best_move = None

    for move in possible_moves:
        row, col = move
        board[row][col] = current_player if is_maximizing else opponent  # Simulate move
        score, _ = minimax( board, depth - 1, not is_maximizing, current_player, opponent,alpha, beta)
        board[row][col] = 0  # Undo move
        # print(f"score: {score} , move: {move} , best_score: {best_score} \n")
        if is_maximizing:
            if score > best_score:
                best_score, best_move = score, move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        else:
            if score < best_score:
                best_score, best_move = score, move
                beta = min(beta, score)
                if beta <= alpha:
                    break

    return best_score, best_move

def heuristic_move(board):
    """Gets the AI's move."""
    current_player = 2
    opponent = 1
    _, best_move = minimax(board.board, depth= 3, is_maximizing=True, current_player=current_player, opponent=opponent, alpha= -math.inf, beta= math.inf)
    return best_move


# # Example Game Simulation
# board = Board(19)
#
# board.board[3][1] = 2
# board.board[3][2] = 2
# board.board[3][3] = 2
# board.board[3][4] = 2
#
#
#
# board.board[6][5] = 1
# board.board[6][6] = 1
# board.board[6][7] = 1
# board.board[6][8] = 1
#
# board.print_board()
#
# ai_move = heuristic_move(board)
# board.board[ai_move[0]][ai_move[1]] = 2
#
# # Get AI move and print it
# print("\nAI recommends move:", ai_move)
# board.print_board()
#
#
# end_time = time.time()
# print(f"Execution time: {end_time - start_time:.6f} seconds")