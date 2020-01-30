# Represent several different fighters and pit them against one another in combat. 
# Use random and time to add effect
# The class becomes objects, but how do I access that object and continue to track and use it? The answer: with a global variable
import time
import random
# Deleting the global variables, to see if the global variable called in the function play_game() will call itself and save to global scope. 
# It could work, if we never keave the function and go to global scope. 


# Functions go here. 
def random_letter():
	"""Selects a random letter"""
	i = random.choice("A" "B" "C")
	return i

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
	# Return the instance	
	return players_fighter

def computers_pick():
	"""
	Selects a random fighter.
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
	# Return instance		
	return computers_fighter

def computers_move():
	"""
	Selects a random move.
	"""
	comps_choice = random.choice("P" "K" "W")

def play_game():
	"""
	Begins the game loop
	"""
	print("Select your fighter:\n")
	print("For Hobo with a Slingshot || enter: A ||\nFor Gladiator || type B ||\nFor the Elf || type C")
	letter = ""
	while letter != "A" or "B" or "C":
		letter = input("Enter your selection: ")
		if letter == "A":
			players_fighter = Hobo()
			print("You have selected " + players_fighter.name + "!")
			break
		elif letter == "B":
			players_fighter = Gladiator()
			print("You have selected " + players_fighter.name + "!")
			break
		elif letter == "C":
			players_fighter = Elf()
			print("You have selected " + players_fighter.name + "!")
			break
		else:
			print("Incorrect input\nChoices are A, B or C: ")

	print("Computer is selecting.")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(1)

	print("Computer has selected.")
	computers_fighter = computers_pick()
	print("Computer selected: " + computers_fighter.name + "!") 
	print("Compiling fighters.")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("You have: " + str(players_fighter.hitpoints) + " hitpoints.")
	print("Computer has: " + str(computers_fighter.hitpoints) + " hitpoints")
	print(players_fighter.hitpoints)
	print(players_fighter.stamina)
	players_fighter.stamina -= 10
	print(" I just changed stamina and now its: ")
	print(players_fighter.stamina)
	return computers_fighter
	return players_fighter
	# If this works here, it returned fighter() instances globally

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

def p1_fight():
	"""
	The fight loop for player 1
	For the computers version:
	Make a new function where the input is random
	Run that function at the end of every statement!
	"""
	global computers_fighter
	global players_fighter
	# Now testing if making classes global effects it, was I using a local variable instead of the global class? Stay tuned to find out
	
	health = computers_fighter.hitpoints
	draw_weapon = 1

	while health > 0:
		# This could all probably be its own function.
		move = input("Enter your move: ")
		if move == "P":
			x = random_number(15)
			if x > 10:
				print("Critical Hit!")
				print("Crit " + computers_fighter.name + " for " + str(x) + " points ")
				health -= x
				print(computers_fighter.name +  " has " + str(health) + " hit points")
				# Now let the computer do some work
			else:
				print("You punch " + computers_fighter.name + " for " + str(x) + " points ")
				health -= x
				print(computers_fighter.name +  " has " + str(health) + " hit points")
		elif move == "K":
			x = random_number(15)
			if x > 10:
				print("Critical Hit!")
				print("Crit " + computers_fighter.name + " for " + str(x) + " points ")
				health -= x
				print(computers_fighter.name +  " has " + str(health) + " hit points")
			else:
				print("You kick " + computers_fighter.name + " for " + str(x) + " points ")
				health -= x
				print(computers_fighter.name +  " has " + str(health) + " hit points")
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
				elif x > 20:
					print("A savage crit!")
					print("You crit " + computers_fighter.name + " for " + str(x) + " points ")
					health -= x
					print(computers_fighter.name +  " has " + str(health) + " hit points")
					print("Stamina reduced by 10")
					players_fighter.stamina -= 10
					print(str(players_fighter.stamina) + " stamina left.")
				else:
					x = random_number(25)
					print("You attack " + computers_fighter.name + " for " + str(x) + " points ")
					health -= x
					print(computers_fighter.name +  " has " + str(health) + " hit points")
					print("Stamina reduced by 10")
					players_fighter.stamina -= 10
					print(str(players_fighter.stamina) + " stamina left.")
		elif move == "Q":
			print('Bye have a wonderful time')
			break
		else:
			print("Incorrect Input")
	# This will also play if I enter quit, hmm that aint good. 
	# This needs to print only when health is below 100
	print("Player 1 Wins!!")


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
		
	


class Elf(Fighter):
	"""
	Initializes an Elf class
	"""
	def __init__(self):
		super().__init__()
		self.name ="The Elf"
		
play_game()
print("Okay that worked fine, now watch it fail")
# It fails here, once the class onject hits global scope again
# can I create it again? And then have it work?
print("If you see 100 hitpoints after this the global object variable was correctly returned.")
print(players_fighter.hitpoints)
