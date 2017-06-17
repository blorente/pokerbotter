import random

suits = ['c', 'h', 's', 'd']
values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

class Deck:
    """A python representation of a deck"""
    def __init__(self):
        self.resetDeck()
        self.shuffle()

    def resetDeck(self):
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append((value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, numCards):
        dealt = []
        for i in range(0, numCards):
            dealt.append(self.cards.pop())
        return dealt
