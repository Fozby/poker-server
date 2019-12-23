from deck import Deck, CardValue, CardSuit, Card, HandRankings
import math

# -1 0 1
def computeWinner():
    deck = Deck()
    print(deck)
    pass


# Returns a score associated with the hand type
def isStraightFlush(sortedCards):
    sortedCards = swapPotentialStraightAce(sortedCards)

    initialValue = sortedCards[0].value
    desired_suit = sortedCards[0].suit
    straight_flush_value = initialValue
    for card in sortedCards[1:]:
        if card.value != initialValue + 1 or card.suit != desired_suit:
            return -1

        initialValue += 1
        straight_flush_value += card.value

    return straight_flush_value

def isQuads(sortedCards):
    countDict = createCountDict(sortedCards)
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

def isFullHouse(sortedCards):
    countDict = createCountDict(sortedCards)
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
    desired_suit = sortedCards[0].suit
    flush_value = computeValue(sortedCards[0])
    for card in sortedCards[1:]:
        if card.suit != desired_suit:
            return -1

        flush_value += computeValue(card)
    return flush_value

def isStraight(sortedCards):
    sortedCards = swapPotentialStraightAce(sortedCards)

    initialValue = sortedCards[0].value
    straight_value = initialValue
    for card in sortedCards[1:]:
        if card.value != initialValue + 1:
            return -1

        initialValue += 1
        straight_value += card.value

    return straight_value

def isTrips(sortedCards):
    countDict = createCountDict(sortedCards)
    if (len(countDict) is not 3):
        return -1

    keys = list(countDict.keys())

    trips = []
    kickers = []
    for key in keys:
        if countDict[key] == 3:
            trips.append(key)
        else:
            kickers.append(key)

    if len(trips) is not 1 or len(kickers) is not 2:
        return -1

    trips_value = 0
    for kicker in kickers:
        trips_value += computeValue(kicker)

    return trips_value + 15 ** trips[0].value


def isTwoPair(sortedCards):
    countDict = createCountDict(sortedCards)
    if (len(countDict) is not 3):
        return -1

    keys = list(countDict.keys())

    pairs = []
    kicker = 0
    for key in keys:
        if countDict[key] == 2:
            pairs.append(key)
        else:
            kicker = key.value

    if len(pairs) is not 2:
        return -1

    two_pair_value = 0
    for pair in pairs:
        two_pair_value += computeValue(pair)

    return two_pair_value + kicker

def isPair(sortedCards):
    countDict = createCountDict(sortedCards)
    if (len(countDict) is not 4):
        return -1

    keys = list(countDict.keys())

    pair = 0
    kickers = []

    for key in keys:
        if countDict[key] == 2:
            pair = key.value
        else:
            kickers.append(key)

    kicker_value = 0
    for kicker in kickers:
        kicker_value += computeValue(kicker)

    return kicker_value + pair

def isHighCard(sortedCards):
    countDict = createCountDict(sortedCards)
    if (len(countDict) is not 5):
        return -1

    high_card_value = 0
    for card in sortedCards:
        high_card_value += computeValue(card)

    return high_card_value

def createCountDict(sortedCards):
    countDict = {}

    for card in sortedCards:
        if card.value not in countDict:
            countDict[card.value] = 1
        else:
            countDict[card.value] += 1

    return countDict

def swapPotentialStraightAce(sortedCards):

    if sortedCards[4].value is CardValue.Ace and sortedCards[3].value is CardValue.Four:
        newSet = [Card.Low_ace]
        newSet[1:] = sortedCards[0:4]
        return newSet
    return sortedCards

def computeValue(card):
    return 2 ** card.value

# Takes in 5 card hand as input
def determineBestHand(playableCards):

    values = sorted([c.value for c in playableCards])
    suits = [c.suit for c in playableCards]

    print(values)
    print(suits)

    pass

def sortCards(cards):
    return sorted(cards, key=lambda x: x.value)

def computeCardValue(cards):

    sortedCards = sortCards(cards)

    handRanks = [
            (HandRankings.Straight_flush, isStraightFlush),
            (HandRankings.Quads, isQuads),
            (HandRankings.Full_house, isFullHouse),
            (HandRankings.Flush, isFlush),
            (HandRankings.Straight, isStraight),
            (HandRankings.Trips, isTrips),
            (HandRankings.Two_pair, isTwoPair),
            (HandRankings.Pair, isPair),
            (HandRankings.High_card, isHighCard)
            ]

    for tuple in handRanks:
        value = tuple[1](sortedCards)

        if value > -1:
            return (tuple[0], value)

    raise Exception

if __name__ == '__main__':
    computeWinner()

    flush_board = []

    straight_board = [
            Card(CardValue.King, CardSuit.Club),
            Card(CardValue.King, CardSuit.Heart),
            Card(CardValue.King, CardSuit.Diamond),
            Card(CardValue.Ace, CardSuit.Spade),
            Card(CardValue.Ace, CardSuit.Spade),
            ]
    print(computeCardValue(straight_board))
    pass
