	
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
	print("||SELECT FIGHTER NOW||:\n")
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
	print("||Welcome to the Arena||\n")
	sleepy_time()
	print("||2020 Grimes Golden Software||")
	sleepy_time()
	print("||INSTRUCTIONS||")
	print("Every fighter begins with 100 hit points and 50 stamina.\n")
	print("One use of the \'Special Move\' unlocked when below 50 hitpoints\n")
	print("Your fighter will die when below 0 hit points.\n")
	print("||Press P to punch||\n||K to kick||\n||W for weapon (takes 10 stamina)||\n||S for a special move||\n||or Q to quit||")
	time.sleep(1)
	print("\n||Type H at any time to see these instructions again||\n")

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