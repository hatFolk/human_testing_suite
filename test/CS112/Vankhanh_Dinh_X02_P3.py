#-------------------------------------------------------------------------------
# Name: Vankhanh Dinh
# Project 3
# Section X02
# Due Date: 07/03/2013
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Slides, Documentation [Tons] 
#-------------------------------------------------------------------------------
# Comments and assumptions: Extra Credit Attempted.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
""" Make a main menu that looks like this:
	Welcome to the Loopalyzer Menu! Please select an option by typing in the
	number.

	1. the final countdown!
	2. count the divisors
	3. binary number parity check
	4. quit

Must use loops on options 1-3.
Option 1. Ask "what are we counting down from?" and get a number (assume int,
non-negative). Print each number from the given value down to zero on separate
lines, then print "lift-off!"
For example user types 3:
	3...
	2...
	1...
	lift-off!

Option 2. count the divisors. Ask the user for a positive integer (assume 
correctly entered). Count how many divisors it has from [1, number].
Print message like "The number 6 has 4 divisors.", based on number and
divisor count.

Option 3: binary number parity check. Binary numbers only have 1's and 0's.
Parity check is a mechanism for transmitted data to be quickly checked for 
incorrect transmission. Get binary number from user. Then parity bit.
To check if parity bit matches binary, add the 1's. If odd and parity bit is
1, it is correct. If even and parity bit is 0, it is correct. Else, failed.
Print "Successful tranismission" or "FAILURE!!!" for appropriate response.

Option 4: quit. If the user chooses this, the program should end.
Don't do printing or input-requests except to print "Goodbye".

Other values: Do not quit, do not crash. Let user retry.

EC: Crash-proof program. Program should -never- crash. Recommended: use
Exceptions.
"""
def countdown(n = -1): 							  #Does countdown option (1)
	while n == -1:
		try:				 					  # Check for positive integer.
			n = int(input("What number do you want to count down from?\n"))
		except ValueError:
			n = -1		    					  # Rest of the loop catches bad
			print("What did you say?")			  # input.
		if n < 0:
			print("You're joshing me. Try again.")
	for i in range(n, 0, -1): 					  # Simple for-loop for
		print("{}...".format(i))				  # counting down.
	print("Lift off!") 							  # Don't really need the 
												  # for-else construct.
def divisors(n = 0, counter = 0): 				  # Does divisors option (2)
	while n <= 0 : 								  # Get/Find good/bad input.
		try:
			n = int(input("What number do you want analyzed?\n"))
		except ValueError:
			n = 0
			print("Try again.")
		if n < 0:
			print("Non-Negative, please.")
		elif n == 0: 							  # 0 is special case. Invalid.
			print("0 is infinitely divisible except by 0.")
			print("Analyze something else.")
	for i in range(1,n+1): 						  # goes through [1,n] to find
		if n%i == 0: 							  # factors. Only really need  
			counter += 1 						  # to check up to n//2.
	print("The number {n} has {counter} divisors.".format(n=n,counter=counter))
												  
def parity(binary = -1, parity = -1, paritycheck = 0, allowDigit = ["0","1"]):
	while binary == -1: 						  # Looks for bad input.
		binary = input("Please input your binary string!")
		for i in binary: 						  # If input is good,
			if i in allowDigit:					  # add it to paritycheck.
				paritycheck += int(i)
			else: 								  # Bad Input, reset.
				paritycheck = 0
				binary = -1
				print("Invalid String. Try again.")
				break 					  	      # Bad string, bad. 
		paritycheck %= 2 						  # "What is good parity bit?" 
	while parity == -1: 					      # Looks for bad input.
		parity = input("Input Parity Bit: ")
		if parity not in allowDigit: 
			parity = -1 						  #Reset. Try again.
			print("Error. That's not a valid bit.")
		else: 									  #Checks if parity bit matches.
			if paritycheck == int(parity):
				print("Transmission successful!") # Even == 0. Odd == 1.
			else:
				print("Failure!!") 				  # Fail. 

def exiting(): 									  # A quitting function (4)
	print("Good bye!") 							  # Didn't have to make it.
	quit()										  # Just wanted to say bye

def menu(choice = 0): 							  # Gets the choices
	while choice not in range(1,5):
		try:
			choice = int(input("""1. The final countdown
2. count the divisors
3. binary number parity check
4. quit\n"""))
		except ValueError:
			print("Error. Try again.")
			choice = 0
		if choice not in range(1,5):
			print("Error. Try again.")
			choice = 0
	return choice

def main(): 									  # Main body
	print("Welcome to the Loopalyzer Menu! Please select an option by typing"+\
	" in the number.\n")
	while True:									  # Select option via index.
		choice = menu()
		if choice == 1:
			countdown()
		elif choice == 2:
			divisors()
		elif choice == 3:
			parity()
		elif choice == 4:
			exiting()

if __name__ == "__main__":main() 
