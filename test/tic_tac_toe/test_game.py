import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_switch_player(self):
        game = Game("Player1", "Player2")
        self.assertEqual(game.current_player, game.player1)

        game.switch_player()

        self.assertEqual(game.current_player, game.player2)
        game.switch_player()
        self.assertEqual(game.current_player, game.player1)


