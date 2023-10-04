import re

from game import Game
from test.bankApp.exception import CustomerException


def run():
    play()


def play():
    try:
        player1_name = str(input("Enter name for Player 1: "))
        validate_name_input(player1_name)

        player2_name = str(input("Enter name for Player 2: "))
        validate_name_input(player2_name)

        game = Game(player1_name, player2_name)
        game.play()

    except CustomerException as error:
        print(str(error))
        play()


def validate_name_input(user_name):
    pattern = r"^\D*$"
    if not re.fullmatch(pattern, user_name):
        raise CustomerException("Invalid entry")


if __name__ == "__main__":
    run()
