#!/usr/bin/python3

import sys
from StringToken import stringToken
from sections import *

DESCR_STRAT_LOCATION = "./descr_strat.txt"
DESCR_STRAT_NEW = "./new.txt"

def split_into_sections(filetext):
	sections = []
	j = 0
	for i in range(0, len(filetext)):
		is_section = True
		if filetext[i][0] == ";" and len(filetext[i]) == 165:
			for k in range(0, len(filetext[i])):
				if filetext[i][k] != ";":
					is_section = False
		else:
			is_section = False
		if is_section == True:
			sections.append(filetext[j:i])
			j = i
	sections.append(filetext[j:len(filetext)])
	sections = convert_text_to_section_object(sections)
	return sections

def convert_text_to_section_object(text_list):
	sections = []
	sections.append(settings_section("general settings", text_list[0]))
	sections.append(landmarks_section("landmarks", text_list[1]))
	sections.append(resources_section("resources", text_list[2]))
	sections.append(section("sound emitters", text_list[3]))
	sections.append(section("events", text_list[4]))
	sections.append(factions_section("factions", text_list[5]))
	sections.append(section("diplomacy0", text_list[6]))
	sections.append(diplomacy_section("diplomacy", text_list[7]))
	sections.append(section("regions", text_list[8]))
	return sections

def sections_to_string(sections):
	outstr = ""
	for i in range(0, len(sections)):
		outstr += sections[i].to_string()
	return outstr

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

def display_current_superfaction_relationships(factions):
	print("Displaying Current Superfaction Relationships...")
	for i in range(0, len(factions)):
		if factions[i].superfaction != "":
			print("Faction: " + factions[i].name)
			print("Superfaction: " + factions[i].superfaction + "\n")

def parse_descr_strat():
	infile = open(DESCR_STRAT_LOCATION, "r")
	filetext = stringToken(infile.read(), "\n", 'f')
	infile.close()
	return split_into_sections(filetext)

def write_changes(sections):
	outfile = open(DESCR_STRAT_NEW, "w")
	outfile.write(sections_to_string(sections))
	outfile.close()

# write_changes(parse_descr_strat())

# [x] next task is to write this to file successfully and verify that no changes have been made
# the task after that is to parse each section into smaller and smaller data structures, and build a framework for all of that to be automated
# maybe make a parent object and have each section inherit from it, so they all share a common toString method? - yes

# continue reading information into objects, I left off on the diplomacy section

# make a script that gives every city to rebels and gets rid of every faction as a kind of blank canvas - must add in invisible cities
# probably make a comprehensive list of everything I want to accomplish with my modifications and use that approach to decide how the mod tools will work

