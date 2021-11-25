import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("diamond", 8)
        self.card3 = Card("hearts", 4)

        self.cards = [self.card1, self.card2, self.card3]

        self.game = CardGame()


    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))
        self.assertEqual(False, self.game.check_for_ace(self.card2))


    def test_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card2, self.card3))
        self.assertEqual(self.card3, self.game.highest_card(self.card1, self.card3))


    def test_cards_total(self):
        self.assertEqual("You have a total of13", self.game.cards_total(self.cards))
