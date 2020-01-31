# Classes go here.
import random
import time
from functions import computers_pick
# Functions
# Removed super() init

def random_number(i):
	"""
	Generates a random number
	Between 1 and the input
	"""
	for x in range(1):
		return (random.randint(1, i))

def sleepy_time():
	"""
	Sleeps for 1 second
	Simulates loading
	"""
	time.sleep(1)
	print("...")


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
		"""
		Initialize the fighter
		"""
		self.hitpoints = 100
		self.stamina = 50
		print("Fighter Initialized")
		
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
		"""
		Select fighters and run intro
		"""
		instructions()
		self.player = players_pick()
		self.computer = intro()
		welcome = "Player One picked " + self.player.name + "\nComputer picked " + self.computer.name
		print(welcome)

	def fight(self):
		i = input("Press any key to begin!\nOr Q to exit.")
		if i == 'Q':
			print("Goodbye!")
		else:
			comp_health = self.computer.hitpoints
			player_health = self.player.hitpoints
			player_stamina = self.player.stamina
			draw_weapon = 1
			while comp_health >= 0 and player_health >= 0:
				move = input("Enter your move: ")
				if move == "P":
					x = random_number(15)
					if x > 10:
						time.sleep(1)
						print("...")
						time.sleep(1)
						print("Critical Hit!")
						print("You crit Computer for " + str(x) + " points ")
						comp_health -= x
						print("Computer has " + str(comp_health) + " hit points")
					else:
						print("You punch Computer for " + str(x) + " points ")
						comp_health -= x
						print("Computer has " + str(comp_health) + " hit points")
				elif move == "K":
					x = random_number(15)
					if x > 10:
						print("Critical Hit!")
						print("You crit Computer for " + str(x) + " points ")
						comp_health -= x
						print("Computer has " + str(comp_health) + " hit points")
					else:
						print("You kick Computer for " + str(x) + " points ")
						comp_health -= x
						print("Computer has " + str(comp_health) + " hit points")
				elif move  == "W":
					"""
					Weapon Loop
					"""
					draw_weapon -= 1
					if draw_weapon == 0:
						print("You draw your weapon!, ruthless onslaught unlocked.")
					if draw_weapon <= 0:
						x = random_number(25)
						if player_stamina < 10:
							print("You are too exhausted to use your weapon!!")
						elif x > 20:
							print("A savage crit!")
							print("You crit Computer for " + str(x) + " points ")
							comp_health -= x
							print("Computer has " + str(comp_health) + " hit points")
							print("Your stamina reduced by 10")
							player_stamina -= 10
							print(str(player_stamina) + " stamina left.")
						else:
							print("You attack Computer for " + str(x) + " points ")
							comp_health -= x
							print("Computer has " + str(comp_health) + " hit points")
							print("Your stamina reduced by 10")
							player_stamina -= 10
							print(str(player_stamina) + " stamina left.")
				elif move == "Q":
					instruction()
				elif move == "Q":
					print('Bye have a wonderful time')
					break
				else:
					print("Incorrect Input")
					print("Press H for instructions")
			print("Game Over\n")
			sleepy_time()
			if comp_health > player_health:
				print("Computer Wins!")
			elif comp_health < player_health:
				print("Player One Wins!")
			else:
				print("Error")
			#As long as the while loop runs the variables remain changed, once the while loop breaks its over. Lets change that
			self.computer.hitpoints = comp_health
			self.player.hitpoints = player_health
			self.comp_fight()
	def comp_fight(self):
		print("Second method initialised")
		print("Please god the variables saved!")
		print("Computer played as " + self.computer.name)
		print("Player has " + str(self.player.hitpoints) + " hitpoints!")
		print("Computer has " + str(self.computer.hitpoints) + " hitpoints!")
		



# Game recognize game
game = Game()
game.fight()
print("Thanks for playing")