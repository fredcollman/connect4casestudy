from itertools import groupby


SIZE_TO_WIN = 4


class Board:
    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.coins = [[None] * Board.WIDTH for _ in range(Board.HEIGHT)]

    def add(self, coin):
        current_coin = self._get(coin.column, coin.row)
        if current_coin is None:
            self._set(coin)
        else:
            raise ValueError('position already filled')

    def _set(self, coin):
        self.coins[coin.row][coin.column] = coin

    def _get(self, column, row):
        return self.coins[row][column]

    @staticmethod
    def is_winning_sequence(seq):
        grouped_by_player = groupby(seq, Board._extract_player)
        return _has_group_of_size_at_least(SIZE_TO_WIN, grouped_by_player)

    @staticmethod
    def _extract_player(coin):
        return coin.player if coin else None

    def has_winner(self):
        return any(
            self.is_winning_sequence(row) for row in self.rows()
        ) or any(
            self.is_winning_sequence(col) for col in self.columns()
        )

    def rows(self):
        return reversed(self.coins)

    def columns(self):
        for col in range(Board.WIDTH):
            yield [self._get(col, row) for row in range(Board.HEIGHT)]

    def __str__(self):
        return repr(self.coins)


def _has_group_of_size_at_least(num, groups):
    for key, group in groups:
        if key is not None and len(list(group)) >= num:
            return True
    return False
