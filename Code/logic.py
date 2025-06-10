import random
from board import Board
from minimax import minimax_move
from alphbeta import alphbeta_move
from Heuristic_1 import heuristic_move

class Connect6Logic:
    def __init__(self, mode,user_board_size):
        self.user_board_size = int( user_board_size)
        self.board = Board(board_size= self.user_board_size)
        self.board_size = self.board.board_size
        self.mode = mode
        self.current_player = 1
        self.moves_made = 0
        self.max_moves_per_turn = 2
        self.turn = 0
        self.vsai = 1 if mode.lower() != "pvp" else 0

    def is_valid_move(self, row, col):
        if 0 <= row < self.board.board_size and 0 <= col < self.board.board_size:
            return self.board.board[row][col] == 0  # Check if the cell is empty
        return False

    def place_piece(self, row, col):
        if self.is_valid_move(row, col):
            self.board.board[row][col] = self.current_player
            if self.turn == 0:
                self.moves_made += 2
            else:
                self.moves_made += 1
            print(f"player {self.current_player} played({row}, {col})")
        self.turn += 1


    def switch_player(self):
        if self.moves_made >= self.max_moves_per_turn:
            self.current_player = 3 - self.current_player  # Switch between player 1 and 2
            self.moves_made = 0
        elif self.vsai and self.moves_made == 2:
            self.ai_move()


    def aai_moves(self, mode ):
        """
        Makes AI moves using the get_ai_move function.
        """
        self.current_player = 2  # Set AI as the current player
        moves_placed = 0  # Counter to track how many moves the AI has made in this turn
        while moves_placed < self.max_moves_per_turn:
            if mode.lower() == "minimax":
                best_move = minimax_move(self.board)
            if mode.lower() == "alphbeta":
                best_move = alphbeta_move(self.board)
            if mode.lower() == "heuristic":
                best_move = heuristic_move(self.board)
            if best_move:
                row, col = best_move
                if self.is_valid_move(row, col):
                    self.place_piece(row, col)  # Place the AI's move
                    return best_move
                    moves_placed += 1
                else:
                    print(f"Invalid move suggested by AI: ({row}, {col})")
                # lehh 3aml nfs el 7ag amrteen yacta
            else:
                print("AI did not suggest a valid move.")
                break  # Stop the loop if no valid move is returned

        # After AI has completed its moves, switch to human player
        self.switch_player()  # Switch back to the human player

    def check_win(self, row, col):
        return any(self.count_in_direction(row, col, dr, dc) >= 6
                   for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1),
                                  (-1, -1), (1, 1), (-1, 1), (1, -1)])
    def count_in_direction(self, row, col, dr, dc):
        count = 1  # Include the current piece
        for step in (-1, 1):  # Check both directions
            r, c = row + step * dr, col + step * dc
            while 0 <= r < self.board.board_size and 0 <= c < self.board.board_size and self.board.board[r][c] == self.current_player:
                count += 1
                r += step * dr
                c += step * dc
        return count

    # def reset_game(self):
    #     self.board = Board(self.board.board_size)  # Recreate a new board
    #     self.current_player = 1
    #     self.moves_made = 0
    #     self.turn = 0
    #     print("Game has been reset.")
    #
    def check_draw(self):
        for row in range(self.board.board_size):
            for col in range(self.board.board_size):
                if self.board.board[row][col] == 0:  # Check if any cell is empty
                    return False  # Not a draw since there are still empty cells
        # If the board is full and no one has won, it's a draw
        return True
