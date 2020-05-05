#!/usr/bin/python3

import sys

def main(args):
	instantiate_pages().display()

class page():
	def __init__(self, name, actions, args, parent, children):
		self.name = name
		self.actions = actions
		self.args = args
		self.parent = parent
		self.children = children

	def run(self):
		if len(self.args) != len(self.actions):
			print("functions and arguments mismatch", file = sys.stderr)
			return
		for i in range(0, len(self.actions)):
			# self.actions[i]()
			self.actions[i](self.args[i])

	def display(self):
		print("page")
		self.run()

def instantiate_pages():
	return page("Main Menu", [print, print, print], ["test", "test1", "test2"], None, [])

main(sys.argv)
