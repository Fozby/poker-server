import unittest

from deck import Deck, Card, CardValue, CardSuit
from hand_utils import isStraightFlush, sortCards, isQuads, isFullHouse,  createCountDict, isFlush, isStraight,isTrips, isTwoPair, isHighCard

class TestHandUtils(unittest.TestCase):

    def test_straight_flush(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Deuce, CardSuit.Club),
                Card(CardValue.Three, CardSuit.Heart),
                Card(CardValue.Four, CardSuit.Club),
                Card(CardValue.Five, CardSuit.Club)
                ]
        wheel_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Deuce, CardSuit.Club),
                Card(CardValue.Three, CardSuit.Club),
                Card(CardValue.Four, CardSuit.Club),
                Card(CardValue.Five, CardSuit.Club)
                ]

        royal_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.King, CardSuit.Club),
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.Jack, CardSuit.Club),
                Card(CardValue.Ten, CardSuit.Club)
                ]

        second_nut_set = [
                Card(CardValue.Nine, CardSuit.Club),
                Card(CardValue.King, CardSuit.Club),
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.Jack, CardSuit.Club),
                Card(CardValue.Ten, CardSuit.Club)
                ]

        invalid_result = isStraightFlush(sortCards(invalid_set))
        self.assertEqual(invalid_result, -1)

        royal = isStraightFlush(sortCards(royal_set))
        wheel_flush = isStraightFlush(sortCards(wheel_set))
        second_nut_flush = isStraightFlush(sortCards(second_nut_set))

        self.assertGreater(second_nut_flush, wheel_flush)
        self.assertGreater(royal, second_nut_flush)

    def test_straight(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Deuce, CardSuit.Club),
                Card(CardValue.Three, CardSuit.Heart),
                Card(CardValue.Four, CardSuit.Club),
                Card(CardValue.Six, CardSuit.Club)
                ]
        wheel_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Deuce, CardSuit.Club),
                Card(CardValue.Three, CardSuit.Club),
                Card(CardValue.Four, CardSuit.Club),
                Card(CardValue.Five, CardSuit.Club)
                ]

        royal_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.King, CardSuit.Club),
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.Jack, CardSuit.Club),
                Card(CardValue.Ten, CardSuit.Club)
                ]

        second_nut_set = [
                Card(CardValue.Nine, CardSuit.Club),
                Card(CardValue.King, CardSuit.Club),
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.Jack, CardSuit.Club),
                Card(CardValue.Ten, CardSuit.Club)
                ]

        invalid_result = isStraight(sortCards(invalid_set))
        self.assertEqual(invalid_result, -1)

        royal = isStraight(sortCards(royal_set))
        wheel_flush = isStraight(sortCards(wheel_set))
        second_nut_flush = isStraight(sortCards(second_nut_set))

        self.assertGreater(second_nut_flush, wheel_flush)
        self.assertGreater(royal, second_nut_flush)

    def test_quads(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.Five, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.Ace, CardSuit.Diamond),
                Card(CardValue.Five, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.Ace, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]
        valid_set_result = isQuads(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isQuads(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isQuads(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)

    def test_full_house(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.Five, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.Five, CardSuit.Diamond),
                Card(CardValue.Five, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]
        valid_set_result = isFullHouse(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isFullHouse(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isFullHouse(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)

    def test_flush(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.Five, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.King, CardSuit.Club),
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.Jack, CardSuit.Club),
                Card(CardValue.Ten, CardSuit.Club),
                Card(CardValue.Eight, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Deuce, CardSuit.Club),
                Card(CardValue.Three, CardSuit.Club),
                Card(CardValue.Four, CardSuit.Club),
                Card(CardValue.Five, CardSuit.Club)
                ]
        valid_set_result = isFlush(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isFlush(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isFlush(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)

    def test_trips(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.Queen, CardSuit.Diamond),
                Card(CardValue.Jack, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.Deuce, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]
        valid_set_result = isTrips(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isTrips(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isTrips(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)

    def test_two_pair(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Deuce, CardSuit.Heart),
                Card(CardValue.Deuce, CardSuit.Diamond),
                Card(CardValue.Jack, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Deuce, CardSuit.Heart),
                Card(CardValue.Deuce, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]
        valid_set_result = isTwoPair(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isTwoPair(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isTwoPair(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)

    def test_high_card(self):
        invalid_set = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.Ace, CardSuit.Spade),
                Card(CardValue.Ace, CardSuit.Heart),
                Card(CardValue.King, CardSuit.Diamond),
                Card(CardValue.King, CardSuit.Club)
                ]

        valid_set = [
                Card(CardValue.Queen, CardSuit.Club),
                Card(CardValue.King, CardSuit.Spade),
                Card(CardValue.Deuce, CardSuit.Heart),
                Card(CardValue.Three, CardSuit.Diamond),
                Card(CardValue.Ten, CardSuit.Club)
                ]

        valid_set_nuts = [
                Card(CardValue.Ace, CardSuit.Club),
                Card(CardValue.King, CardSuit.Spade),
                Card(CardValue.Deuce, CardSuit.Heart),
                Card(CardValue.Three, CardSuit.Diamond),
                Card(CardValue.Ten, CardSuit.Club)
                ]
        valid_set_result = isHighCard(sortCards(valid_set))

        self.assertGreater(valid_set_result, 0)

        invalid_result = isHighCard(sortCards(invalid_set))

        self.assertEqual(invalid_result, -1)


        valid_set_nuts_result = isHighCard(sortCards(valid_set_nuts))


        self.assertGreater(valid_set_nuts_result, valid_set_result)


if __name__ == '__main__':
    unittest.main()
