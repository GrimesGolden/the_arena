# Classes go here.
import random
import time
from functions import computers_pick
# Functions

def random_number(i):
	"""
	Generates a random number
	Between 1 and the input
	"""
	for x in range(1):
		return (random.randint(1, i))

def computers_pick():
	"""Randomly selects the computers fighter"""
	x = random_number(3)
	if x == 1:
		computer = Hobo()
	elif x == 2:
		computer = Gladiator()
	elif x == 3:
		computer = Elf()
	return computer

def players_pick():
	"""
	Selects the players fighter
	"""
	print("Select your fighter:\n")
	print("For Hobo with a Slingshot || enter: A ||\nFor Gladiator || type B ||\nFor the Elf || type C")
	letter = ""
	while letter != "A" or "B" or "C":
		letter = input("Enter your selection: ")
		if letter == "A":
			player = Hobo()
			break
		elif letter == "B":
			player = Gladiator()
			break
		elif letter == "C":
			player = Elf()
			break
		else:
			print("Incorrect input\nChoices are A, B or C: ")
	return player

def instructions():
	"""
	Prints instructions
	"""
	print("Welcome to the Arena. A Product of \'Grimes Golden\' Software\n")
	time.sleep(1)
	print("Every fighter will begin with 100 hit points and 50 stamina.\n")
	print("One use of the \'Special Move\' is unlocked when your fighter is below 50 hitpoints\n")
	print("Your fighter will die if they reach 0 hit points.\n")
	print("Press P for punch, K for kick, W for weapon (takes 10 stamina), Spacebar to block, S for special move, or Q to quit.")
	time.sleep(1)
	print("Type H at any time to see these instructions again.\n")

def intro():
	"""
	Prints an intro
	"""
	print("Computer is selecting.")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(1)
	computer = computers_pick()
	print("Computer selected: " + computer.name + "!") 
	print("Compiling fighters.")
	time.sleep(1)
	print("...")
	time.sleep(1)
	return computer


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
		print("Fighter Initialized")
		

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


class Game:
	"""
	A class that begins the game loop
	"""
	def __init__ (self):
		instructions()
		self.player = players_pick()
		self.computer = intro()
		


# Game recognize game
game = Game()
print("It worked if hitpoints print below, congrats and github upload")
print(game.computer.hitpoints)
print(game.player.hitpoints)