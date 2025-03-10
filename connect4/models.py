from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from connect4.core.board import Board

# Create your models here.


@python_2_unicode_compatible
class Game(models.Model):
    player1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player_1')
    player2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player_2', blank=True, null=True)
    status = models.CharField(max_length=10)
    winner = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.player2:
            return ' vs '.join([self.player1.get_full_name(), self.player2.get_full_name()])

        else:
            return 'Join now to play %s' % self.player1.get_short_name()

    @property
    def start_date(self):
        return self.coin_set.order_by('created_date')[0].created_date

    @property
    def last_move(self):
        return self.coin_set.order_by('-created_date')[0]

    @property
    def last_action_date(self):
        return self.last_move.created_date

    def join_up(self, player_2):
        if self.player2 is None:
            self.player2 = player_2
            self.save()
            return True
        else:
            return False

    def make_move(self, player, row, column):
        try:
            self.coin_set.create(game=self, player=player,
                                 row=row, column=column)
        except:
            return False

        return True

    def place_counter(self, player, column):
        if self.is_turn_of(player):
            return self.make_move(
                player, Coin.number_in_column(self, column), column)

    @classmethod
    def games_for_user(cls, user):
        return cls.objects.filter(player1=user) | \
            cls.objects.filter(player2=user)

    @classmethod
    def available_games(cls, user):
        return cls.objects.exclude(player1=user).filter(player2=None)

    def is_viewable_by(self, user):
        return user in [self.player1, self.player2]

    def is_turn_of(self, user):
        return user == self.whose_turn()

    def whose_turn(self):
        if not self.coin_set.exists():
            return self.player1
        elif self.board.has_winner():
            return None
        elif self.last_move.player == self.player1:
            return self.player2
        else:
            return self.player1

    def colour_for(self, user):
        if user == self.player1:
            return 'red'
        elif user == self.player2:
            return 'yellow'

    @property
    def board(self):
        board = Board()
        for coin in self.coin_set.all():
            board.add(coin)
        return board


@python_2_unicode_compatible
class Coin(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    column = models.IntegerField()
    row = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ' '.join([
            self.player, 'to', self.row, self.column
        ])

    @classmethod
    def number_in_column(cls, game, column):
        return cls.objects.filter(game=game, column=column).count()

    def colour(self):
        return self.game.colour_for(self.player)
