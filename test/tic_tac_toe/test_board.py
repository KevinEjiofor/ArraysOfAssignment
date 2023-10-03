import unittest

from test.tic_tac_toe.board import Board
class TestBoard(unittest.TestCase):
    def test_initial_board(self):
        board = Board()
        self.assertEqual(board.cells, [' '] * 9)

    def test_make_move_valid(self):
        board = Board()
        self.assertTrue(board.make_move(0, 'X'))
        self.assertEqual(board.cells[0], 'X')

    def test_make_move_invalid(self):
        board = Board()
        board.make_move(0, 'X')
        self.assertFalse(board.make_move(0, 'O'))

    def test_is_full_empty(self):
        board = Board()
        self.assertFalse(board.is_full())

    def test_is_full_full(self):
        board = Board()
        for i in range(9):
            board.make_move(i, 'X')
        self.assertTrue(board.is_full())

    def test_check_winner_horizontal(self):
        board = Board()
        for i in range(0, 3):
            board.make_move(i, 'X')
        self.assertTrue(board.check_winner('X'))


