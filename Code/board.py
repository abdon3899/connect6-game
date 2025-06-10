
class Board:
    def __init__(self,board_size = 19):
        self.board_size = board_size
        self.board = self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        #creat a grid that have a size of board size  and set it all to 0 if a player makes a move change the block to 1 or 2


    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
