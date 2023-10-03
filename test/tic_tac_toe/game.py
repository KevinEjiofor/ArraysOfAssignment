from board import Board
from player import Player
from test.bankApp.exception import CustomerException


class Game:
    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        while True:
            self.board.display()

            position = get_valid_integer_input(f"{self.current_player.name}'s turn ({self.current_player.symbol}): ")

            if not (1 <= position <= 9):
                print("Invalid position. Choose a number between 1 and 9.")
                continue

            if self.board.make_move(position - 1, self.current_player.symbol):
                if self.board.check_winner(self.current_player.symbol):
                    self.board.display()
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("Position already occupied. Try again.")


def get_valid_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")