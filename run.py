#!/usr/bin/python3

import sys
from pages import *
from descr_strat_opener import *

DESCR_STRAT = []
# other data entries

def main():
	print("---------------------------------------")
	print("Welcome to Arkantos v0.041, a set of modding tools for Rome Total War.\nThese mod tools were developed by Justin Privitera.\n")
	read_data()
	instantiate_pages()
	cur_page = MAIN_MENU
	while 1:
		cur_page = PAGES[cur_page].run()
		if cur_page == QUIT:
			write_data()
			return

def instantiate_pages():
	global DESCR_STRAT

	name = "MAIN MENU"
	info = "Press 'h' for help.\n"
	act = run_main_menu
	arg = None
	PAGES.append(page(name, info, act, arg))

	name = "FACTION PLAYABILITY"
	info = "On this page you can edit faction playability.\n"
	act = run_faction_playability
	arg = DESCR_STRAT
	PAGES.append(page(name, info, act, arg))

	name = "CURRENT FACTION PLAYABILITY"
	info = "This page displays current faction playability.\n"
	act = run_current_faction_playability
	arg = DESCR_STRAT
	PAGES.append(page(name, info, act, arg))
	# more pages

def read_data():
	global DESCR_STRAT
	DESCR_STRAT = parse_descr_strat()
	# other files

def write_data():
	global DESCR_STRAT
	write_changes(DESCR_STRAT)
	# other files

main()
