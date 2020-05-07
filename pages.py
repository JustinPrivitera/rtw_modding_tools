# page object, data from files, page instantiation, page directory, and run functions for each page

from run_pages import *

class page():
	def __init__(self, name, information, action, argument):
		self.name = name
		self.info = information
		self.actn = action
		self.args = argument
		# self.sels = selections
		# self.lpgs = linked_pages

	def run(self):
		print("---------------------------------------")
		print(self.name)
		print(self.info)
		retval = self.actn(* self.args)
		print("---------------------------------------")
		return retval

def instantiate_pages():
	name = "MAIN MENU"
	info = "Press 'h' for help.\n"
	actn = run_main_menu
	args = []
	config.PAGES.append(page(name, info, actn, args))

	#######################################################

	name = "FACTION PLAYABILITY"
	info = "On this page you can edit faction playability.\n"
	actn = run_faction_playability
	args = []
	config.PAGES.append(page(name, info, actn, args))

	name = "CURRENT FACTION PLAYABILITY"
	info = "Displaying current faction playability.\n"
	actn = run_current_faction_playability
	args = []
	config.PAGES.append(page(name, info, actn, args))

	name = "PLAYABLE TO UNLOCKABLE"
	info = "Displaying playable factions.\n"
	actn = run_playability_change_page
	args = ["Playable -> Unlockable", "playable", config.DESCR_STRAT[0].playable, config.DESCR_STRAT[0].unlockable]
	config.PAGES.append(page(name, info, actn, args))

	name = "PLAYABLE TO NONPLAYABLE"
	info = "Displaying playable factions.\n"
	actn = run_playability_change_page
	args = ["Playable -> Nonplayable", "playable", config.DESCR_STRAT[0].playable, config.DESCR_STRAT[0].nonplayable]
	config.PAGES.append(page(name, info, actn, args))

	name = "UNLOCKABLE TO PLAYABLE"
	info = "Displaying unlockable factions.\n"
	actn = run_playability_change_page
	args = ["Unlockable -> Playable", "unlockable", config.DESCR_STRAT[0].unlockable, config.DESCR_STRAT[0].playable]
	config.PAGES.append(page(name, info, actn, args))

	name = "UNLOCKABLE TO NONPLAYABLE"
	info = "Displaying unlockable factions.\n"
	actn = run_playability_change_page
	args = ["Unlockable -> Nonplayable", "unlockable", config.DESCR_STRAT[0].unlockable, config.DESCR_STRAT[0].nonplayable]
	config.PAGES.append(page(name, info, actn, args))

	name = "NONPLAYABLE TO PLAYABLE"
	info = "Displaying nonplayable factions.\n"
	actn = run_playability_change_page
	args = ["Nonplayable -> Playable", "nonplayable", config.DESCR_STRAT[0].nonplayable, config.DESCR_STRAT[0].playable]
	config.PAGES.append(page(name, info, actn, args))

	name = "NONPLAYABLE TO UNLOCKABLE"
	info = "Displaying nonplayable factions.\n"
	actn = run_playability_change_page
	args = ["Nonplayable -> Unlockable", "nonplayable", config.DESCR_STRAT[0].nonplayable, config.DESCR_STRAT[0].unlockable]
	config.PAGES.append(page(name, info, actn, args))

	#######################################################
	# more pages
