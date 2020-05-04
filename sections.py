# describes sections of the descr_strat.txt file

from StringToken import stringToken
from descr_strat_objects import *
import sys

SECTION_DELIMITER = ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\r\n"

class section:
	def __init__(self, title, text):
		self.title = title
		self.text = text

	def get_title(self):
		return self.title

	def get_text(self):
		return self.text

	def trim_text(self):
		i = 0
		while i < len(self.text):
			if self.text[i] == "\n":
				self.text.pop(i)
			else:
				i += 1

	def to_string(self):
		outstr = ""
		for i in range(0, len(self.text)):
			if self.text[i] == '\n':
				outstr += "\r\n"
			else:
				outstr += self.text[i]
		return outstr

class settings_section(section):
	def __init__(self, title, text):
		section.__init__(self, title, text)
		self.file_description = ""
		self.campaign = ""
		self.playable = []
		self.unlockable = []
		self.nonplayable = []
		self.start_date = ""
		self.end_date = ""
		self.brigand_spawn_value = 0
		self.pirate_spawn_value = 0
		self.populate()

	def populate(self):
		self.trim_text()
		i = 0
		self.file_description = self.text[i]
		i += 1
		self.campaign = stringToken(self.text[i], "\t")[1]
		i += 2
		while self.text[i] != "end":
			self.playable.append(stringToken(self.text[i], "\t")[0])
			i += 1
		i += 2
		while self.text[i] != "end":
			self.unlockable.append(stringToken(self.text[i], "\t")[0])
			i += 1
		i += 2
		while self.text[i] != "end":
			self.nonplayable.append(stringToken(self.text[i], "\t")[0])
			i += 1
		i += 1
		self.start_date = stringToken(self.text[i], "\t")[1]
		i += 1
		self.end_date = stringToken(self.text[i], "\t")[1]
		i += 1
		self.brigand_spawn_value = int(stringToken(self.text[i], " ")[1])
		i += 1
		self.pirate_spawn_value = int(stringToken(self.text[i], " ")[1])

	def to_string(self):
		outstr = ""
		outstr += self.file_description + "\r\n\r\n"
		outstr += "campaign\t\t" + self.campaign + "\r\n"
		outstr += "playable\r\n"
		for i in range(0, len(self.playable)):
			outstr += "\t" + self.playable[i] + "\r\n"
		outstr += "end\r\n"
		outstr += "unlockable\r\n"
		for i in range(0, len(self.unlockable)):
			outstr += "\t" + self.unlockable[i] + "\r\n"
		outstr += "end\r\n"
		outstr += "nonplayable\r\n"
		for i in range(0, len(self.nonplayable)):
			outstr += "\t" + self.nonplayable[i] + "\r\n"
		outstr += "end\r\n"
		outstr += "\r\n\r\n"
		outstr += "start_date\t" + self.start_date + "\r\n"
		outstr += "end_date\t" + self.end_date + "\r\n"
		outstr += "\r\n"
		outstr += "brigand_spawn_value " + str(self.brigand_spawn_value) + "\r\n"
		outstr += "pirate_spawn_value " + str(self.pirate_spawn_value) + "\r\n"
		outstr += "\r\n\r\n"
		return outstr

class landmarks_section(section):
	def __init__(self, title, text):
		section.__init__(self, title, text)
		self.landmarks = []
		self.populate()

	def populate(self):
		self.trim_text()
		for i in range(2, len(self.text)):
			lm = stringToken(self.text[i], "\t,")
			self.landmarks.append(landmark(lm[1], int(lm[2]), int(lm[3])))

	def to_string(self):
		outstr = ""
		outstr += SECTION_DELIMITER
		outstr += "; >>>> start of landmarks section <<<<\r\n\r\n"
		for i in range(0, len(self.landmarks)):
			outstr += self.landmarks[i].to_string()
		return outstr

