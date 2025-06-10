from board import Board
import random

def get_ai_move(board):
    """
    Generate AI moves for the given board and player.
    Returns a list of valid moves (row, col) for the AI's turn.
    """
    # Ensure we're accessing the board size from the Board object
    board_size = board.board_size
    board_grid = board.board  # Access the board's grid

    # Collect all valid moves
    valid_moves = [
        (row, col)
        for row in range(board_size)
        for col in range(board_size)
        if board_grid[row][col] == 0  # Check if the cell is empty
    ]
    if not valid_moves:
        return None  # Return None if no valid moves are available
    # Shuffle the valid moves and select one
    random.shuffle(valid_moves)
    # print(board.board)
    best_move = valid_moves[0]
    return best_move  # Return up to one move

