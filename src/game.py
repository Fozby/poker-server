import random

from enum import Enum
from .player import Player
from .hand import Hand
from .action import Action, ActionType

STARTING_STACK = 20000
BB_VALUE = 200

class Game:
	self.id = None
	self.current_hand = None
	self.players = []
	self.button = None

	def __init__(self):
		random.seed()
		self.id = random.randint(1,999)

	# Create and return a new player id
	# Set either player_one or player_two variable
	def register_player(self):
		# Only headsup degens allowed
		if len(player_ids) >= 2:
			return

		player_id = random.randint(1000,9999)
		self.players.append(Player(player_id, STARTING_STACK))

		return player_id

	# Assign button and start first hand
	def start_game(self):
		# Todo randomize first button
		# Todo order list from sb -> btn
		self.current_hand = Hand(players, BB_VALUE)
		return

	def handle_action(self, action):
		# Todo handle hand ending, payout and next hand
		self.current_hand.handle_action(action)

		return


