import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGUI:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.generate_mines()
        self.calculate_numbers()

        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.create_board()

    def generate_mines(self):
        mines = 0
        while mines < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines += 1

    def calculate_numbers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    continue
                for x in range(max(0, i - 1), min(self.rows, i + 2)):
                    for y in range(max(0, j - 1), min(self.cols, j + 2)):
                        if self.board[x][y] == -1:
                            self.board[i][j] += 1

    def create_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.master, text="", width=3, height=2, command=lambda row=i, col=j: self.reveal_cell(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def reveal_cell(self, row, col):
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            return

        if self.revealed[row][col]:
            return

        if self.board[row][col] == -1:
            self.reveal_all()
            tk.messagebox.showinfo("Game Over", "You hit a mine!")
        else:
            self.revealed[row][col] = True
            self.buttons[row][col].config(text=str(self.board[row][col]))

            if self.board[row][col] == 0:
                self.reveal_empty_cells(row, col)

    def reveal_empty_cells(self, row, col):
        for x in range(max(0, row - 1), min(self.rows, row + 2)):
            for y in range(max(0, col - 1), min(self.cols, col + 2)):
                if not self.revealed[x][y]:
                    self.reveal_cell(x, y)

    def reveal_all(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.revealed[i][j] = True
                self.buttons[i][j].config(text=str(self.board[i][j]))

def play_minesweeper_gui():
    root = tk.Tk()
    root.title("Minesweeper")

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    num_mines = int(input("Enter the number of mines: "))

    game = MinesweeperGUI(root, rows, cols, num_mines)

    root.mainloop()

if __name__ == "__main__":
    play_minesweeper_gui()
