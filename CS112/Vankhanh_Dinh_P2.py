#-------------------------------------------------------------------------------
# Name: Vankhanh Dinh
# Project 2
# Due Date: 06/28/2013
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Slides, Documentation, mathworld.wolfram.com/AcuteTriangle.html
# wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
#-------------------------------------------------------------------------------
# Comments and assumptions: Integers only, please. (Might be relaxed.)
# Extra Credit Attempted! c:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
"""
Welcome the user to the program: Triangle Checker
Ask them for three different side lengths, one at a time.
If the triangle can exist, print a confirmation. Else, print a denial (and end).
If the triangle exists, print the following yesses and no's like so:
	equilateral:	no
	isoceles:		yes
	acute:			no
	obtuse:			no
	right:			yes
Extra Credit: At the end, ask if they want to do a new triangle.
"yes", "YES", "y", "Y" for affirmative. "no", "NO", "n", "N" for negative.

So parts of the assignment: Check for existance. Then for properties. Then format.
Print.

Notes: Law of Cosines: a^2 + b^2 - 2abcos(C) = c^2
"""
def isRight(a,b,c): # Checks for right-ness
	checking = [a,b,c]
	trimax = max(checking)
	side1 = min(checking)
	side2 = 0
	for i in checking:
		if i != trimax or i != side1:
			side2 = i
	if trimax**2 == (side1**2 + side2**2):
		return True
	return False
def isAcute(a,b,c):
	what = (((a**2+b**2)>c**2) and ((b**2+c**2)>a**2) and ((c**2+a**2)>b**2))
	return True if what else False
	# A derivation of law of cosine and pythagorean triangle.
def repeat():
	repeat = ""
	while repeat == "":
		repeat = input("Do you want to go again?")
		if repeat in ["Yes","yes","YES", "y", "Y"]: # Seek answers!
			return True
		elif repeat in ["No","no", "NO", "n", "N"]:
			print("Bye!")
			return False
		else:
			print("Try again!")
			repeat = ""
def properties(a,b,c):
	certificate = [["equilateral:\t", 0], #index 0
			["isosceles:\t",0], #index 1
			["acute:\t\t",0], #index 2
			["obtuse: \t",0], #index 3
			["right:\t\t", 0]] #index 4
	certificate[0][1] = "yes" if (a==b==c) else "no"
	certificate[1][1] = "yes" if ((a==b) or (a==c) or (b==c)) else "no"
	if isAcute(a,b,c): # Really, I only made the function so I could fit
		certificate[2][1] = "yes" #the 80 line limit.
		certificate[3][1] = certificate[4][1] = "no"
		return certificate # No point in checking the others.
	else:
		certificate[2][1] = "no"
	if isRight(a,b,c):
		certificate[3][1] = "yes"
		certificate[4][1] = "no"
	else:
		certificate[3][1] = "no" # By definition, an existant triangle that
		certificate[4][1] = "yes" # is not right nor acute is obtuse.
	return certificate
def isTriangle(a,b,c): # Checks if the triangle can exist.
	return True if ((a + b > c) and (a+c> b) and (b+c>a)) else False
def main():
	while True: # EC. Will repeat forever if necessary.
		print("""I am Triangle Checker! Happy to meet you.
I tell you if your triangle exists and what kind it is.
Give me your three sides!""") #Greeted.
		a = int(input("Side 1: ")) #Asking for side lengths.
		b = int(input("Side 2: ")) #Assuming ints.
		c = int(input("Side 3: ")) #Technically could eval.
		if isTriangle(a,b,c): #Self-explanatory.
			print("Your triangle exists! Hurrah!") # Congratulate
			print("Now what is it?")
			certificate = properties(a,b,c) # A list[][] of strings.
			for i in certificate:
				print(i[0]+i[1]) # It has the property info.
		else:
			print("Your triangle is disappointing. No triangle.")
		if repeat(): # I don't know why I can't write this in one line format.
			continue
		else:
			break

if __name__ == "__main__": main()
