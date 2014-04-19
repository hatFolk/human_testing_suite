print ("Welcome to Menu Selector" )
print ()   
print ("Select an option below:" )
print ("   1 - Print OK" )
print ("   2 - Exit")
print ()  

# anything that isn't 2... our 'dummy' value.
option = 0

while option != 2:      
	option = int(input("Enter option: ") )
	if option == 1:            
		print ( "OK" )
	elif option == 2:            
		print ( "Good Bye!" )
	else:            
		print ("Incorrect option, try again.")
print ("done.")
