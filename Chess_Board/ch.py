import tkinter as tk
from tkinter import messagebox

class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.selected_piece = None
        self.current_player = "w"  # 'w' for white, 'b' for black

        self.square_size = 60
        self.canvas = tk.Canvas(
            self.root, width=8 * self.square_size, height=8 * self.square_size
        )
        self.canvas.pack()

        self.piece_symbols = {
            "wP": "\u2659", "wR": "\u2656", "wN": "\u2658", "wB": "\u2657", "wQ": "\u2655", "wK": "\u2654",
            "bP": "\u265F", "bR": "\u265C", "bN": "\u265E", "bB": "\u265D", "bQ": "\u265B", "bK": "\u265A"
        }

        self.canvas.bind("<Button-1>", self.on_square_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                piece = self.board[row][col]
                if piece:
                    self.canvas.create_text(
                        x1 + self.square_size // 2,
                        y1 + self.square_size // 2,
                        text=self.piece_symbols[piece],
                        font=("Arial", self.square_size // 2),
                        fill="black" if piece[0] == "b" else "light gray"
                    )

    def on_square_click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size

        if self.selected_piece:
            self.move_piece(row, col)
        elif self.board[row][col] and self.board[row][col][0] == self.current_player:
            self.selected_piece = (row, col)

    def move_piece(self, target_row, target_col):
        src_row, src_col = self.selected_piece
        piece = self.board[src_row][src_col]

        if self.is_valid_move(src_row, src_col, target_row, target_col):
            self.board[target_row][target_col] = piece
            self.board[src_row][src_col] = ""
            self.current_player = "b" if self.current_player == "w" else "w"

        self.selected_piece = None
        self.draw_board()

    def is_valid_move(self, src_row, src_col, target_row, target_col):
        # Basic move validation (placeholder for actual chess rules)
        target_piece = self.board[target_row][target_col]
        if target_piece and target_piece[0] == self.current_player:
            return False
        return True

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = ChessGame()
    game.start()
