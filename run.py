#!/usr/bin/python3

import sys
from pages import *
from descr_strat_opener import *

def main():
	print("---------------------------------------")
	print("Welcome to Arkantos v0.042, a set of modding tools for Rome Total War.\nThese mod tools were developed by Justin Privitera.\n")
	read_data()
	instantiate_pages()
	curr_page = config.MAIN_MENU
	while 1:
		curr_page = config.PAGES[curr_page].run()
		if curr_page == config.QUIT:
			write_data()
			return

def read_data():
	config.DESCR_STRAT = parse_descr_strat()
	# other files

def write_data():
	write_changes(config.DESCR_STRAT)
	# other files

main()
