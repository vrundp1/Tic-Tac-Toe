import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.players = ["X", "O"]
        self.current_player = random.choice(self.players)

        self.label = tk.Label(root, text=self.current_player + "'s turn", font=('Helvetica', 30))
        self.label.pack(side="top")

        self.reset_button = tk.Button(root, text="New Game", font=('Helvetica', 15), command=self.new_game)
        self.reset_button.pack(side="top")

        self.x_wins = 0
        self.o_wins = 0

        self.x_wins_label = tk.Label(root, text="X Wins: 0", font=('Helvetica', 15))
        self.x_wins_label.pack(side="top")

        self.o_wins_label = tk.Label(root, text="O Wins: 0", font=('Helvetica', 15))
        self.o_wins_label.pack(side="top")

        self.create_game_grid()

    def create_game_grid(self):
        self.buttons = [[0, 0, 0] for _ in range(3)]

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for row in range(3):
            row_buttons = []
            for column in range(3):
                button = tk.Button(self.frame, text="", font=('Helvetica', 30), width=5, height=2,
                                   command=lambda r=row, c=column: self.next_turn(r, c))
                button.grid(row=row, column=column)
                row_buttons.append(button)
            self.buttons[row] = row_buttons

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.current_player

            if self.check_winner():
                self.label.config(text=self.current_player + " Wins!")

                if self.current_player == "X":
                    self.x_wins += 1
                    self.x_wins_label.config(text="X Wins: {}".format(self.x_wins))
                else:
                    self.o_wins += 1
                    self.o_wins_label.config(text="O Wins: {}".format(self.o_wins))

            elif self.empty_spaces():
                self.label.config(text="Tie!")
            else:
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                self.label.config(text=self.current_player + "'s turn")

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.highlight_winner_buttons(row, 0, row, 1, row, 2)
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.highlight_winner_buttons(0, column, 1, column, 2, column)
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.highlight_winner_buttons(0, 0, 1, 1, 2, 2)
            return True

        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.highlight_winner_buttons(0, 2, 1, 1, 2, 0)
            return True

        return False

    def highlight_winner_buttons(self, *coordinates):
        for i in range(0, len(coordinates), 2):
            row, col = coordinates[i], coordinates[i + 1]
            self.buttons[row][col].config(bg="green")

    def empty_spaces(self):
        return all(self.buttons[row][column]['text'] != "" for row in range(3) for column in range(3))

    def new_game(self):
        self.current_player = random.choice(self.players)
        self.label.config(text=self.current_player + "'s turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()