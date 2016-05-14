from unittest import TestCase
from connect4.core.board import Board
from itertools import groupby


class FakeCoin:
    def __init__(self, column, row, player):
        self.column = column
        self.row = row
        self.player = player

ALICE = 0
BOB = 1


class BoardTest(TestCase):
    def test_cannot_add_duplicate_coin(self):
        board = Board()
        coin = FakeCoin(0, 0, ALICE)
        board.add(coin)
        with self.assertRaises(ValueError):
            board.add(coin)

    def test_bounded_width(self):
        board = Board()
        with self.assertRaises(IndexError):
            board.add(FakeCoin(Board.WIDTH, 0, 0))

    def test_bounded_height(self):
        board = Board()
        with self.assertRaises(IndexError):
            board.add(FakeCoin(Board.WIDTH, 0, 0))

    def test_can_win_horizontally(self):
        board = Board()
        for column in range(3):
            board.add(FakeCoin(column, 0, ALICE))
        self.assertFalse(board.has_winner())
        board.add(FakeCoin(3, 0, ALICE))
        self.assertTrue(board.has_winner())

    def test_checks_players(self):
        board = Board()
        for column in range(3):
            board.add(FakeCoin(column, 0, ALICE))
        board.add(FakeCoin(3, 0, BOB))
        self.assertFalse(board.has_winner())

    def test_can_win_vertically(self):
        board = Board()
        for row in range(3):
            board.add(FakeCoin(0, row, ALICE))
        self.assertFalse(board.has_winner())
        board.add(FakeCoin(0, 3, ALICE))
        self.assertTrue(board.has_winner())

    def test_group_of_small_size(self):
        coin = FakeCoin(0, 0, ALICE)
        self.assertFalse(Board.is_winning_sequence([coin] * 3))

    def test_group_of_right_size(self):
        coin = FakeCoin(0, 0, ALICE)
        self.assertTrue(Board.is_winning_sequence([coin] * 4))

    def test_invalid_larger_group(self):
        a = FakeCoin(0, 0, ALICE)
        b = FakeCoin(0, 0, BOB)
        self.assertFalse(Board.is_winning_sequence([a, a, a, b, a, a, a]))

    def test_valid_larger_group(self):
        a = FakeCoin(0, 0, ALICE)
        b = FakeCoin(0, 0, BOB)
        self.assertTrue(Board.is_winning_sequence([a, a, a, b, b, b, b, a]))
