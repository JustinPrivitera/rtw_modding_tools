#!/usr/bin/python3

from descr_strat_opener import *
import sys

def main(args):
	print("Welcome to Arkantos v0.03, a set of modding tools for Rome Total War.")
	print("These mod tools were developed by Justin Privitera.\n")

	while 1:
		print("---------------------------------------")
		print("Please make a selection:")
		print("\t[1].....Edit Faction Playability")
		print("\t[2].....Edit Superfaction Relationships")
		print("\t[3].....Null")
		print("\t[q].....Quit\n")
		user_input = input("$ ")

		if user_input == "1":
			selection1()
		elif user_input == "2":
			selection2()
		elif user_input == "3":
			print("Selection not yet implemented\n")
		elif user_input == "q" or user_input == "Q" or user_input == "quit" or user_input == "Quit" or user_input == "QUIT":
			print("Thank you for using Arkantos.")
			print("Exiting")
			# saving and writing of files SHOULD happen here
			return
		else:
			print("Selection invalid\n")


	# be able to catch exceptions and complain for invalid input
	# a button to give more information on each option?
	# maybe make it work like a shell and show you where you are?

def selection1():
	sections = parse_descr_strat()
	print("---------------------------------------")
	display_current_faction_playability(sections)

	while 1:
		print("---------------------------------------")
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
			display_current_faction_playability(sections)
		elif user_input == "2":
			e = format_playability_list(sections[0].playable, "Playable -> Unlockable")
			if e == 0:
				print("error, there are no currently 'playable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].unlockable.append(sections[0].playable.pop(int(user_input) - 1))
		elif user_input == "3":
			e = format_playability_list(sections[0].playable, "Playable -> Nonplayable")
			if e == 0:
				print("error, there are no currently 'playable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].nonplayable.append(sections[0].playable.pop(int(user_input) - 1))
		elif user_input == "4":
			e = format_playability_list(sections[0].unlockable, "Unlockable -> Playable")
			if e == 0:
				print("error, there are no currently 'unlockable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].playable.append(sections[0].unlockable.pop(int(user_input) - 1))
		elif user_input == "5":
			e = format_playability_list(sections[0].unlockable, "Unlockable -> Nonplayable")
			if e == 0:
				print("error, there are no currently 'unlockable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].nonplayable.append(sections[0].unlockable.pop(int(user_input) - 1))
		elif user_input == "6":
			e = format_playability_list(sections[0].nonplayable, "Nonplayable -> Playable")
			if e == 0:
				print("error, there are no currently 'nonplayable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].playable.append(sections[0].nonplayable.pop(int(user_input) - 1))
		elif user_input == "7":
			e = format_playability_list(sections[0].nonplayable, "Nonplayable -> Unlockable")
			if e == 0:
				print("error, there are no currently 'nonplayable' factions")
			# must catch index out of bounds error
			else:
				user_input = input("$ ")
				sections[0].unlockable.append(sections[0].nonplayable.pop(int(user_input) - 1))
		elif user_input == "b":
			print("Saving and returning to main menu")
			write_changes(sections)
			return
		else:
			print("Selection invalid\n")

def format_playability_list(alist, action):
	print(action)
	if len(alist) == 0:
		return 0 # failure
	else:
		print("Please make a selection:")
		for i in range(0, len(alist)):
			print("\t[" + str(i + 1) + "] " + alist[i])
		return 1 # success

def selection2():
	# TODO
	# - prevent factions from being in nested superfaction relationships? No grandchildren allowed
	# - MAYBE fix indices when prompted and somehow convert to true indices
	sections = parse_descr_strat()
	print("---------------------------------------")
	display_current_superfaction_relationships(sections[5].factions)

	while 1:
		print("---------------------------------------")
		print("Please make a selection:")
		print("\t[1].....Display Current Superfaction Relationships")
		print("\t[2].....Add a Superfaction Relationship")
		print("\t[3].....Remove a Superfaction Relationship")
		print("\t[4].....Remove all Superfaction Relationships")
		print("\t[b].....Back\n")
		user_input = input("$ ")

		if user_input == "1":
			display_current_superfaction_relationships(sections[5].factions)
		elif user_input == "2":
			e = format_faction_super_list(sections[5].factions, "Add a Superfaction Relationship", 0)
			if e == 0:
				print("error, there are currently no factions")
			else:
				user_input1 = input("$ ")
				e = format_faction_super_list(sections[5].factions, "Displaying Available Superfactions", 0, int(user_input1) - 1)
				if e == 0:
					print("error, there are currently no potential superfactions")
				else:
					user_input2 = input("$ ")
					if user_input1 == user_input2:
						print("Selection invalid; please select a different faction to be a superfaction.")
					else:
						sections[5].factions[int(user_input1) - 1].superfaction = sections[5].factions[int(user_input2) - 1].name
		elif user_input == "3":
			e = format_faction_super_list(sections[5].factions, "Remove a Superfaction Relationship", 1)
			if e == 0:
				print("error, there are currently no child factions")
			else:
				user_input = input("$ ")
				sections[5].factions[int(user_input) - 1].superfaction = ""
		elif user_input == "4":
			e = format_faction_super_list(sections[5].factions, "Remove all Superfaction Relationships", 2)
			if e == 0:
				print("error, there are currently no child factions")
			else:
				for i in range(0, len(sections[5].factions)):
					sections[5].factions[i].superfaction = ""
		elif user_input == "b":
			print("Saving and returning to main menu")
			write_changes(sections)
			return
		else:
			print("Selection invalid\n")

def format_faction_super_list(factions, action, action_code, hide = -1): # code 0 = add; 1 = remove; 2 = remove all # hide is the index to hide
	print(action)
	if len(factions) == 0 or action_code < 0 or action_code > 2:
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

main(sys.argv)
