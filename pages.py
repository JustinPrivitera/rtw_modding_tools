# page object, data from files, page instantiation, page directory, and run functions for each page

from run_pages import *

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
		retval = config.FAILURE
		if self.act != None:
			if self.arg == None:
				retval = self.act()
			else:
				retval = self.act(self.arg)
		print("---------------------------------------")
		return retval

	# def update_argument(self, argument):
	# 	self.arg = argument

def instantiate_pages():
	name = "MAIN MENU"
	info = "Press 'h' for help.\n"
	act = run_main_menu
	arg = None
	config.PAGES.append(page(name, info, act, arg))

	name = "FACTION PLAYABILITY"
	info = "On this page you can edit faction playability.\n"
	act = run_faction_playability
	arg = None
	config.PAGES.append(page(name, info, act, arg))

	name = "CURRENT FACTION PLAYABILITY"
	info = "This page displays current faction playability.\n"
	act = run_current_faction_playability
	arg = None
	config.PAGES.append(page(name, info, act, arg))
	# more pages
