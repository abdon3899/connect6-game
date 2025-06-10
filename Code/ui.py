import tkinter as tk
from tkinter import messagebox
from logic import Connect6Logic


class Connect6UI:
    def __init__(self, root, mode,board_size):
        self.root = root
        self.mode = mode
        self.board_size = board_size
        self.root.title("Connect 6")
        if mode == "pvp":
            self.game_logic = Connect6Logic(mode= self.mode,user_board_size= self.board_size)
            print(self.mode)
        elif mode == "minimax":
            self.game_logic = Connect6Logic(mode= self.mode,user_board_size= self.board_size)
            print(self.mode)
        elif mode == "alphbeta":
            self.game_logic = Connect6Logic(mode= self.mode,user_board_size= self.board_size)
            print(self.mode)
        elif mode == "heuristic":
            self.game_logic = Connect6Logic(mode= self.mode,user_board_size= self.board_size)
            print(self.mode)

        # UI settings
        self.cell_size = 30
        # Create the canvas for the board
        self.canvas = tk.Canvas(self.root,
                                 width=self.game_logic.board_size * self.cell_size,
                                 height=self.game_logic.board_size * self.cell_size, bg="white")
        self.canvas.pack()
        # Draw the grid
        self.draw_grid()
        # Bind mouse clicks
        self.canvas.bind("<Button-1>", self.handle_click)

        # self.place_piece(0, 0)

    def draw_grid(self):
        for i in range(self.game_logic.board_size):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.game_logic.board_size * self.cell_size, fill="black")
            self.canvas.create_line(0, x, self.game_logic.board_size * self.cell_size, x, fill="black")

    def handle_click(self, event):
        row, col = event.y // self.cell_size, event.x // self.cell_size
        self.logicc(row, col)


    def logicc(self , row ,col):
        if self.mode == "pvp":
            if self.game_logic.is_valid_move(row, col):
                self.place_piece(row,col)
                # print(self.game_logic.moves_made)
                self.draw()
                if self.game_logic.check_win(row,col):
                    self.declare_winner()
                if self.game_logic.moves_made == 2:
                    self.moves_made_this_turn = 0
                    self.game_logic.switch_player()
        elif self.mode != "pvp":
            if self.game_logic.is_valid_move(row, col):
                self.place_piece(row, col)
                self.draw()
                if self.game_logic.check_win(row, col):
                    self.declare_winner()
                if self.game_logic.moves_made == 2:
                    self.moves_made_this_turn = 0
                    self.handle_ai_turn()


    def place_piece(self, row, col ):
            self.game_logic.place_piece(row, col)  # Update game logic
            x1, y1 = col * self.cell_size + 2, row * self.cell_size + 2
            x2, y2 = (col + 1) * self.cell_size - 2, (row + 1) * self.cell_size - 2
            if self.game_logic.current_player == 1 :
                self.canvas.create_oval(x1, y1, x2, y2, fill="black")
            elif self.game_logic.current_player == 2 :
                self.canvas.create_oval(x1, y1, x2, y2, fill="green")


    def handle_ai_turn(self):
        self.moves = 0
        while self.moves < 2:
            self.game_logic.current_player = 2
            ai_moves = self.game_logic.aai_moves(self.mode)
            row, col = ai_moves  # Extract row and col
            self.place_piece(row, col)  # Draw the piece on the canvas
            self.game_logic.place_piece(row, col)  # Update game logic
            self.moves += 1
            # Check if AI's move results in a win
            self.draw()
            if self.game_logic.check_win(row, col):
                self.declare_winner()
                return  # End the turn if AI wins
            # Switch back to human player
        self.game_logic.switch_player()


    def declare_winner(self):

        if self.mode != "pvp" :
            if self.game_logic.current_player == 2:
                winner = f" ai wins xd!"
                # self.reset_game()
            else:
                winner = f" you outplayed the ai good job"
            messagebox.showinfo("Game Over", winner)
            # self.reset_game()
        else:
            winner = f"Player {self.game_logic.current_player} wins!"
            messagebox.showinfo("Game Over", winner)
        # self.reset_game()

    def draw(self):
        if self.game_logic.check_draw() :
            messagebox.showinfo("draw plese start anther game")
            return False
        return True






class ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Selection Window")
        self.root.geometry("650x600")

        # Centering the label in the grid
        self.start = tk.Label(self.root, text="Connect6", font=("Courier", 25, "bold"))
        self.start.grid(row=0, column=1)

        # Label and entry for board size
        self.boardd = tk.Label(self.root, text="Board size:", font=("Courier", 20))
        self.boardd.grid(row=1, column=0)

        self.board = tk.Entry(self.root, width=21, font=("Courier", 15))
        self.board.grid(row=1, column=1)

        # Button to print the board size
        self.enter_button = tk.Button(self.root, text="Enter", font=("Courier", 15), command=self.print_board_size)
        self.enter_button.grid(row=1, column=2)

        # Buttons for other modes
        self.pvp_button = tk.Button(self.root, text="PVP", font=("Courier", 15), command=self.start_pvp)
        self.pvp_button.grid(row=3, column=1, pady=20)

        self.ai_minimax = tk.Button(self.root, text="ai_MiniMax", font=("Courier", 15), command=self.ai_MiniMax)
        self.ai_minimax.grid(row=4, column=0, pady=20)
        self.alph_beta = tk.Button(self.root, text="ai_AlphBeta", font=("Courier", 15), command=self.ai_AlphBeta)
        self.alph_beta.grid(row=4, column=1, pady=20)
        self.heuristic = tk.Button(self.root, text="ai_Heuristic", font=("Courier", 15), command=self.ai_Heuristic)
        self.heuristic.grid(row=4, column=2, pady=20)

        self.credits = tk.Button(self.root, text="credits", font=("Courier", 15), command=self.credits)
        self.credits.grid(row=5, column=1, pady=20)

    def print_board_size(self):
        board_size = self.board.get()  # Get the value from the input field
        if int(board_size) < 6:
            print(f"Board size entered: {board_size}")  # Print the value to the console
            print("this size is too small")
        else:
            print(f"Board size entered: {board_size}")  # Print the value to the console
            return board_size

    def start_pvp(self):
        root = tk.Tk()
        board_size = self.print_board_size()  # Get the value from the input field

        game = Connect6UI(root, mode="pvp",board_size= board_size)
        self.root.destroy()

    def ai_MiniMax(self):
        root = tk.Tk()
        board_size = self.print_board_size()  # Get the value from the input field

        game = Connect6UI(root, mode="minimax",board_size= board_size)
        self.root.destroy()

    def ai_AlphBeta(self):
        root = tk.Tk()
        board_size = self.print_board_size()  # Get the value from the input field

        game = Connect6UI(root, mode="alphbeta",board_size= board_size)
        self.root.destroy()

    def ai_Heuristic(self):
        root = tk.Tk()
        board_size = self.print_board_size()  # Get the value from the input field

        game = Connect6UI(root, mode="heuristic",board_size= board_size)
        self.root.destroy()

    def credits(self):
        print("im too lazy to write all the names")


    def run(self):
        self.root.mainloop()

# Create and run the UI
lol = ui()
lol.run()
