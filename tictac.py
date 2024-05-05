import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        self.buttons = [[tk.Button(self, text="", width=10, height=3,
                                   command=lambda x=x, y=y: self.button_click(x, y))
                         for y in range(3)] for x in range(3)]

        for x in range(3):
            for y in range(3):
                self.buttons[x][y].grid(row=x, column=y)

    def button_click(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            self.buttons[x][y].config(text=self.current_player)

            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showerror("Tic Tac Toe", "Invalid move!")

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for x in range(3):
            for y in range(3):
                self.buttons[x][y].config(text="")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
