from sys import exit
from random import randint

class Scence(object):
	def enter(self):
		print ("This scence is not yet configured")
			exit(1)

class Engine(object):
	def __init__(self, scence_map):
		self.scence_map = scence_map
	def play(self):
		current_scence = self.scence_map.opening_scence()
		while (True):
			print("\n-----")
			next_scence_name = current_scence.enter()
			current_scence = self.scence_map.next_scence(next_scence_name)

class Death(Scence):
	quips = [
	"You died."
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scence):
	def enter(self):
		



