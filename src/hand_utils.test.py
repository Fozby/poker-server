import unittest

from deck import Deck, Card, CardValue, CardSuit
from hand_utils import isStraightFlush, sortCards

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

        invalid_result = isStraightFlush(invalid_set)
        self.assertEqual(invalid_result, -1)

        royal = isStraightFlush(sortCards(royal_set))
        wheel_flush = isStraightFlush(sortCards(wheel_set))
        second_nut_flush = isStraightFlush(sortCards(second_nut_set))

        self.assertGreater(second_nut_flush, wheel_flush)
        self.assertGreater(royal, second_nut_flush)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
