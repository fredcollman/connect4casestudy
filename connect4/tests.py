from django.contrib.auth.models import User
from django.test import TestCase
from connect4.models import Game


class GameTest(TestCase):
    def setUp(self):
        self.alice = self._create_user('alice')
        self.bob = self._create_user('bob')

    def _create_user(self, name):
        return User.objects.create(username=name, first_name=name,
                                   password='qwertyuiop')

    def test_games_for_user_includes_users_games(self):
        game = Game.objects.create(player1=self.bob)
        self.assertIn(game, Game.games_for_user(self.bob))

    def test_games_for_user_excludes_other_users_games(self):
        game = Game.objects.create(player1=self.bob)
        self.assertNotIn(game, Game.games_for_user(self.alice))

    def test_games_for_user_includes_player2(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertIn(game, Game.games_for_user(self.bob))
