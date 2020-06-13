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
		return config.SR
	elif user_input == "3":
		print("Selection not yet implemented")
		return config.MAIN_MENU
	elif user_input == "q" or user_input == "Q" or user_input == "quit" or user_input == "Quit" or user_input == "QUIT":
		print("Thank you for using Arkantos.")
		print("Exiting")
		return config.QUIT
	elif user_input == "h" or user_input == "H" or user_input == "help" or user_input == "Help" or user_input == "HELP":
		print("Help not yet implemented... you're on your own")
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
	elif user_input == "2":
		return config.PLAYABLE_TO_UNLOCKABLE
	elif user_input == "3":
		return config.PLAYABLE_TO_NONPLAYABLE
	elif user_input == "4":
		return config.UNLOCKABLE_TO_PLAYABLE
	elif user_input == "5":
		return config.UNLOCKABLE_TO_NONPLAYABLE
	elif user_input == "6":
		return config.NONPLAYABLE_TO_PLAYABLE
	elif user_input == "7":
		return config.NONPLAYABLE_TO_UNLOCKABLE
	elif user_input == "b":
		print("Returning to main menu")
		return config.MAIN_MENU
	else:
		print("Selection invalid")
		return config.FACTION_PLAYABILITY

def run_current_faction_playability():
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

def run_playability_change_page(purpose, str_set, src, dest):
	e = format_playability_list(src, purpose)
	if e == 0:
		print("error; there are currently no '" + str_set + "' factions")
	else:
		user_input = input("$ ")
		# MUST CHECK IF USER INPUT IS ABLE TO BE CAST TO AN INT
		index = int(user_input) - 1
		if index >= len(src):
			print("error; the specified selection is out of bounds")
		else:
			dest.append(src.pop(index))
	return config.FACTION_PLAYABILITY

def format_playability_list(alist, action):
	print(action)
	if len(alist) == 0:
		return 0 # failure
	else:
		print("Please make a selection:")
		for i in range(0, len(alist)):
			print("\t[" + str(i + 1) + "] " + alist[i])
		return 1 # success

def run_superfaction_relationships():
	print("\t[1].....Display Current Superfaction Relationships")
	print("\t[2].....Add a Superfaction Relationship")
	print("\t[3].....Remove a Superfaction Relationship")
	print("\t[4].....Remove all Superfaction Relationships")
	print("\t[b].....Back\n")
	user_input = input("$ ")

	if user_input == "1":
		return config.CURR_SR
	elif user_input == "2":
		return config.ADD_SR
	elif user_input == "3":
		return config.RM_SR
	elif user_input == "4":
		return config.RM_ALL_SR
	elif user_input == "b":
		print("Returning to main menu")
		return config.MAIN_MENU
	else:
		print("Selection invalid")
		return config.SR

def run_current_sr():
	if config.DESCR_STRAT[5].get_num_sr() == 0:
		print("There are currently no superfaction relationships.")
	else:
		factions = config.DESCR_STRAT[5].factions
		for i in range(0, len(factions)):
			if factions[i].superfaction != "":
				print("\tFaction: " + factions[i].name)
				print("\tSuperfaction: " + factions[i].superfaction + "\n")
	print("\nPress 'return' to continue.")
	user_input = input("$ ")
	return config.SR

def add_sr():
	factions = config.DESCR_STRAT[5].factions
	e = format_faction_super_list(factions, "Select a Subfaction", 0)
	if e == 0:
		print("error, returning to superfaction relationships menu")
		print("\nPress 'return' to continue.")
		user_input = input("$ ")
		return config.SR
	else:
		user_input1 = input("$ ") # user's choice of faction
		e = format_faction_super_list(factions, "Select a Superfaction", 0, int(user_input1) - 1)
		if e == 0:
			print("error, there are no potential superfactions, returning to superfaction relationships menu")
			print("\nPress 'return' to continue.")
			user_input = input("$ ")
			return config.SR
		else:
			user_input2 = input("$ ")
			while user_input1 == user_input2:
				print("Selection invalid; please select a different faction to be a superfaction, or press 'q' to quit.")
				user_input2 = input("$ ")
				if user_input2 == "q" or user_input2 == "Q" or user_input2 == "quit" or user_input2 == "Quit" or user_input2 == "QUIT":
					print("Returning to superfaction relationships menu")
					return config.SR
			factions[int(user_input1) - 1].superfaction = factions[int(user_input2) - 1].name
	return config.SR

def rm_sr():
	factions = config.DESCR_STRAT[5].factions
	e = format_faction_super_list(factions, "Select a Subfaction", 1)
	if e == 0:
		print("error, there are currently no subfactions, returning to superfaction relationships menu")
		print("\nPress 'return' to continue.")
		user_input = input("$ ")
		return config.SR
	else:
		user_input = input("$ ")
		factions[int(user_input) - 1].superfaction = ""
	return config.SR

def rm_all_sr():
	factions = config.DESCR_STRAT[5].factions
	e = format_faction_super_list(factions, "Removing all Superfaction Relationships", 2)
	if e == 0:
		print("error, there are currently no child factions, returning to superfaction relationships menu")
		print("\nPress 'return' to continue.")
		user_input = input("$ ")
		return config.SR
	else:
		for i in range(0, len(factions)):
			factions[i].superfaction = ""
	print("\nPress 'return' to continue.")
	user_input = input("$ ")
	return config.SR

def format_faction_super_list(factions, action, action_code, hide = -1): # code 0 = add; 1 = remove; 2 = remove all # hide is the index to hide
	print(action)
	if len(factions) == 0 or action_code < 0 or action_code > 2 or config.DESCR_STRAT[5].get_num_sr() == 0:
		return 0 # failure
	else:
		print("Please make a selection:")
		for i in range(0, len(factions)):
			if action_code == 0:
				if factions[i].superfaction == "":
					if hide != i:
						print("\t[" + str(i + 1) + "] " + factions[i].name)
			elif action_code == 1:
				if factions[i].superfaction != "":
					if hide != i:
						print("\t[" + str(i + 1) + "] " + factions[i].name)
			elif action_code == 2:
				if factions[i].superfaction != "":
					print("\tRemoving superfaction from....." + factions[i].name)
		return 1 # success

