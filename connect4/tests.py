from django.test import TestCase

# Create your tests here.


class GamesTest(TestCase):
    def test_games_are_listed(self):
        self.client.get('/games')
        print(3)
        self.assertTemplateUsed('games.html')
