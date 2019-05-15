from itertools import groupby
from collections import Counter
class helper_functions: # Initialize Game
	def __init__(self):
		self.river = []
		self.player_hand = []
		self.active_cards_values = []
		self.active_cards_suits = []
		self.spades = ['1S', '2S', '3S', '4S', '5S', '6S', '7S','8S', '9S', '10S', 'JS', 'QS', 'KS']
		self.clubs = ['1C', '2C', '3C', '4C', '5C', '6C', '7C','8C', '9C', '10C', 'JC', 'QC', 'KC']
		self.diamonds = ['1D', '2D', '3D', '4D', '5D', '6D', '7D','8D', '9D', '10D', 'JD', 'QD', 'KD']
		self.hearts = ['1H', '2H', '3H', '4H', '5H', '6H', '7H','8H', '9H', '10H', 'JH', 'QH', 'KH']
		self.deck = self.spades + self.clubs + self.diamonds + self.hearts

	def update_actives(self):
		for card in self.river:
			self.active_cards_values.append(card[0])
			self.active_cards_suits.append(card[1])
		for card in self.player_hand:
			self.active_cards_values.append(card[0])
			self.active_cards_suits.append(card[1])

	def community_card_entry(self):
		valid_choice = False
		while !valid_choice:
			try:
				player_choice = str(input())
			except ValueError:
				print("Please enter a valid choice")
			else:
				if player_choice not in self.deck:
					print("Please enter a valid choice")
				else:
					self.river.append(player_choice)
					self.deck.remove(player_choice)
					valid_choice = True
			self.update_actives()

	def pre_flop(self):
		while len(self.player_hand) != 2: #Gets player's hand
			print("Enter your hand")
			valid_choice = False
			while !valid_choice:
				try:
					player_choice = str(input())
				except ValueError:
					print("Please enter a valid choice")
				else:
					if player_choice not in self.deck:
						print("Please enter a valid choice")
					else:
						self.player_hand.append(player_choice)
						self.deck.remove(player_choice)
						valid_choice = True
			self.update_actives()

	def flop(self):
		print("Enter the first 3 community cards")
		for i in range(3):
			self.community_card_entry()

	def board_1(self):
		print("Enter the 4th community card")
		self.community_card_entry()

	def board_2(self):
		print("Enter the final community card")
		self.community_card_entry()

	def one_pair(self):
		pairs = 0
		unique_card_values = []
		for card in self.active_cards_values:
			if card not in unique_card_values:
				unique_card_values.append(card)
			else:
				pairs += 1
		if pairs == 1:
			return True
		return False

	def two_pair(self):
		pairs = 0
		unique_card_values = []
		for card in self.active_cards_values:
			if card not in unique_card_values:
				unique_card_values.append(card)
			else:
				pairs += 1
		if pairs > 1:
			return True
		return False

	def trips(self):
		distinct_values = set(self.active_card_values)
		for value in distinct_values:
			count = self.active_card_values.count(value)
			if count == 3:
				return True
		return False

	def quads(self):
		distinct_values = set(self.active_card_values)
		for value in distinct_values:
			count = self.active_card_values.count(value)
			if count == 4:
				return True
		return False

	def straight(self):
		straight = False
		distinct_values = set(self.active_card_values).sort()
		if len(distinct_values) > 4:
			for start_index in range(len(distinct_values) - 4):
				for i in range(start_index, start_index + 4):
					count = 0
					if distinct_values[i+1] - distinct_values[i] == 1:
						count += 1
					if count == 4:
						straight = True
		return straight

	def flush(self):
		distinct_suits = set(self.active_card_suits)
		for suit in distinct_suits:
			count = self.active_card_suits.count(suit)
			if count >= 5:
				return True
		return False

	def full_house(self):
		return (self.trips() and self.one_pair()) or (self.trips() and self.two_pair())

	def one_pair_probability:


	def print_probabilities(self):
		if not self.one_pair():
			print("One Pair: ", self.one_pair_probability())
		if not self.two_pair():
			print("Two Pair: ", self.two_pair_probability())
		if not self.trips():
			print("Trips: ", self.trips_probability())
		if not self.quads():
			print("Quads: ", self.quads_probability())
		if not self.straight():
			print("Straight: ", self.straight_probability())
		if not self.flush():
			print("Flush: ", self.flush_probability())
		if not self.full_house():
			print("Full House: ", self.full_house_probability()) 

	def reset(self):
		self.river = []
		self.player_hand = []
		self.active_cards_values = []
		self.active_cards_suits = []
		self.deck = self.spades + self.clubs + self.diamonds + self.hearts
