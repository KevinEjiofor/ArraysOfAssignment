from game import Game

if __name__ == "__main__":
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")

    game = Game(player1_name, player2_name)
    game.play()
