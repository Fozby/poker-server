from deck import Deck, CardValue, CardSuit, Card



def computeWinner():
    deck = Deck()
    print(deck)
    pass


# Returns a score associated with the hand type
def isStraightFlush(sortedCards):
    initialValue = sortedCards[0].value
    desired_suit = sortedCards[0].suit
    straight_flush_value = initialValue
    for card in sortedCards[1:]:
        if card.value != initialValue + 1 or card.suit != desired_suit:
            return -1

        initialValue += 1
        straight_flush_value += card.value
    return straight_flush_value

def isFlush(sortedCards):
    pass

# Takes in 5 card hand as input
def determineBestHand(playableCards):

    values = sorted([c.value for c in playableCards])
    suits = [c.suit for c in playableCards]

    print(values)
    print(suits)

    pass


if __name__ == '__main__':
    computeWinner()

    flush_board = []

    straight_board = [
            Card(CardValue.Ace, CardSuit.Club),
            Card(CardValue.King, CardSuit.Heart),
            Card(CardValue.Queen, CardSuit.Diamond),
            Card(CardValue.Jack, CardSuit.Spade),
            Card(CardValue.Ten, CardSuit.Spade),
            ]
    determineBestHand(straight_board)
    pass
