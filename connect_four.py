#connect 4 game for 2 players (red & yellow)

#game board 7x6 grid

# print "|___|___|___|___|___|___|___| \n" * 6,\
# "  1   2   3   4   5   6   7 \n",\
#  "         CONNECT FOUR         "

while(True):
	start_game = raw_input("Would you like to initialize a game of Connect Four? Y/N: ").lower()
	if start_game == "y":
		print "Starting Game!"
		turn_1 = raw_input("Red Player, select a row to insert a checker.")
	elif start_game == "n":
		print "Quitting Game!"
		break
	else:
		print "Please reply with 'Y' for yes or 'N' for no. "
