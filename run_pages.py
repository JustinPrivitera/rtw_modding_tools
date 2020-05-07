# functions that run each page in the program

import config

def run_main_menu():
	print("Please make a selection:")
	print("\t[1].....Edit Faction Playability")
	print("\t[2].....Edit Superfaction Relationships")
	print("\t[3].....Null")
	print("\t[q].....Quit\n")
	user_input = input("$ ")

	if user_input == "1":
		return config.FACTION_PLAYABILITY
	elif user_input == "2":
		print("Selection not yet implemented")
		return config.MAIN_MENU
	elif user_input == "3":
		print("Selection not yet implemented")
		return config.MAIN_MENU
	elif user_input == "q" or user_input == "Q" or user_input == "quit" or user_input == "Quit" or user_input == "QUIT":
		print("Thank you for using Arkantos.")
		print("Exiting")
		# saving and writing of files SHOULD happen here
		return config.QUIT
	elif user_input == "h" or user_input == "H" or user_input == "help" or user_input == "Help" or user_input == "HELP":
		print("Selection not yet implemented")
		return config.MAIN_MENU
	else:
		print("Selection invalid")
		return config.MAIN_MENU

def run_faction_playability():
	print("Please make a selection:")
	print("\t[1].....Display Current Faction Playability")
	print("\t[2].....Playable -> Unlockable")
	print("\t[3].....Playable -> Nonplayable")
	print("\t[4].....Unlockable -> Playable")
	print("\t[5].....Unlockable -> Nonplayable")
	print("\t[6].....Nonplayable -> Playable")
	print("\t[7].....Nonplayable -> Unlockable")
	print("\t[b].....Back\n")
	user_input = input("$ ")

	if user_input == "1":
		return config.CURRENT_FACTION_PLAYABILITY
	# elif user_input == "2":
	# 	e = format_playability_list(sections[0].playable, "Playable -> Unlockable")
	# 	if e == 0:
	# 		print("error, there are no currently 'playable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].unlockable.append(sections[0].playable.pop(int(user_input) - 1))
	# elif user_input == "3":
	# 	e = format_playability_list(sections[0].playable, "Playable -> Nonplayable")
	# 	if e == 0:
	# 		print("error, there are no currently 'playable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].nonplayable.append(sections[0].playable.pop(int(user_input) - 1))
	# elif user_input == "4":
	# 	e = format_playability_list(sections[0].unlockable, "Unlockable -> Playable")
	# 	if e == 0:
	# 		print("error, there are no currently 'unlockable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].playable.append(sections[0].unlockable.pop(int(user_input) - 1))
	# elif user_input == "5":
	# 	e = format_playability_list(sections[0].unlockable, "Unlockable -> Nonplayable")
	# 	if e == 0:
	# 		print("error, there are no currently 'unlockable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].nonplayable.append(sections[0].unlockable.pop(int(user_input) - 1))
	# elif user_input == "6":
	# 	e = format_playability_list(sections[0].nonplayable, "Nonplayable -> Playable")
	# 	if e == 0:
	# 		print("error, there are no currently 'nonplayable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].playable.append(sections[0].nonplayable.pop(int(user_input) - 1))
	# elif user_input == "7":
	# 	e = format_playability_list(sections[0].nonplayable, "Nonplayable -> Unlockable")
	# 	if e == 0:
	# 		print("error, there are no currently 'nonplayable' factions")
	# 	# must catch index out of bounds error
	# 	else:
	# 		user_input = input("$ ")
	# 		sections[0].unlockable.append(sections[0].nonplayable.pop(int(user_input) - 1))
	elif user_input == "b":
		print("Returning to main menu")
		return config.MAIN_MENU
	else:
		print("Selection invalid")
		return config.FACTION_PLAYABILITY

def run_current_faction_playability():
	# print("Displaying Current Faction Playability...")
	print("Playable:")
	for i in range(0, len(config.DESCR_STRAT[0].playable)):
		print("\t" + config.DESCR_STRAT[0].playable[i])
	print("Unlockable:")
	for i in range(0, len(config.DESCR_STRAT[0].unlockable)):
		print("\t" + config.DESCR_STRAT[0].unlockable[i])
	print("Nonplayable:")
	for i in range(0, len(config.DESCR_STRAT[0].nonplayable)):
		print("\t" + config.DESCR_STRAT[0].nonplayable[i])
	print("\nPress 'return' to continue.")
	user_input = input("$ ")
	return config.FACTION_PLAYABILITY