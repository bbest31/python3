from random import shuffle
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = [Card(suit, value) for suit in suits for value in values]

    def count(self):
        return len(self.deck)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif num >= self.count():
            cards = self.deck.copy()
            return cards
        else:
           cards = self.deck[-num:]
           self.deck = self.deck[:-num]
           return cards
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.deck)
        return self
            

    
