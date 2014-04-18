
choice = input("do you want the sum or the average?")

count = 7
if choice in ["sum", "Sum", "SUM","average"]:
	n1 = int(input("next num:"))
	n2 = int(input("next num:"))
	n3 = int(input("next num:"))
	n4 = int(input("next num:"))
	n5 = int(input("next num:"))
	n6 = int(input("next num:"))
	n7 = int(input("next num:"))

	
	sum = n1 + n2 + n3 + n4 + n5 + n6 + n7
	
	#if user says sum:
	if choice == "sum":
		print("the sum is",sum)
	elif choice == "average": # they wanted the average
		avg = sum / count
		print ("the average is", avg)
else:
	print ("I didn't recognize that operation.")	


print ("thanks! goodbye.")
	