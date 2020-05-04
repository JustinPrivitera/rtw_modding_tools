# describes objects of the descr_strat.txt file

class landmark:
	def __init__(self, name, x, y):
		self.name = name
		self.pos = point(x, y, "landmark", self.name)

	def to_string(self):
		return "landmark\t" + self.name + "\t" + str(self.pos.x) + ",\t" + str(self.pos.y) + "\r\n"

class resource:
	def __init__(self, name, x, y):
		self.name = name
		self.pos = point(x, y, "resource", self.name)

	def to_string(self):
		return "resource\t" + self.name + ",\t" + str(self.pos.x) + ",\t" + str(self.pos.y) + "\r\n"

class faction:
	def __init__(self):
		self.name = ""
		self.build_pref = ""
		self.unit_pref = ""
		self.superfaction = ""
		self.denari = 0
		self.settlements = []
		self.characters = []

	def to_string(self):
		outstr = "faction\t" + self.name + ", " + self.build_pref + " " + self.unit_pref + "\r\n"
		if self.superfaction != "":
			outstr += "superfaction " + self.superfaction + "\r\n"
		outstr += "denari\t" + str(self.denari) + "\r\n"
		for i in range(0, len(self.settlements)):
			outstr += self.settlements[i].to_string()
		for i in range(0, len(self.characters)):
			if isinstance(self.characters[i], strat_map_character):
				outstr += self.characters[i].to_string()
		outstr += "\r\n"
		if self.name != "slave":
			for i in range(0, len(self.characters)):
				if isinstance(self.characters[i], non_strat_map_character):
					outstr += self.characters[i].to_string()
			outstr += "\r\n"
			for i in range(0, len(self.characters)):
				if isinstance(self.characters[i], named_character):
					# print(self.characters[i].relative_to_string())
					outstr += self.characters[i].relative_to_string()
			outstr += "\r\n"
		outstr += "\r\n"
		return outstr

class settlement:
	def __init__(self):
		self.level = ""
		self.region = ""
		self.year_founded = 0
		self.population = 0
		self.plan_set = "default_set"
		self.faction_creator = ""
		self.buildings = []
		# self.pos = point(-1, -1, "settlement", "")

	def to_string(self):
		outstr = "settlement\r\n{\r\n"
		outstr += "\tlevel " + self.level + "\r\n"
		outstr += "\tregion " + self.region + "\r\n\r\n"
		outstr += "\tyear_founded " + str(self.year_founded) + "\r\n"
		outstr += "\tpopulation " + str(self.population) + "\r\n"
		outstr += "\tplan_set " + self.plan_set + "\r\n"
		outstr += "\tfaction_creator " + self.faction_creator + "\r\n"
		for i in range(0, len(self.buildings)):
			outstr += self.buildings[i].to_string()
		outstr += "}\r\n\r\n"
		return outstr

class building:
	def __init__(self, b_type, b_value):
		self.b_type = b_type
		self.b_value = b_value

	def to_string(self):
		return "\tbuilding\r\n\t{\r\n\t\ttype " + self.b_type + " " + self.b_value + "\r\n\t}\r\n"

class character:
	def __init__(self):
		self.name = ""
		self.age = 0
		# self.faction

class strat_map_character(character):
	def __init__(self):
		character.__init__(self)
		self.char_type = ""
		self.pos = point(-1, -1, "character", "")
		self.traits = [] # a list of trait objects
		self.ancillaries = [] # a list of strings

	def traits_ancillaries_to_string(self):
		outstr = ""
		# traits
		if (len(self.traits) > 0):
			outstr += "traits "
			for i in range(0, len(self.traits) - 1):
				outstr += self.traits[i].to_string() + ", "
			outstr += self.traits[len(self.traits) - 1].to_string() + "\r\n"
			# ancillaries
			if (len(self.ancillaries) > 0):
				outstr += "ancillaries "
				for i in range(0, len(self.ancillaries) - 1):
					outstr += self.ancillaries[i] + ", "
				outstr += self.ancillaries[len(self.ancillaries) - 1] + "\r\n"
		else:
			outstr += "\r\n" # if there are no traits then there are no ancillaries so I can put a newline here without fear
		return outstr

	def to_string(self):
		# first line
		outstr = "character\t" + self.name + ", " + self.char_type + ", age " + str(self.age) + ", , x " + str(self.pos.x) + ", y " + str(self.pos.y) + " \r\n"
		outstr += self.traits_ancillaries_to_string()
		outstr += "\r\n"
		return outstr

