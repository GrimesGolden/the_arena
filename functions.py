import random

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
		elif letter == "B":
			player = Gladiator()
		elif letter == "C":
			player = Elf()
		else:
			print("Incorrect input\nChoices are A, B or C: ")
	return player()

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
	
