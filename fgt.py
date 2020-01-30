# Represent several different fighters and pit them against one another in combat. 
# Use random and time to add effect
# The class becomes objects, but how do I access that object and continue to track and use it? The answer: with a global variable
import time
import random

# Warning test environment
# Still having the problem of hit points regenerating.
# The only possibility is somehow the class is getting created each time.
# AttributeError: 'str' object has no attribute 'stamina'

# Global variables go here.
players_fighter = " "
computers_fighter = " "
quit_flag = 0
turn = 0


# Functions go here. 
def random_letter():
	"""Selects a random letter"""
	i = random.choice("A" "B" "C")
	return i

def sleepy_time():
	"""
	Sleeps for 1 second
	Simulates loading
	"""
	time.sleep(1)
	print("...")

def random_number(i):
	"""
	Generates a random number
	Between 1 and the input
	"""
	for x in range(1):
		return (random.randint(1, i))

def select(letter):
	"""
	Selects a fighter based on input
	"""
	global players_fighter	
	if letter == "A":
		players_fighter = Hobo()
	elif letter == "B":
		players_fighter = Gladiator()
	elif letter == "C":
		players_fighter = Elf()
	else:
		print("Please enter a correct choice")
		select(letter)


def computers_move():
	"""
	Selects a frandom fighter.
	"""
	comps_choice = random.choice("P" "K" "W")
	return comps_choice
	
	

def computers_fighter():
	"""
	Selects a frandom fighter.
	"""
	global computers_fighter
	comps_choice = random.choice("A" "B" "C")
	# choose a random class from the list and instantiate it
	if comps_choice == "A":
		computers_fighter = Hobo()
	elif comps_choice == "B":
		computers_fighter = Gladiator()
	elif comps_choice == "C":
		computers_fighter = Elf()

def play_game():
	"""
	Begins the game loop
	"""
	global players_fighter
	
	print("Type A")
	while input != "A" or "B" or "C":
		letter = input("Enter your selection: ")
		if letter == "A":
			players_fighter = Hobo()
			break
		elif letter == "B":
			players_fighter = Gladiator()
			break
		elif letter == "C":
			players_fighter = Elf()
			break
		else:
			print("Incorrect input\nChoices are ")
		

	print("Computer is selecting.")
	print("computer has selected.")
	computers_fighter()
	

def instructions():
	"""
	Allows player to input move
	Calculates move
	"""
	print("Welcome to the Arena. A Product of \'Grimes Golden\' Software\n")
	time.sleep(1)
	print("Every fighter will begin with 100 hit points and 50 stamina.\n")
	print("One use of the \'Special Move\' is unlocked when your fighter is below 50 hitpoints\n")
	print("Your fighter will die if they reach below 100 hit points.\n")
	print("Press P for punch, K for kick, W for weapon (takes 10 stamina), Spacebar to block, S for special move, or Q to quit.")
	time.sleep(1)
	print("Type H at any time to see these instructions again.")


def p1_move():
	"""
	The fight loop for player 1
	For the computers version:
	Make a new function where the input is random
	Run that function at the end of every statement!
	"""
	# Now testing if making classes global effects it, was I using a local variable instead of the global class? Stay tuned to find out
	# Oh boy all these break statements, if things start going wrong, theres your problem. 
	# Okay add a second loop to the bottom. That will be the computers turn. 
	global computers_fighter
	global players_fighter
	global computers_fighter
	global turn
	comp_health = computers_fighter.hitpoints
	players_health = players_fighter.hitpoints
	draw_weapon = 1

	while comp_health and players_health >= 0:
		# I put the globals inside the while loop
		# This could all probably be its own function.
		move = input("Enter your move: ")
		if turn == 1:
			comp_move()
		if turn != 1:
			move = input("Enter your move: ")
		if move == "P":
			x = random_number(15)
			if x > 10:
				time.sleep(1)
				print("...")
				time.sleep(1)
				print("Critical Hit!")
				print("Crit " + computers_fighter.name + " for " + str(x) + " points ")
				comp_health -= x
				print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
				turn += 1
			else:
				print("You punch " + computers_fighter.name + " for " + str(x) + " points ")
				comp_health -= x
				print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
				turn += 1
		elif move == "K":
			x = random_number(15)
			if x > 10:
				print("Critical Hit!")
				print("Crit " + computers_fighter.name + " for " + str(x) + " points ")
				comp_health -= x
				print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
				turn += 1
			else:
				print("You kick " + computers_fighter.name + " for " + str(x) + " points ")
				comp_health -= x
				print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
				turn += 1
		elif move  == "W":
			"""
			Weapon Loop
			"""
			draw_weapon -= 1
			if draw_weapon == 0:
				print("You draw your weapon!, ruthless onslaught unlocked.")
				move == "W"
			if draw_weapon <= 0:
				x = random_number(25)
				if players_fighter.stamina < 10:
					print("You are too exhausted to use your weapon!!")
					turn += 1
				elif x > 20:
					print("A savage crit!")
					print("You crit " + computers_fighter.name + " for " + str(x) + " points ")
					comp_health -= x
					print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
					print("Stamina reduced by 10")
					players_fighter.stamina -= 10
					print(str(players_fighter.stamina) + " stamina left.")
					turn += 1
				else:
					x = random_number(25)
					print("You attack " + computers_fighter.name + " for " + str(x) + " points ")
					comp_health -= x
					print(computers_fighter.name +  " has " + str(comp_health) + " hit points")
					print("Stamina reduced by 10")
					players_fighter.stamina -= 10
					print(str(players_fighter.stamina) + " stamina left.")
					turn += 1
		elif move == "Q":
			print('Bye have a wonderful time')
			quit_flag = 1
		else:
			print("Incorrect Input")
	