class general(strat_map_character):
	def __init__(self):
		strat_map_character.__init__(self)
		self.sub_faction = ""
		self.army = [] # a list of unit objects

	def to_string(self):
		outstr = ""
		# first line
		if self.sub_faction == "":
			outstr = "character\t" + self.name + ", " + self.char_type + ", age " + str(self.age) + ", , x " + str(self.pos.x) + ", y " + str(self.pos.y) + " \r\n"
		else:
			outstr = "character\tsub_faction " + self.sub_faction + ", " + self.name + ", " + self.char_type + ", age " + str(self.age) + ", , x " + str(self.pos.x) + ", y " + str(self.pos.y) + " \r\n"
		outstr += self.traits_ancillaries_to_string()
		# army
		outstr += "army\r\n"
		for i in range(0, len(self.army)):
			outstr += self.army[i].to_string()
		outstr += "\r\n"
		# return complete string
		return outstr

class named_character(general):
	def __init__(self):
		general.__init__(self)
		self.rank = "" # "leader", "heir", or ""
		self.wife = "" # should this point to a character?
		self.children = [] # a list of strings? or of characters

	def rank_to_string(self):
		if len(self.rank) > 0:
			return self.rank + ", "
		else:
			return ""

	def to_string(self):
		# first line
		outstr = "character\t" + self.name + ", " + self.char_type + ", " + self.rank_to_string() + "age " + str(self.age) + ", , x " + str(self.pos.x) + ", y " + str(self.pos.y) + " \r\n"
		outstr += self.traits_ancillaries_to_string()
		# army
		outstr += "army\r\n"
		for i in range(0, len(self.army)):
			outstr += self.army[i].to_string()
		outstr += "\r\n"
		# return complete string
		return outstr

	def relative_to_string(self):
		if self.wife == "":
			return ""
		else:
			outstr = "relative \t" + self.name + ", \t" + self.wife + ",\t\t"
			for i in range(0, len(self.children)):
				outstr += self.children[i] + ",\t"
			outstr += "end\r\n"
			return outstr

class non_strat_map_character(character):
	def __init__(self):
		character.__init__(self)
		self.gender = ""
		self.command = 0 # these don't do anything and I need to change the to_string if I want them to be changeable
		self.influence = 0
		self.management = 0
		self.subterfuge = 0
		self.state = "alive"
		self.leader = "never_a_leader"

	def to_string(self):
		return "character_record\t\t" + self.name + ", \t" + self.gender + ", command 0, influence 0, management 0, subterfuge 0, age " + str(self.age) + ", alive, never_a_leader\r\n"

class trait:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def to_string(self):
		return self.name + " " + str(self.level) + " "

class strat_map_unit:
	def __init__(self, name, exp, armour, weapon_lvl):
		self.name = name
		self.exp = exp
		self.armour = armour
		self.weapon_lvl = weapon_lvl

	def to_string(self):
		return "unit\t\t" + self.name + "\t\t\t\t" + "exp " + str(self.exp) + " armour " + str(self.armour) + " weapon_lvl " + str(self.weapon_lvl) + "\r\n"

class diplomacy_entry: # represents core_attitudes and faction_relationships
	def __init__(self, d_type, faction, stance, targets):
		self.d_type = d_type
		self.faction = faction
		self.stance = stance # int
		self.targets = targets

	def to_string(self):
		outstr = self.d_type + "\t" + self.faction + ",\t\t" + str(self.stance) + "\t\t"
		for i in range(0, len(self.targets) - 1):
			outstr += self.targets[i] + ", "
		outstr += self.targets[len(self.targets) - 1]
		outstr += "\r\n"
		return outstr

class point:
	def __init__(self, x, y, obj, add_info):
		self.x = x # int
		self.y = y # int
		self.obj = obj # object that occupies this point
		self.add_info = add_info # additional info about the object
