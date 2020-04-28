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

class building:
	def __init__(self, b_type, b_value):
		self.b_type = b_type
		self.b_value = b_value

class character:
	def __init__(self):
		self.name = ""
		self.age = 0
		# self.faction

class strat_map_character(character):
	def __init__(self):
		character.__init__(self)
		self.sub_faction = ""
		self.char_type = ""
		self.pos = point(-1, -1, "character", "")
		self.traits = [] # a list of trait objects
		self.ancillaries = [] # a list of strings

class general(strat_map_character):
	def __init__(self):
		strat_map_character.__init__(self)
		self.sub_faction = ""
		self.army = [] # a list of unit objects

class named_character(general):
	def __init__(self):
		general.__init__(self)
		self.rank = "" # "leader", "heir", or ""
		self.wife = "" # should this point to a character?
		self.children = [] # a list of strings? or of characters

class non_strat_map_character(character):
	def __init__(self):
		character.__init__(self)
		self.gender = ""
		self.command = 0
		self.influence = 0
		self.management = 0
		self.subterfuge = 0
		self.state = "alive"
		self.leader = "never_a_leader"

class trait:
	def __init__(self, name, level):
		self.name = name
		self.level = level

class strat_map_unit:
	def __init__(self, name, exp, armour, weapon_lvl):
		self.name = name
		self.exp = exp
		self.armour = armour
		self.weapon_lvl = weapon_lvl

class point:
	def __init__(self, x, y, obj, add_info):
		self.x = x # int
		self.y = y # int
		self.obj = obj # object that occupies this point
		self.add_info = add_info # additional info about the object
