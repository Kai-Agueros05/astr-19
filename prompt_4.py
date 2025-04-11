class RedTailedHawk(object): #Labels object RedTailedHawk and creates a class
	"""docstring for RedTailedHawk"""
	#parameters for the hawk, can add as many of these as you want to describe the physical characteristics
	def __init__(self, wingspan, leg_length, num_eyes, has_tail, is_furry):
		self.wingspan = wingspan
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry
	#prints a description of the hawk
	def physical_characteristics(self):
		print("Red Tailed Hawk Traits")
		print(f"Wingspan is {self.wingspan} cm.")
		print(f"Leg Length is {self.leg_length} cm.")
		print(f"Number of eyes is {self.num_eyes}.")
		print(f"Has Tail? {'Yes' if self.has_tail else 'No'}.")
		print(f"Is Furry? {'Yes' if self.is_furry else 'No'}. \n")

class dolphin(object):
	"""docstring for dolphin"""
	def __init__(self, fin_length, has_tail, num_eyes, is_furry):
		self.fin_length = fin_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry

	def physical_traits(self):
		#just a different way of organizing the print sequence
		sentence = "Dolphin Traits:\n "
		sentence += f"Fin length is {self.fin_length}cm. \n" 
		sentence += f"Number of eyes is {self.num_eyes}. \n"
		sentence += f"Has tail? {"Y" if self.has_tail else "N"}. \n"
		sentence += f"Is furry? {"Y" if self.is_furry else "N"}. \n"
		print(sentence)
		

def main():
	#Gives values to the hawk once the program runs, this can be altered as many times
	RedTailedHawk1 = RedTailedHawk(wingspan = 114.6, leg_length = 7.8, num_eyes = 2, has_tail = True, is_furry = False)
	#runs the description printing function
	RedTailedHawk1.physical_characteristics()

	Dolphin1 = dolphin(fin_length = 30.6, num_eyes = 2, has_tail = True, is_furry = False)
	Dolphin1.physical_traits()


if __name__ == '__main__':
	main()