def comp_move():
	"""
	The fight loop for computers
	For the computers version:
	Make a new function where the input is random
	Run that function at the end of every statement!
	"""
	global computers_fighter
	global players_fighter
	global quit_flag
	global turn
	move = random_number(3)
	# Now testing if making classes global effects it, was I using a local variable instead of the global class? Stay tuned to find out
	
	players_health = players_fighter.hitpoints
	draw_weapon = 1
	if move == 1:
		x = random_number(15)
		if x > 10:
			sleepy_time()
			print("Critical Hit!")
			print("Computer critically hits " + players_fighter.name + " for " + str(x) + " points ")
			players_health -= x
			sleepy_time()
			print("Player 1 has " + str(players_health) + " hit points")
			print("\n")
			turn -= 1
		else:
			sleepy_time()
			print("Computer punches " + players_fighter.name + " for " + str(x) + " points ")
			sleepy_time()
			players_health -= x
			sleepy_time()
			print("Player 1 has " + str(players_health) + " hit points")
			print("\n")
			turn -= 1
	elif move == 2:
		x = random_number(15)
		if x > 10:
			sleepy_time()
			print("Critical Hit!")
			print("Computer critically hits " + players_fighter.name + " for " + str(x) + " points ")
			players_health -= x
			sleepy_time()
			print("Player 1 has "+ str(players_health) + " hit points")
			turn -= 1
		else:
			sleepy_time()
			print("Computer kicks " + players_fighter.name + " for " + str(x) + " points ")
			players_health -= x
			sleepy_time()
			print("Player 1 has " + str(players_health) + " hit points")
			print("\n")
			turn -= 1
	elif move  == 3:
		if computers_fighter.stamina < 10:
			turn = 0
			"""
			Weapon Loop
			"""
			draw_weapon -= 1
			if draw_weapon == 0:
				sleepy_time()
				print("Computer draws weapon!, god help us.")
			if draw_weapon <= 0:
				x = random_number(25)
				if x > 20:
					print("A savage crit!")
					print("Computer weapon crits Player 1 for " + str(x) + " points ")
					players_health -= x
					sleepy_time()
					print("Player 1 has " + str(players_health) + " hit points")
					print("Stamina reduced by 10")
					computers_fighter.stamina -= 10
					sleepy_time()
					print("Computer has " + str(computers_fighter.stamina) + " stamina left.")
					print("\n")
					turn -= 1
				else:
					sleepy_time()
					x = random_number(25)
					print("Computer attacks " + players_fighter.name + " for " + str(x) + " points ")
					players_health -= x
					sleepy_time()
					print("Player 1 has " + str(players_health) + " hit points")
					print("Stamina reduced by 10")
					computers_fighter.stamina -= 10
					print("Computer has " + str(computers_fighter.stamina) + " stamina left.")
					print("\n")
					turn -= 1
	else:
		print("Incorrect Input")
	# This will also play if I enter quit, hmm that aint good. 
	# This needs to print only when health is below 100


	


# Classes go here.
class Fighter():
	"""
	Base class for all fighters
	"""
	def __init__(self):
		self.hitpoints = 100
		self.stamina = 50
		"""
		Initialize the fighter
		"""
		print("Fighter Ready")
		

	def hits(i):
		"""
		Checks hits and reduces hitpoint
		"""
		self.hits -= i

	def stam(i):
		"""
		Reduces stamina from weapon hit or
		special move.
		"""
		self.stamina -= i

class Hobo(Fighter):
	"""
	Initializes a hobo class
	"""
	def __init__(self):
		"""
		Initializing parent methods
		"""
		super().__init__()
		self.name = "The Hobo"
		print("The Hobo with a Slingshot has entered the fray!")


class Gladiator(Fighter):
	"""
	Initializes a Gladiator class
	"""

	def __init__(self):
		"""
		Initializing parent methods
		"""
		super().__init__()
		self.name = "The Gladiator"
		print("The Gladiator has entered the fray!")
	


class Elf(Fighter):
	"""
	Initializes an Elf class
	"""
	def __init__(self):
		super().__init__()
		self.name ="The Elf"
		print("The Elf has entered the fray!")

# Here I try to keep a loop going as long as the health of both players is above zero
# Trying to keep the fight ongoing without hitpoints resetting
play_game()
p1_move()
print("Game over")
