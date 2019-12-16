from .player import Player
from .action import Action, ActionType

class Hand:
    self.board = []
    self.pot = 0
    self.players = []
    self.street = None
    self.preflop_actions = []
    self.bb_value = 0

    # Assume players are ordered from SB to BTN
    def __init__(self, players, bb_value):
        self.street = Street.preflop
        self.players = players
        self.bb_value = bb_value

    def start_hand(self):
        self.handle_action(Action(self.players[0].id, ActionType.bet, bb_value / 2))
        self.handle_action(Action(self.players[1].id, ActionType.bet, bb_value))
        return

    def get_actions(self, player_id):
        return []

    def handle_action(self, action):
        # todo validate
        # todo sometimes deal next street
        # todo handle showdown and return winner(s)
        return

# for explicit
class Street(Enum):
    preflop = 1
    flop = 2
    turn = 3
    river = 4
