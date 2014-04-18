# Name: Vankhanh Dinh
# Project 1
# Due Date: 06/23/13
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Lecture, Notes, Documentation 
#-------------------------------------------------------------------------------
# Comments and assumptions: Extra Credit attempted. Assumes the following:
# User will enter a number for number, and strings for strings.
# Times are in seconds. (Can give fractional seconds.)
# Largest time unit is in days.
# Initial time does not have to be 0.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
"""
Welcome the user to the Timer Application
Ask questions: What
	is your name
	name of the race
	starting time (in seconds)
	time at first lap
	time at second lap
	time at third lap
	time at finish line
		?
Calculate the number of seconds per lap, then total race time.
Print out race name with contestant name on next line
Print each lap name on separate line in seconds
Print out total race time, using days, hours, minutes, and seconds appropriately.
Looks like this:
Madame Trinket's Race for the Curios
contestant: George Mason

lap 1: 848 seconds.
lap 2: 852 seconds.
lap 3: 855 seconds.
lap 4: 1100 seconds.
total race time: 0 days, 1 hours, 0 minutes, and 55 seconds.

For extra credit, use if-else statements so if the lap times aren't increasing
And calculating negative lap times, exactly print phrase
"lap times can't be negative - sorry, quitting!"
Do for each time it's possible for users to enter disallowed times.
Remember to mention in comments that attempting extra credit.
"""
def laptimes():
	"""I'm a question asking function. I ask about what time you got each of
	your laps. I also get very mad at you giving me wibbly-wobbly timey-
	whimey times."""
	time = []
	print("The following is to be answered in the time unit Seconds.")
	input("Press enter to continue")
	for i in range(5): # Index 0 is starting. Index 4 is Final. Between, laps
		if i == 0:
			a = int(input("What was the starting time?\n")) # 2. c
			time.append(a)
		elif i == 4:
			a = int(input("What was time at the finish line?\n")) # 2. g
			if a <= time[-1]:
				print("lap times can't be negative - sorry, quitting!\n") # EC
				quit()
			elif a > time[-1]:
				time.append(a)
		elif (i < 5) or (i > 0):
			a = int(input("What was the time at lap "+str(i)+"?\n")) # 2. d-f
			if a <= time[-1]:
				print("lap times can't be negative - sorry, quitting!\n") # EC
				quit()
			elif a > time[-1]:
				time.append(a)
	return time
def grammar(a): #Self explanatory
	a[0] = "1 day" if a[0] == 1 else str(a[0]) +" days, "
	a[1] = "1 hour, " if a[1] == 1 else  str(a[1])+ " hours, "
	a[2] = "1 minute, "if a[2] == 1 else  str(a[2])+" minutes, "
	a[3] = "and 1 second." if a[3] == 1 else "and "+str(a[3])+" seconds."
	return a
def lapcalc(time): # 3.
	# What we want to do here is find the difference between all of the laps.
	# [start, lap1, lap2, lap3, final] <-- Lap times.
	# [ 10,    22,   45,   55,   100 ]
	#  Lap 1 = lap1-start = 12
	# lap 2 = lap2 - lap1
	# lap 3 = lap3 - lap2
	# lap 4 = final - lap3
	"""How long did it actually take you to make your orbit...
	Who knows? Nobody knows... EXCEPT ME."""
	newtime = [0]*(len(time)-1)
	total = 0
	for i in range(4):
		newtime[i] = time[i+1]-time[i]
	for i in newtime:
		total += i
	for i in range(len(newtime)): #5
		if newtime[i] == 1:
			newtime[i] = "Lap "+str(i+1)+": " + str(newtime[i]) + " second."
		else:
			newtime[i] = "Lap "+str(i+1)+": " + str(newtime[i]) + " seconds."
	days = 0
	hours = 0
	minutes = 0
	while total > 0:
		total -= 60
		minutes += 1
		if minutes == 60:
			minutes -= 60
			hours += 1
			if hours == 24:
				hours -= 24
				days += 1
	total += 60
	a = [days, hours, minutes, total] #6
	a = grammar(a)
	b = "Total racetime: "
	for i in a:
		b += i
	newtime.append(b)
	return newtime
def main():
	"""I'm a main function. When I run, I go do stuff then tell my other
	function buddies to run, when I need something."""
	print("Welcome to the Timer Application!") # 1.
	name = input("What is your name?:\n") # 2. a
	race = input("What is the name of the race?:\n") # 2. b
	time = laptimes() # 2. c-g
	print("\n"*4)
	print("~"*80)
	print(race+ "\n"+ "Contestant: " + name) #4
	newtime = lapcalc(time) #3
	for i in newtime: #5, 6
		print(i)
	print("~"*80)


if __name__ == "__main__": main() #I don't know why I keep writing this line.
# Guess it's force of habit, now. It's really only useful when I'm importing
# self-crafted modules. __name__ evaluates to one of two things:
# "__main__" or the name of the program it is being imported to.
# So, if I decided that I wanted this to run on its own AND be importable,
# That would be the purpose of writing the conditional...
# ... Eh. It might be a good conditional to keep using.
