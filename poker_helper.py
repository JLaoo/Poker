from helper_functions import *
game = helper_functions()
play = True
while play:
	game.pre_flop()



	print("Continue? (Y/N)") #Continue?
	valid_choice = False
	while !valid_choice:
		try:
			player_choice = str(input())
		except ValueError:
			print("Please enter a valid choice")
		else:
			if player_choice == "N":
				play = False
				valid_choice = True
				print("Good choice")
			elif player_choice == "Y":
				print("Get ready to lose more money...")
				valid_choice = True
			else:
				print("Please enter a valid choice")
	game.reset()