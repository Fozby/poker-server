class ActionType(Enum):
    fold = 1
    check = 2
    bet = 3

class Action:
    def __init__(self, player_id, type, amount=0):
        self.player_id = player_id
        self.type = type
        self.amount = amount

    def __str__(self):
        return """
            \tplayer_id = {}
            \taction_type = {}
            \tamount = {}
            """.format(self.player_id, self.action_type, self.amount)
