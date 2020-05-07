#!/usr/bin/python3

import sys
from pages import *
from descr_strat_opener import *

def main():
	print("---------------------------------------")
	print("Welcome to Arkantos v0.042, a set of modding tools for Rome Total War.\nThese mod tools were developed by Justin Privitera.\n")
	read_data()
	instantiate_pages()
	cur_page = config.MAIN_MENU
	while 1:
		cur_page = config.PAGES[cur_page].run()
		if cur_page == config.QUIT:
			write_data()
			return

def read_data():
	# global config.DESCR_STRAT
	config.DESCR_STRAT = parse_descr_strat()
	# other files

def write_data():
	# global DESCR_STRAT
	write_changes(config.DESCR_STRAT)
	# other files

main()
