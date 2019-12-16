from .player import Player
from .action import Action, ActionType

class Hand:
    self.board = []
    self.pot = 0
    self.players = []
    self.street = None
    self.preflop_actions = []
    self.bb_value = 0

    # Players who still need to act in the hand, in order
    self.pending_player_ids = []

    # Assume players are ordered from SB to BTN
    def __init__(self, players, bb_value):
        self.street = Street.preflop
        self.players = players
        self.bb_value = bb_value

    def start_hand(self):
        self.handle_action(Action(self.players[0].id, ActionType.bet, bb_value / 2))
        self.handle_action(Action(self.players[1].id, ActionType.bet, bb_value))

        # We need SB to act, then BB
        for player in players:
            pending_player_ids.append(player.id)

        return

    def get_actions(self, player_id):
        return []

    def handle_action(self, action):
        self.pending_player_ids.pop(0)
        # todo validate
        # todo sometimes deal next street
        # todo handle showdown and return winner(s)

        if action.type == ActionType.fold:
            # assume hand over because only headsup
            return

        # Check if last player to act on street
        if len(self.pending_player_ids) == 0:
            self.next_street()
            return

        # If action is a bet, we need to reset pending_player_ids

        if self.street == Street.preflop:
            self.preflop_actions.append(action)
        return

    def next_street(self):
        # deal next card, reset pending player ids
        return

# for explicit
class Street(Enum):
    preflop = 1
    flop = 2
    turn = 3
    river = 4
