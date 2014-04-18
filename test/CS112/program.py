# Create a menu application able to display the sum of three numbers
# Or the product there of, or quit.
# Have at least these functions:
#	Get user input and make sure it is valid. Keep asking until valid input get.
#	Function to calculate sum
#	Function to calculate product
#	Main function to display menu and run code.

def menu():
	choice = 0
	while choice < 1:
		try:
			choice = int(input("""Welcome to lab function. Enter a number:
1. Get the sum of three numbers
2. Get the product of three numbers
3. Quit
"""))
		except ValueError:
			choice = 0
			print("Try again!")
		if choice not in range(1,4):
			choice = 0
			print("Try again!")
	return choice

def sum3():
	num = 0
	for i in range(3):
		a = ""
		while a == "":
			try:
				a = float(input("Number "+str(i)+"> "))
			except ValueError:
				a = ""
		num += a
	return num
def product():
	num = 1
	for i in range(3):
		a = ""
		while a == "":
			try:
				a = float(input("Number "+str(i)+"> "))
			except ValueError:
				a = ""
		num *= a
	return num
def main():
	while True:
		choice = menu()
		if choice == 1:
			num = sum3()
			print("The answer is :" + str(num))
		elif choice == 2:
			num = product()
			print("The answer is :" + str(num))
		elif choice == 3:
			print("Bye!")
			break

if __name__ == "__main__": main()
