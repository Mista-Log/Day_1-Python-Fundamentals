import random

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.turn = "X"
        self.winner = None

    def display_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print("|", self.board[i], "|", self.board[i + 1], "|", self.board[i + 2], "|")
            print("-------------")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.turn
            self.check_winner()
            if self.winner is None:
                self.switch_turn()
        else:
            print("Invalid move. Please try again.")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                self.winner = self.board[combination[0]]
                break

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_tie(self):
        return " " not in self.board and self.winner is None

    def play_game(self):
        while True:
            self.display_board()
            print(f"Player {self.turn}'s turn.")
            position = int(input("Enter the position (1-9): ")) - 1
            if 0 <= position < 9:
                self.make_move(position)
            else:
                print("Invalid position. Please try again.")

            if self.winner:
                print(f"Player {self.winner} wins!")
                break
            elif self.check_tie():
                print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
