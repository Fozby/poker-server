from flask import Flask
from enum import Enum

app = Flask(__name__)

@app.route('/')
def hello_world():
    state = HandState(p1_stack=20000, p2_stack=20000, big_blind=200, p1_button=True)
    print("{}".format(state))
    """Print 'Hello, world!' as the response body."""
    return 'Hello, blah!'


class HandState:
    board = []
    pot = 0
    p1 = None
    p2 = None
    preflop_actions = []

    def __init__(self, p1_stack, p2_stack, big_blind, p1_button):
        self.pot = 300
        self.p1 = Player(p1_stack, p1_button)
        self.p2 = Player(p2_stack, not p1_button)
        self.preflop_actions.append(Action("p1", ActionType.bet, big_blind/2))
        self.preflop_actions.append(Action("p2", ActionType.bet, big_blind))

    def __str__(self):
        return """
            Board = {}
            Pot = {}
            p1 = {}
            p2 = {}
            preflop_actions = {}
            """.format(self.board, self.pot, self.p1, self.p2, [str(item) for item in self.preflop_actions])

class Player:
    stack = 0
    is_button = False

    def __init__(self, stack, is_button):
        self.stack = stack
        self.is_button = is_button

    def __str__(self):
        return """
            \tStack = {}
            \tis_button = {}
        """.format(self.stack, self.is_button)

class ActionType(Enum):
    fold = 1
    check = 2
    bet = 3

class Action:
    def __init__(self, player, actionType, amount=0):
        self.player = player
        self.actionType = actionType
        self.amount = amount

    def __str__(self):
        return """
            \tActionType = {}
            \tAmount = {}
        """.format(self.actionType, self.amount)

