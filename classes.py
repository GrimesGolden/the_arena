
import random
import time
# Is this a pokemon clone? Pretty sure it is at this point. 
# Functions

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
	print("Your fighter will die if they reach 0 hit points.\n")
	print("Press P for punch, K for kick, W for weapon (takes 10 stamina), S for special move, or Q to quit.")
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

#***************************************************************************************************************************************************#
#Classes
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
		self.weapon = "Slingshot"

	def special_move(self, i):
		player_health = i
		print("The hobo pulls out a 40oz of King Cobra\n")
		print("AND STARTS CHUGGING!!\n")
		x = random_number(12)
		print("It heals Hobo for " + str(x) +" hitpoints!")
		if x > 6:
			print("||SUPER EFFECTIVE||")
		player_health += x
		print("Player One has " + str(player_health) + " hitpoints.")
		return player_health

		
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
		self.weapon = "Gladius"

	def special_move(self):
		print("Special Move...Coming soon.")
		
class Elf(Fighter):
	"""
	Initializes an Elf class
	"""
	def __init__(self):
		super().__init__()
		self.name ="The Elf"
		self.weapon = "Bow"
	
	def special_move(self):
		print("Special move, coming to a code near you!")
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

	def main(self):
		"""main game loop"""
		comp_health = self.computer.hitpoints
		player_health = self.player.hitpoints
		player_stamina = self.player.stamina
		draw_weapon = 1
		while comp_health >= 0 and player_health >= 0:
			move = input("Enter your move: \n")
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
					player_health = self.player.hitpoints 
					game.comp_fight()
				else:
					print("You punch Computer for " + str(x) + " points \n")
					comp_health -= x
					print("Computer has " + str(comp_health) + " hit points")
					player_health = self.player.hitpoints
					game.comp_fight()
			elif move == "K":
				x = random_number(15)
				if x > 10:
					print("Critical Hit!")
					print("You crit Computer for " + str(x) + " points \n")
					comp_health -= x
					print("Computer has " + str(comp_health) + " hit points")
					player_health = self.player.hitpoints
					game.comp_fight()
				else:
					print("You kick Computer for " + str(x) + " points \n")
					comp_health -= x
					print("Computer has " + str(comp_health) + " hit points")
					player_health = self.player.hitpoints
					game.comp_fight()
			elif move  == "W":
				"""
				Weapon Loop
				"""
				draw_weapon -= 1
				if draw_weapon == 0:
					print("You draw your " + self.player.weapon + "! Ruthless onslaught unlocked.\n")
					sleepy_time()
				if draw_weapon <= 0:
					x = random_number(2)
				if player_stamina < 10:
					print("You are too exhausted to use your weapon!!")
				elif x > 20:
					print("You crit Computer for " + str(x) + " points \n")
					comp_health -= x
					print("Computer has " + str(comp_health) + " hit points")
					print("Your stamina reduced by 10\n")
					player_stamina -= 10
					print(str(player_stamina) + " stamina left.")
					player_health = self.player.hitpoints
					game.comp_fight()
				else:
					print("You attack with " + self.player.weapon + " for" + str(x) + " points \n")
					comp_health -= x
					print("Computer has " + str(comp_health) + " hit points")
					print("Your stamina reduced by 10\n")
					player_stamina -= 10
					print(str(player_stamina) + " stamina left.")
					player_health = self.player.hitpoints
					game.comp_fight()
			elif move == "S":
				player_health = self.player.hitpoints
				self.player.hitpoints = self.player.special_move(player_health)
				#If it doesnt work the problems in the other function
				player_health = self.player.hitpoints
				game.comp_fight()

			elif move == "H":
				instructions()
			elif move == "Q":
				print('||QUIT ENTERED||')
				sleepy_time()
				print("||EXITING||")
				break
			else:
				print("||INCORRECT INPUT||\n")
				print("Press H for instructions")
				sleepy_time()
		if comp_health > player_health:
			print("||GAME OVER||")
			print("||COMPUTER WINS||")
		elif comp_health < player_health:
			print("||GAME OVER||")
			print("||PLAYER ONE WINS")
		else:
			print("Error")
		#As long as the while loop runs the variables remain changed, once the while loop breaks its over. Lets change that
		self.computer.hitpoints = comp_health
		self.player.hitpoints = player_health

	def fight(self):
		"""
		Functional Player One
		Fight Loop
		"""
		i = input("Press any key to begin!\nOr Q to exit.")
		if i == 'Q':
			print("Goodbye!")
		else:
			self.main()

	def comp_fight(self):
		"""
		Computers turn
		Beta Mode
		"""
		comp_health = self.computer.hitpoints
		player_health = self.player.hitpoints
		comp_stamina = self.computer.stamina
		draw_weapon = 1
		comps_move = random_number(3)
		if comps_move == 1:
			x = random_number(15)
			if x > 10:
				sleepy_time()
				print("Critical Hit!")
				print("Computer critically hits player one  for " + str(x) + " points ")
				player_health -= x
				sleepy_time()
				print("Player 1 has " + str(player_health) + " hit points")
				self.player.hitpoints = player_health
			else:
				sleepy_time()
				print("Computer punches player one for " + str(x) + " points ")
				sleepy_time()
				player_health -= x
				sleepy_time()
				print("Player 1 has " + str(player_health) + " hit points")
				self.player.hitpoints = player_health
		elif comps_move == 2:
			x = random_number(15)
			if x > 10:
				sleepy_time()
				print("Critical Hit!")
				print("Computer critically hits player one for " + str(x) + " points ")
				player_health -= x
				sleepy_time()
				print("Player 1 has " + str(player_health) + " hit points")
				self.player.hitpoints = player_health
			else:
				sleepy_time()
				print("Computer kicks player one for " + str(x) + " points ")
				player_health -= x
				sleepy_time()
				print("Player 1 has " + str(player_health) + " hit points")
				self.player.hitpoints = player_health
		elif comps_move  == 3:
			x = random_number(25)
			print("Computer draws " + self.computer.weapon + "!\n" )
			if comp_stamina < 10:
				print("But they are out of stamina\n")
			if comp_stamina > 10:
				player_health -= x
				sleepy_time()
				print(self.computer.weapon + " strike for " + str(x) + " hitpoints.")
				sleepy_time()
				print("Player 1 has " + str(player_health) + " hit points")
				comp_stamina -= 10
				self.computer.stamina = comp_stamina
				self.player.hitpoints = player_health
		else:
			print("Incorrect Input")


		



# Game recognize game
game = Game()
game.fight()
print("Thanks for playing a Grimes Golden product")
print("Please support your local strippers")