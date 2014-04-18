choice = input ("do you want the sum or average? "\
				+"(type the word exactly) ")

# we didn't understand...
if choice!="sum" and choice!="average":
	print ("I didn't understand. quitting.")
# we did get a 'sum' or 'average' request.
else:
	num1 = int ( input("next num: "))
	num2 = int ( input("next num: "))
	num3 = int ( input("next num: "))
	num4 = int ( input("next num: "))
	num5 = int ( input("next num: "))
	num6 = int ( input("next num: "))
	sum = num1 + num2 + num3 + num4 + num5 + num6
	
	if choice == "sum":
		print ("your sum is " + str(sum) + ".")
	elif choice == "average":
		avg = sum / 6
		print ("the average is",avg,".")
		print ("When does this run?")

print ("thanks for using the program.")