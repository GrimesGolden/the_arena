import time


def sleepy_time():
	"""
	Sleeps for 1 second
	Simulates loading
	"""
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("...")

sleepy_time()
sleepy_time()
print("oh hi")


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
		elif move == "P":
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
	# This will also play if I enter quit, hmm that aint good. 
	# This needs to print only when health is below 100