from deck import Deck, CardValue, CardSuit, Card

def computeWinner():
    deck = Deck()
    print(deck)
    pass


# Returns a score associated with the hand type
def isStraightFlush(sortedCards):
    # Check for potential royal and swap sorted position
    if sortedCards[0].value is CardValue.Ace and sortedCards[1].value is CardValue.Ten:
        tmp = sortedCards[0]
        sortedCards = sortedCards[1:]
        sortedCards.append(Card(CardValue.High_ace, tmp.suit))

    initialValue = sortedCards[0].value
    desired_suit = sortedCards[0].suit
    straight_flush_value = initialValue
    for card in sortedCards[1:]:
        if card.value != initialValue + 1 or card.suit != desired_suit:
            return -1

        initialValue += 1
        straight_flush_value += card.value

    return straight_flush_value

def createCountDict(sortedCards):
    countDict = {}

    for card in sortedCards:
        if card.value not in countDict:
            countDict[card.value] = 1
        else:
            countDict[card.value] += 1

    return countDict

def isQuads(sortedCards, countDict):
    if (len(countDict) is not 2):
        return -1

    keys = list(countDict.keys())
    # only need to check for the complement
    if not countDict[keys[0]] == 1 and not countDict[keys[1]] == 1:
        return -1

    if countDict[keys[0]] == 1:
        quad_value = keys[0].value
        kicker = keys[1].value
    else:
        quad_value = keys[1].value
        kicker = keys[0].value

    return 100 * quad_value + kicker

def isFullHouse(sortedCards, countDict):
    if (len(countDict) is not 2):
        return -1

    keys = list(countDict.keys())

    # only need to check for the complement
    if not countDict[keys[0]] == 2 and not countDict[keys[1]] == 2:
        return -1
    if countDict[keys[0]] == 3:
        boat_value = keys[0].value
        kicker = keys[1].value
    else:
        boat_value = keys[1].value
        kicker = keys[0].value

    return 100 * boat_value + kicker

def isFlush(sortedCards):
    pass

def isStraight(sortedCards):
    pass

def isTwoPair(sortedCards):
    pass

def isHighCard(sortedCards):
    pass

# Takes in 5 card hand as input
def determineBestHand(playableCards):

    values = sorted([c.value for c in playableCards])
    suits = [c.suit for c in playableCards]

    print(values)
    print(suits)

    pass

def sortCards(cards):
    return sorted(cards, key=lambda x: x.value)

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
