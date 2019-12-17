from enum import Enum

class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class CardValue(OrderedEnum):
    Ace = 1
    Deuce = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class CardSuit(Enum):
    Club = 1
    Heart = 2
    Diamond = 3
    Spade = 4

class HandRankings(OrderedEnum):
    High_card = 1
    Pair = 2
    Two_pair = 3
    Trips = 4
    Straight = 5
    Flush = 6
    Full_house = 7
    Quads = 8
    Straight_flush = 9

class Card(tuple):

    def __new__(cls, value, suit):
        assert isinstance(value, CardValue)
        assert isinstance(suit, CardSuit)
        return tuple.__new__(cls, (value, suit))

    @property
    def value(self):
        return self[0]

    @property
    def suit(self):
        return self[1]

    def __str__(self):
        return "{} of {}s".format(self.value.name, self.suit.name)

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError

class Deck:
    def __init__(self):
        self.cards = {
            Card(value, suit) for value in CardValue for suit in CardSuit
        }
