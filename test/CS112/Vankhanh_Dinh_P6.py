#-------------------------------------------------------------------------------
# Name: Vankhanh Dinh
# Project 6
# Section X02
# Due Date: Saturday, August 3rd
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Final Exam Review Guide, Slides, Documentation
#-------------------------------------------------------------------------------
# Comments and assumptions: I'm using all (3) of my late tokens for EC~! (+15)
# Look, An Exception Class. Wasn't necessary for balanceparens(), so only
# implemented for CSVErrors. More EC please (5%)
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
from string import (ascii_letters, digits)

class CSVError(BaseException): # Look, an exception class.
	"""I make and print Errors"""
	def __init__(self, i, string = ""): 
		self.i = i # This is the row number.
		self.string = string # This the error found.
	def __str__(self):
		if self.i == -1: # -1 is Opening Error.
			return "file doesn't exist."
		elif self.i == 0: # Header error.
			return "file was missing valid header row."
		else:
			return "row {} had {}".format(self.i, self.string)

def csvvalid(filename):
	"""I make sure your CSVs are valid. Otherwise, I'm angry."""
	i = -1
	try:
		f = open(filename, "rU")
	except IOError: # Reraise as CSVError
		raise CSVError(i) # Case -1. Unopenable.
	for line in f.readlines():
		line = line[:-1] # Chomp!
		i += 1 # Count the rows.
		if i == 0: # Case 0, Wrong header.
			if line != '"id","name","quantity","price"' :
				raise CSVError(i)
			else:
				continue
		error = lineanalysis(line) # Check for errors.
		if error != None:
			raise CSVError(i, error) # Raise first found.
	print("file is valid.")

def lineanalysis(line):
	"""A way to check for the rest of the CSVErrors is via
	state machine. Take this string:
	"1", "a","0","0"
	^ = "
	state = in quote
	item = 0

	"1", "a","0","0"
	 ^ = 1
	state = in quote
	item = 0

	"1","a","0","0"
	  ^ = "
	state = out quote (expect next char to be ',')
	item = 0

	"1","a","0","0"
	   ^ = ,
	state = out quote (expect next char to be '"')
	item = 0

	"1","a","0","0"
	    ^ = "
	state = in quote
	item = 1 (and etc.) And so if items 0, 2, 3 are not digits, non-numeric.
	If there are other chars besides ',' in out quote besides the first '"'
	disallow.
	if items is < or > 3, wrong number of items.
	"""
	if not(line[0] == line[-1] == '"'): # Cuts the function short in case of
		return "disallowed characters in it." # Futility.
	state = "out quote" # Assume 'out quote' (Not yet in line)
	item = 0 # Number of items in line
	expect = '"' 
	i = 0 # Iterating index
	itemlen = 0
	# Using "in quote" and "out quote" for self-commenting code type thing.
	# An alternative would just to use "True" and "False"
	while i < len(line):
		if item > 4: # catches too many items rather than continue computing
			return "had wrong number of items."
		if line[i] not in ascii_letters + digits +'-" _,\'.': # <-certain others
			return "disallowed characters in it." # No Unicode or extraneous.
		if state == "out quote" and expect == '"': 
			state = "in quote"
			item += 1
		elif state == "out quote" and expect == ',':
			if line[i] != ',':
				return "disallowed characters in it."
			else:
				expect = '"'
		elif state == "in quote" and line[i] == '"':
			state = "out quote"
			expect = ','
			if item in [1,3,4] and itemlen == 0:
				return "non-numeric data where required."
			else:
				itemlen = 0
		elif state == "in quote" and item in [1, 3, 4]:
			if line[i] not in digits:
				return "non-numeric data where required."
			itemlen += 1
		i += 1
	if item < 4: # Catches too few items
		return "had wrong number of items."
	
	return None

def balanceparens(string, stack):
	if len(string) == 0: # Base case.
		return True if stack == [] else False
	else: # Recursive case
		if string[0] == "(":
			stack.append(1) # Adding to the stack length. 
		elif string[0] == ")":
			try:
				stack.pop()
			except IndexError:
				return False # Bogus string handling. Too many )
		elif string[0] not in "()":
			return False # Ew.
		return balanceparens(string[1:], stack) # Forget the first char. Recurse.

def menu(choice = "I'm being initialized!"):
	"""I make sure you actually give me something valid to choose."""
	while choice not in range(1,4):
		try:
			choice = int(input("""1. CSV validator
2. Balanced Parentheses
3. Quit
> """))
		except ValueError:
			pass #Handled below
		if choice not in range(1,4):
			print("Invalid Choice! Redo!")
	return choice

def main(choice = "I'm being initialized!"):
	"""I show you what you can do in this program!"""
	while choice != 3:
		choice = menu()
		if choice == 1:
			try:
				filename = input("Please give me your filename! > ")
				csvvalid(filename)
			except CSVError as e:
				print(e)
		if choice == 2:
			st = [] # Stack. Is over here due to Python memory weirdness.
			ps = input("May I have your string? > ") # Strings.
			print("Balanced!") if balanceparens(ps, st) else print("UNBALANCED")
	print("Bye!")
if __name__ == "__main__": main()