class resources_section(section):
	def __init__(self, title, text):
		section.__init__(self, title, text)
		self.resources = []
		self.populate()

	def populate(self):
		self.trim_text()
		for i in range(2, len(self.text)):
			rc = stringToken(self.text[i], "\t,")
			self.resources.append(resource(rc[1], int(rc[2]), int(rc[3])))

	def to_string(self):
		outstr = ""
		outstr += SECTION_DELIMITER
		outstr += "; >>>> start of resources section <<<<\r\n\r\n"
		for i in range(0, len(self.resources)):
			outstr += self.resources[i].to_string()
		return outstr

class factions_section(section):
	def __init__(self, title, text):
		section.__init__(self, title, text)
		self.factions = []
		self.populate()

	def populate(self):
		self.trim_text()
		i = 2
		j = 0
		while i < len(self.text):
			first = stringToken(self.text[i], "\t ,")
			self.factions.append(faction())
			self.factions[j].name = first[1]
			self.factions[j].build_pref = first[2]
			self.factions[j].unit_pref = first[3]
			i += 1
			second = stringToken(self.text[i], " \t")
			third = second
			if second[0] == "superfaction":
				self.factions[j].superfaction = second[1]
				i += 1
				third = stringToken(self.text[i], "\t")
			self.factions[j].denari = int(third[1])
			i += 1
			l = 0 # settlement incrementor
			while stringToken(self.text[i], "\t")[0] != "character": # read settlements
				if self.text[i] == "settlement":
					self.factions[j].settlements.append(settlement())
					k = 2 # index to move through a settlement
					self.factions[j].settlements[l].level = stringToken(self.text[i + k], " ")[1]
					k += 1
					self.factions[j].settlements[l].region = stringToken(self.text[i + k], " ")[1]
					k += 1
					self.factions[j].settlements[l].year_founded = int(stringToken(self.text[i + k], " ")[1])
					k += 1
					self.factions[j].settlements[l].population = int(stringToken(self.text[i + k], " ")[1])
					k += 1
					self.factions[j].settlements[l].plan_set = stringToken(self.text[i + k], " ")[1]
					k += 1
					self.factions[j].settlements[l].faction_creator = stringToken(self.text[i + k], " ")[1]
					k += 1
					if self.text[i + k] == "}": # no buildings case
						i = i + k + 1
					else: # buildings case
						while self.text[i + k] == "\tbuilding":
							info = stringToken(self.text[i + k + 2], " ")
							self.factions[j].settlements[l].buildings.append(building(info[1], info[2]))
							k += 4
						i = i + k + 1
					l += 1
				else:
					print("error reading settlements in " + self.factions[j].name, file = sys.stdout)
					break
			l = 0 # character incrementor
			while stringToken(self.text[i], "\t")[0] != "character_record": # read characters
				first = stringToken(self.text[i], "\t,")
				if first[0] == "character":
					if stringToken(first[1], " ")[0] == "sub_faction":
						self.factions[j].characters.append(general())
						self.factions[j].characters[l].name = stringToken(first[2], " ")[0] # don't these have to be fixed???
						self.factions[j].characters[l].age = int(stringToken(first[4], " ")[1])
						self.factions[j].characters[l].sub_faction = stringToken(first[1], " ")[1]
						self.factions[j].characters[l].char_type = stringToken(first[3], " ")[0]
						self.factions[j].characters[l].pos = point(stringToken(first[6], " ")[1], stringToken(first[7], " ")[1], self.factions[j].characters[l].char_type, self.factions[j].characters[l].name)
						i += 1
						second = self.text[i]
						if second == "army":
							k = 1 # unit incrementor
							unit_line = stringToken(self.text[i + k], "\t")
							while unit_line[0] == "unit":
								unit_stats = stringToken(unit_line[2], " ")
								self.factions[j].characters[l].army.append(strat_map_unit(unit_line[1], int(unit_stats[1]), int(unit_stats[3]), int(unit_stats[5])))
								if len(self.text) > i + k + 1:
									k += 1
								else:
									return # we arrived at EOF so it's time to stop reading things
								unit_line = stringToken(self.text[i + k], "\t")
							i += k
						l += 1
					elif first[2] == " named character":
						self.factions[j].characters.append(named_character())
						self.factions[j].characters[l].name = first[1]
						if first[3] == " heir" or first[3] == " leader":
							self.factions[j].characters[l].rank = first[3].lstrip()
							self.factions[j].characters[l].age = int(stringToken(first[4], " ")[1])
							self.factions[j].characters[l].pos = point(stringToken(first[6], " ")[1], stringToken(first[7], " ")[1], self.factions[j].characters[l].char_type, self.factions[j].characters[l].name)
						else:
							self.factions[j].characters[l].rank = ""
							self.factions[j].characters[l].age = int(stringToken(first[3], " ")[1])
							self.factions[j].characters[l].pos = point(stringToken(first[5], " ")[1], stringToken(first[6], " ")[1], self.factions[j].characters[l].char_type, self.factions[j].characters[l].name)
						self.factions[j].characters[l].wife = "" # to be filled in later
						self.factions[j].characters[l].children = [] # to be filled in later
						self.factions[j].characters[l].sub_faction = ""
						char_type = stringToken(first[2], " ")
						self.factions[j].characters[l].char_type = char_type[0] + " " + char_type[1]
						i += 1
						second = stringToken(self.text[i], " ,")
						third = second
						fourth = third
						if second[0] == "traits":
							k = 1 # traits incrementor
							while k < len(second) - 1:
								self.factions[j].characters[l].traits.append(trait(second[k], int(second[k + 1])))
								k += 2
							i += 1
							third = stringToken(self.text[i], " ,")
							fourth = third
						if third[0] == "ancillaries":
							k = 1 # ancillaries incrementor
							while k < len(third):
								self.factions[j].characters[l].ancillaries.append(third[k])
								k += 1
							i += 1
							fourth = [self.text[i]]
						if fourth[0] == "army":
							k = 1 # unit incrementor
							unit_line = stringToken(self.text[i + k], "\t")
							while unit_line[0] == "unit":
								unit_stats = stringToken(unit_line[2], " ")
								self.factions[j].characters[l].army.append(strat_map_unit(unit_line[1], int(unit_stats[1]), int(unit_stats[3]), int(unit_stats[5])))
								k += 1
								unit_line = stringToken(self.text[i + k], "\t")
							i += k
						l += 1
					elif first[2] == " admiral" or first[2] == " general":
						self.factions[j].characters.append(general())
						self.factions[j].characters[l].name = first[1]
						self.factions[j].characters[l].age = int(stringToken(first[3], " ")[1])
						self.factions[j].characters[l].sub_faction = ""
						self.factions[j].characters[l].char_type = stringToken(first[2], " ")[0]
						self.factions[j].characters[l].pos = point(stringToken(first[5], " ")[1], stringToken(first[6], " ")[1], self.factions[j].characters[l].char_type, self.factions[j].characters[l].name)
						i += 1
						second = stringToken(self.text[i], " ,")
						third = second
						fourth = third
						if second[0] == "traits":
							k = 1 # traits incrementor
							while k < len(second) - 1:
								self.factions[j].characters[l].traits.append(trait(second[k], int(second[k + 1])))
								k += 2
							i += 1
							third = stringToken(self.text[i], " ,")
							fourth = third
						if third[0] == "ancillaries":
							k = 1 # ancillaries incrementor
							while k < len(third):
								self.factions[j].characters[l].ancillaries.append(third[k])
								k += 1
							i += 1
							fourth = [self.text[i]]
						if fourth[0] == "army":
							k = 1 # unit incrementor
							unit_line = stringToken(self.text[i + k], "\t")
							while unit_line[0] == "unit":
								unit_stats = stringToken(unit_line[2], " ")
								self.factions[j].characters[l].army.append(strat_map_unit(unit_line[1], int(unit_stats[1]), int(unit_stats[3]), int(unit_stats[5])))
								k += 1
								unit_line = stringToken(self.text[i + k], "\t")
							i += k
						l += 1
					elif first[2] == " diplomat" or first[2] == " spy":
						self.factions[j].characters.append(strat_map_character())
						self.factions[j].characters[l].name = first[1]
						self.factions[j].characters[l].age = int(stringToken(first[3], " ")[1])
						# self.factions[j].characters[l].sub_faction = ""
						self.factions[j].characters[l].char_type = stringToken(first[2], " ")[0]
						self.factions[j].characters[l].pos = point(stringToken(first[5], " ")[1], stringToken(first[6], " ")[1], self.factions[j].characters[l].char_type, self.factions[j].characters[l].name)
						i += 1
						second = stringToken(self.text[i], " ,")
						third = second
						if second[0] == "traits":
							k = 1 # traits incrementor
							while k < len(second) - 1:
								self.factions[j].characters[l].traits.append(trait(second[k], int(second[k + 1])))
								k += 2
							i += 1
							third = stringToken(self.text[i], " ,")
						if third[0] == "ancillaries":
							k = 1 # ancillaries incrementor
							while k < len(third):
								self.factions[j].characters[l].ancillaries.append(third[k])
								k += 1
							i += 1
						l += 1
					else:
						print("error reading characters in " + self.factions[j].name, file = sys.stdout)
						i += 1
			#l = 0 # character record incrementor
			while stringToken(self.text[i], "\t")[0] != "relative ": # read characters_record
				line = stringToken(self.text[i], "\t,")
				if line[0] == "character_record":
					self.factions[j].characters.append(non_strat_map_character())
					self.factions[j].characters[l].name = line[1]
					self.factions[j].characters[l].gender = line[3]
					# skip traits b/c all are 0
					self.factions[j].characters[l].age = int(stringToken(line[8], " ")[1])
					i += 1
					l += 1
				else:
					print("error reading characters_record in " + self.factions[j].name, file = sys.stdout)
			while stringToken(self.text[i], "\t")[0] == "relative ": # read relatives
				line = stringToken(self.text[i], "\t,")
				for n in range(0, len(self.factions[j].characters)):
					if line[1] == self.factions[j].characters[n].name:
						self.factions[j].characters[n].wife = line[3]
						q = 4
						while line[q] != "end":
							self.factions[j].characters[n].children.append(line[q])
							q += 1
						break
				i += 1
			j += 1

	def to_string(self):
		outstr = ""
		outstr += SECTION_DELIMITER
		outstr += "; >>>> start of factions section <<<<\r\n\r\n"
		for i in range(0, len(self.factions)):
			outstr += self.factions[i].to_string()
		return outstr

