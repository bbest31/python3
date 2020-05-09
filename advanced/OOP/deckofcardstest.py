from advanced.OOP.deckofcards import Card
from advanced.OOP.deckofcards import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", "A")

    def test_init(self):
        """card should have a suit and a value"""
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value,"A")

class DeckTests(unittest.TestCase):
    def setUp(self):
        pass
    # ...
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()