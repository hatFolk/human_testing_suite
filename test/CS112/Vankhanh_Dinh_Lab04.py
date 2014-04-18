# Write a program that asks user for a percentage grade.
# Assume user correctly enters a number from [0, 100].
# Then prints letter grade earned, like "you earned an A", etc.
""" Grade Scale:
	A == [90, 100]
	B == [80,90)
	C == [70, 80)
	D == [60, 70)
	F == [0, 60)
"""
askgrade = input("What is your percentage grade?")
if "%" in askgrade:
	askgrade = askgrade[:len(askgrade)-2]
askgrade = int(askgrade)
if askgrade >= 90:
	print("You got an A!")
elif askgrade >= 80:
	print("You got a B!")
elif askgrade >= 70:
	print("You got a C!")
elif askgrade >= 60:
	print("You got a D!")
else:
	print("You got an F! Do better next time!")