# descr_strat has an error where one line of core_attitudes and some of the faction_relationships have an added space
# also, shorter faction names are accompanied by an extra tab for readability, which messes with my parser
# also, all the faction relationship entries have an extra tab
# I've just changed descr_strat so that there are always two tabs separating those entries, I'll test eventually and see if it works
class diplomacy_section(section):
	def __init__(self, title, text):
		section.__init__(self, title, text)
		self.key = []
		self.core_attitudes = []
		self.faction_relationships = []
		self.populate()

	def populate(self):
		self.trim_text()
		for i in range(2, len(self.text)):
			line = stringToken(self.text[i], "\t")
			if self.text[i][0] == ";":
				self.key.append(self.text[i])
			elif line[0] == "core_attitudes":
				self.core_attitudes.append(diplomacy_entry(line[0], stringToken(line[1], ",")[0], int(line[2]), stringToken(line[3], ", ")))
			elif line[0] == "faction_relationships":
				self.faction_relationships.append(diplomacy_entry(line[0], stringToken(line[1], ",")[0], int(line[2]), stringToken(line[3], ", ")))
			else:
				print("error parsing diplomacy section", file = sys.stdout)

	def to_string(self):
		outstr = ""
		outstr += SECTION_DELIMITER
		outstr += "; >>>> start of diplomacy section <<<<\r\n"
		for i in range(0, len(self.key)):
			outstr += self.key[i] + "\r\n"
		outstr += "\r\n"
		for i in range(0, len(self.core_attitudes)):
			outstr += self.core_attitudes[i].to_string()
		outstr += "\r\n"
		for i in range(0, len(self.faction_relationships)):
			outstr += self.faction_relationships[i].to_string()
		return outstr
