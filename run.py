#!/usr/bin/python3

import sys

class page():
	def __init__(self, name, information, action, argument):
		self.name = name
		self.info = information
		self.act = action
		self.arg = argument
		# self.sels = selections
		# self.lpgs = linked_pages

	def run(self):
		print("---------------------------------------")
		print(self.name)
		print(self.info)
		retval = FAILURE
		if self.act != None:
			if self.arg == None:
				retval = self.act()
			else:
				retval = self.act(self.arg)
		print("---------------------------------------")
		return retval

FAILURE = -2
QUIT = -1
MAIN_MENU = 0
PAGES = []

def instantiate_pages():
	name = "MAIN MENU"
	info = "Press 'h' for help\n"
	acts = run_main_menu
	args = None
	PAGES.append(page(name, info, acts, args))
	# more pages

def main(args):
	print("---------------------------------------")
	print("Welcome to Arkantos v0.04, a set of modding tools for Rome Total War.\nThese mod tools were developed by Justin Privitera.\n")
	instantiate_pages()
	page_num = MAIN_MENU
	while 1:
		page_num = PAGES[page_num].run()
		if page_num == QUIT:
			return

def run_main_menu():
	# print("---------------------------------------")
	print("Please make a selection:")
	print("\t[1].....Edit Faction Playability")
	print("\t[2].....Edit Superfaction Relationships")
	print("\t[3].....Null")
	print("\t[q].....Quit\n")
	user_input = input("$ ")

	if user_input == "1":
		print("Selection not yet implemented")
		return 0
	elif user_input == "2":
		print("Selection not yet implemented")
		return 0
	elif user_input == "3":
		print("Selection not yet implemented")
		return 0
	elif user_input == "q" or user_input == "Q" or user_input == "quit" or user_input == "Quit" or user_input == "QUIT":
		print("Thank you for using Arkantos.")
		print("Exiting")
		# saving and writing of files SHOULD happen here
		return -1
	elif user_input == "h" or user_input == "H" or user_input == "help" or user_input == "Help" or user_input == "HELP":
		print("Selection not yet implemented")
		return 0
	else:
		print("Selection invalid")
		return 0

main(sys.argv)
