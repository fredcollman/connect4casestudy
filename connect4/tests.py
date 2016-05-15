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

    def test_games_can_be_available(self):
        game = Game.objects.create(player1=self.alice)
        self.assertIn(game, Game.available_games(self.bob))

    def test_games_in_progress_are_not_available(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        charlie = self._create_user('charlie')
        self.assertNotIn(game, Game.available_games(charlie))

    def test_own_games_are_not_available(self):
        game = Game.objects.create(player1=self.bob)
        self.assertNotIn(game, Game.available_games(self.bob))

    def test_can_view_own_games(self):
        game = Game.objects.create(player1=self.bob)
        self.assertTrue(game.is_viewable_by(self.bob))

    def test_cannot_view_others_games(self):
        game = Game.objects.create(player1=self.bob)
        self.assertFalse(game.is_viewable_by(self.alice))

    def test_player2_can_view(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertTrue(game.is_viewable_by(self.bob))

    def test_player1_is_red(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertEqual('red', game.colour_for(self.alice))

    def test_player2_is_yellow(self):        
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertEqual('yellow', game.colour_for(self.bob))

    def test_player1_goes_first(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertTrue(game.is_turn_of(self.alice))

    def test_player2_cannot_go_first(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        self.assertFalse(game.is_turn_of(self.bob))

    def test_player2_goes_second(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        game.place_counter(self.alice, 0)
        self.assertTrue(game.is_turn_of(self.bob))

    def test_player1_cannot_go_second(self):
        game = Game.objects.create(player1=self.alice, player2=self.bob)
        game.place_counter(self.alice, 0)
        self.assertFalse(game.is_turn_of(self.alice))
