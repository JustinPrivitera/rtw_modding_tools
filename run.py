#!/usr/bin/python3

from descr_strat_opener import *
import sys

def main(args):
	print("Welcome to Arkantos v0.02, a set of modding tools for Rome Total War.")
	print("These mod tools were developed by Justin Privitera.\n")

	while 1:
		print("---------------------------------------")
		print("Please make a selection:")
		print("\t[1].....Edit Faction Playability")
		print("\t[2].....Null")
		print("\t[3].....Null")
		print("\t[q].....Quit\n")
		user_input = input("$ ")

		if user_input == "1":
			selection1()
		elif user_input == "2":
			print("Selection not yet implemented\n")
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

def display_current_faction_playability(sections):
	print("Displaying Current Faction Playability...")
	print("Playable:")
	for i in range(0, len(sections[0].playable)):
		print("\t" + sections[0].playable[i])
	print("Unlockable:")
	for i in range(0, len(sections[0].unlockable)):
		print("\t" + sections[0].unlockable[i])
	print("Nonplayable:")
	for i in range(0, len(sections[0].nonplayable)):
		print("\t" + sections[0].nonplayable[i])
	print()

def format_playability_list(alist, action):
	print(action)
	if len(alist) == 0:
		return 0 # failure
	else:
		print("Please make a selection:")
		for i in range(0, len(alist)):
			print("\t[" + str(i + 1) + "] " + alist[i])
		return 1 # success


main(sys.argv)
