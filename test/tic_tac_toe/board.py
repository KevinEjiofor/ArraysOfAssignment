class Board:
    def __init__(self):
        self.cells = [' ' for _ in range(9)]

    def display(self):
        for i in range(0, 9, 3):
            print(f'{self.cells[i]} | {self.cells[i + 1]} | {self.cells[i + 2]}')
            if i < 6:
                print('---------')

    def make_move(self, position, symbol):
        if self.cells[position] == ' ':
            self.cells[position] = symbol
            return True
        return False

    def is_full(self):
        return ' ' not in self.cells

    def check_winner(self, symbol):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for combo in winning_combinations:
            if all(self.cells[i] == symbol for i in combo):
                return True
        return False
