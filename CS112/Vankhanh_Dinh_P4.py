#-------------------------------------------------------------------------------
# Name: Vankhanh (Lilas) Dinh
# Project 4
# Section X02
# Due Date: Friday, July 12th, at 23:59
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: DOCUMENTATION! SLIDES! Other stuff. c:
#-------------------------------------------------------------------------------
# Comments and assumptions: EXTRA CREDIT ATTEMPTED!!! Hehe.
# This thing actually parses c-code. It's rather fascinating.
# Oh, it also handles if EOF is written first!
# None of the functions can be used if there is nothing written, therefore
# Nothing to be compared.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
"""
Ask user for text input. Continue collecting and storing text until a line only
containing "EOF" on a line appears.

Then present menu:

Text Analyzer Menu (select by number):
	1. shortest word
	2. longest word
	3. most common word
	4. left-column secret message!
	5. fifth-words secret message!
	6. word count
	7. quit

1. shortest word: report the shortest word found in the text. For ties, report
the first word.
2. longest word: Report the longest word found in the text. For ties, report the
first word.
3. most common word: Report the word that shows up the most. For ties, report
all the ones with that many times.
4. left-column secret message: As an example of an acrostic, we are curious if
the first letters of the first word on each line make up a message. You will
extract these letters and report the resulting message as a single printed
string. For blank lines, you will include a space in the output.
5. fifth-words secret message: Similar to option 4, this one simply grabs every
fifth word, regardless of line breaks. You must start with the very first word
included. Report the answer in sentence form, such as "The the the the pies
interiors are Sagan" below. Do not just print a list with all of its brackets
and commas!
6. word count. Report the total number of words in the text. Don't worry about
finding duplicates. (Each occurance of the same word will get counted, so
"I think that that is good" would have 6 words).
7. quit: If the user chooses this option, the program should manage to end (do
no more printing or input-requests except to print "Goodbye!").
All other values should not crash the program, but allow a redo of choice.
Repeat the mainmenu after each function, but never allow additional text-input.
Ignore all punctuation, handling the following characters at minimum:
	[] () {} ' " . , / ? ! ; : -=+
Anything with an apostrophe will get counted twice:
	"there's more" will count as three words: "there","s","more"
Notice that (a"b.c!d:e) has five words in it, although there are no spaces
in that string. So knowing that all punctuation will cause word-breaks, think
ahead when storing user-input.

EC: Implement each menu option as functions, called in the menu. Make the rest
of the program contents in function main(), calling it once in the end.
No global variables for full credit.
"""

def textreplace(line): # Editting the text to find punctuation.
	for i in line: # Takes the line inputted.
		if i in "[](){}'\".,/?!;:-=+": # Looks for these.
			line = line.replace(i, " ") # Replaces it with spaces.
	return line.lstrip() # Then takes the beginning spaces out.

def textstore(): # Getting text input and organizing the words. 
	text = [] # Gets individual words
	textwithnewline = [] # Gets line by line action.
	while True: # Forever and ever!
		line = input("> ") # So people know to start typing.
		if line == "EOF": #Condition for stopping input.
			if len(text) == 0:
				print("Error.")
			else:
				break
		else:
			line = textreplace(line) # Takes line. Finds punctuation. Edit.
			if line == "": # empty strings block calculations in other functions
				line = " " # Fixed!
			textwithnewline.append(line) # Store line.
			text += line.split() # Store words.
	return text, textwithnewline # Returns the two.
def minword(text): # Option 1. Getting the earliest shortest word.
	shortest = text*len(text) #I'm worried about extremely long words.
	for i in text:
		if len(i) < len(shortest): #Standard min algorithm.
			shortest = i
	return shortest

def maxword(text): # Option 2. Getting the earliest longest word.
	longest = "" # Empty string is 0. Lengths are positive.
	for i in text: 
		if len(i) > len(longest): # Standard max algorithm.
			longest = i
	return longest

def modeword(text): # Option 3. Getting the most frequent words.
	freq = {} 
	freqlist = []
	for i in text:
		if i.lower() in freq: #Check if word is in the dictionary already.
			freq[i] += 1 # If so, value += 1
		else:
			freq[i] = 1 # Otherwise, initiate at 1
	mode = max(freq.values()) # Get the maximum value recorded.
	for k, v in freq.items(): # Iterate through.
		if v == mode: # If the value is equal to the maximum frequency
			freqlist.append(k) # add it to the list
	return mode, freqlist # Return the two variables to be used elsewhere.

def acrosticmsg(textwithnewline): # Option 4. Left-Column secret message.
	acrostic = ""
	for i in textwithnewline: # Gets the first word of every line.
		acrostic += i[0] # Adds it to the string.
	return acrostic

def everyfifthword(text): # Option 5. Fifth-words secret message
	message = ""
	i = 0
	while i < len(text): # Technically, you could do this with list comps.
		message += text[i]+ " "# But this works just as well.
		i += 5
	return message

def wordCount(text): # Option 6. That was easy. Built-in functions, ftw.
	wordcount = len(text)
	return wordcount

def menu(): # I'm a menu. Give me your option.
	choice = 0
	while choice < 1:
		try: # Btw, if you give me messed up inputs
			choice = int(input("""Text Analyzer Menu (Select by Number):
			1. shortest word
			2. longest word
			3. most common word
			4. left-column secret message!
			5. fifth-words secret message
			6. word count
			7. quit
"""))
		except ValueError: # I make sure you try again.
			print("Error. That's invalid.") # (Non numbers.)
			choice = 0
		if choice not in range(1,8): # (Non-existant options)
			choice = 0
			print("Really, guys? Try again.") # And I'm snarky.
	return choice #Oh, you made it. Good.

def main(): # I'M A MAIN FUNCTION. I'm the rails of this system.
	print("Input your text. Write 'EOF' when done.")
	text, textwithnewline = textstore() # One is a list of words. The other is
	while True: #A list of lines inputted.
		choice = menu() #Grabs the menu and returns the choices.
		if choice == 1: # Each number corresponds with a different choice.
			shortest = minword(text)
			print("Shortest word first is '"+shortest+"'.")
		elif choice == 2:
			longest = maxword(text)
			print("Longest word first is '"+longest+"'.")
		elif choice == 3:
			mode, freqlist = modeword(text)
			print("Most Frequently Occuring at "+str(mode)+" times!")
			for i in freqlist:
				print(i)
		elif choice == 4:
			acrostic = acrosticmsg(textwithnewline)
			print("Here's an Acrostic of your text.\n{}".format(acrostic))
		elif choice == 5:
			message = everyfifthword(text)
			print("Here's every five words: ")
			print(message)
		elif choice == 6: # This one was pointless to make a function for, really.
			wordcount = wordCount(text)
			print("The word count was ", wordcount)
		elif choice == 7:
			print("AWESOME. See you later!") #Quit.
			break
if __name__ == "__main__": main() #Calling main. Never know when I'll want to
# Import this. Can't hurt.
