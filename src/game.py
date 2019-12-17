from enum import Enum
import random

class Game:
	self.id = None
	self.hand_state = None
	self.player_one = None
	self.player_two = None
	self.button = None

	def __init__(self):
		random.seed()
		self.id = random.randint(1,100)

	# Create and return a new player id
	# Set either player_one or player_two variable
	def register_player(self):
		player_id = random.randint(1000,9999)

		if self.player_one == None:
			player_one = player_id
		else
			player_two = player_id

		return player_id

	# Assign button and start first hand
	def start_game(self):
		self.button = player_one
		self.start_hand(button)
		return

	# Refresh hand state and pay blinds
	def start_hand(self, button):
		sb = button
		bb = player_one + player_two - sb

		self.hand_state = HandState(p1_stack=20000, p2_stack=20000, p1_button=player_one==button)

		self.handle_action(Action(sb, ActionType.bet, 100))
		self.handle_action(Action(bb, ActionType.bet, 200))
		return

	# Determine winner and payout (todo)
	# Switch button
	# Start next hand
	def end_hand(self):
		if player_one == button:
			button = player_two
		else
			button = player_one

		self.start_hand(button)
		return

	# Validate action
	# Update hand state (todo)
	# Possibly end hand (todo)
	def handle_action(self, action):
		print("Handling action {}", action)
		if self.hand_state.street == Street.preflop:
			self.hand_state.preflop_actions.append(action)

		return


	#
	def validate_action(self, action):
		print("Validating action {}", action)
		return

class Players(Enum):
	one = 1
	two = 2

class Street(Enum):
	preflop = 1
	flop = 2
	turn = 3
	river = 4

class HandState:
    self.board = []
    self.pot = 0
    self.p1 = None
    self.p2 = None
    self.preflop_actions = []

    def __init__(self, p1_stack, p2_stack, p1_button):
        self.pot = 300
        self.p1 = Player(p1_stack, p1_button)
        self.p2 = Player(p2_stack, not p1_button)
        self.street = Street.preflop

    def __str__(self):
        return """
            Board = {}
            Street = {}
            Pot = {}
            p1 = {}
            p2 = {}
            preflop_actions = {}
            """.format(self.board, self.street, self.pot, self.p1, self.p2, [str(item) for item in self.preflop_actions])

class Player:
    self.stack = 0
    self.is_button = False

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
