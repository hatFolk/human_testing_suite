#-------------------------------------------------------------------------------
# Name: Vankhanh Dinh
# Project 5
# Section X02
# Due Date: Friday, July 26th 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Piazza, Documentation
#-------------------------------------------------------------------------------
# Comments and assumptions: Assumes all files are CSV format files as discussed
# in class.
# Made assumptions on how to handle Exceptions for Extra Credit, Crashproof.
# Also formatted for extra credit.
# The format method is now my best friend. <3
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

def menu(current): # Serves as a menu
	choice = -1 # Ensures the reprinting of the menu upon usage or input fail.
	while choice not in range(11):
		print("""0  - clear out current inventory
1  - open inventory book
2  - store current inventory to file
3  - add entry (including quantity)
4  - remove current entry
5  - update quantity (of current entry)
6  - select entry by ID#
7  - select entry by name
8  - show all entries by name
9  - show all entries by ID
10 - quit
""")
		print("Current item: "+isselected(current)) #Checks to see if there is
		try: 										# Something selected.
			choice = int(input("Choice? > ")) # Pick an option.
		except ValueError:
			pass # Handled below
		if choice not in range(11): # If it isn't valid, try again.
			print("Good choice. Not. Try again.")
	return choice # Return that integer choice. (See main)
def isselected(current): # Changes "Current item:"
	a = current #Shortening var.
	if len(current) != 0: # Picks a string to be selected.
		return "ID#{0[0]}, {0[1]}. {0[2]} available, at ${1:.2f}".format(a, a[3]/100)
	else:
		return "None selected" # Your default, is of course, Nothing.

def openbook(book): # Finds a .csv file gets the csv.
	filename = input("What's the filename you want to upload? > ")
	try:
		f = open(filename, 'rU') # Find a file.
	except IOError: #Python2 considers this a NameError, but will not budge.
		print("sorry, file not found.\n")
		return book # Returns the previously used book. No change.
	book = {} # Else, new book made.
	for line in f.readlines(): #Ease of use.
		a = fixline(line[:len(line)-1]) # Cut the newline. Format
		book[a[0]] = a[1:] #ID is key, list of other values for value. 
	f.close()
	del book["id"] #Not necessary. Will be readded for saving.
	print("Book opened! You are now working with "+filename+".\n")
	return book #Delivering your book

def fixline(a): # Fixes line to be ready for changing.
	a = a.split('","') # Used in reading the csv. Splits around quotes comma.
	i = 0
	while i < len(a):
		for j in a[i]:
			if j == '"': # Gets rid of any unnecessary quotation.
				a[i] = a[i].replace(j,"")
		if a[i].isdigit() or a[i][0] == "-": #Checks for +/- number
			a[i] = int(a[i]) #Cast to int.
		i += 1 # Iterate
	return a # Gives back the line

def savebook(book):
	filename = input("Save your book? What's the filename? > ")
	if not(filename.endswith(".csv")):
		filename += ".csv" # Just makes it proper. .txt is also fine, really.
	f = open(filename, 'w') # Make the file. Add header.
	f.write(('"{}",'*4)[:-1].format("id","name","quantity","price")+"\n")
	for k,v in book.items(): #Write the products in line by line.
		f.write(('"{}",'*4)[:-1].format(k,v[0],v[1],v[2])+"\n")
	f.close() # Close the file to save.
	print("Done! Go view your new csv!\n") #Dict-to-CSV done!	

def addentry(book): #Simple. Add an entry to your inventory.
	newid = 1 if book == {} else (max(book.keys()) + 1) # ID is highest ID + 1
	newprod = input("Name of your new product? > ") # Get the name.
	newquan = getgoodans("How many do you have? > ") # Get the quantity.
	newpric = getgoodans("How much is it (in pennies?) > ") # Get the price
	book[newid] = [newprod,newquan,newpric] # Put everything in.
	print("Added!: ID# {}, Product {}, Quantity {}, at ${:.2f}".format(newid,
												newprod, newquan, newpric/100))
	return book

def getgoodans(string, a = ""):
	"""Makes sure that answer is valid."""
	while not(a.isdigit()) or a[0] == "-": # Allows for negative number.
		a = input(string)
		if not(a.isdigit()) or a[0] == "-": # Get the string. If invalid...
			print("Invalid response.") # <--
	return int(a) # Returns the int.

def removecurrent(current, book):
	if current == []: # Do no change if nothing is here
		print("Make sure you've selected something first.\n")
	else:
		del book[current[0]] # Remove that and clear the selection.
		current = []
		print("It has been removed. We shall not speak of it.\n")
	return current, book # Return the (non)changes.

def updatecurrent(current, book):
	if current == []: # Do no change if nothing is here
		print("Make sure you've selected something first.\n")
	else:
		print(isselected(current)) # Lets you know what's there already.
		q = getgoodans("What do you want to update the quantity to? > ")
		current[2] = q # Changes the price.
		book[current[0]][1] = current[2] # Updates it in dictionary.
		print("Updated!\n")
	return current, book

def selectid(current, book):
	lookup = input("Give me the ID# you'd like to look up > ") # Get ID
	ids = []
	for k in book:
		if str(k).startswith(lookup):
			ids.append(k)	# Find the IDs that start with the lookup
	if ids == []:
		print("sorry, no matches found.\n") # Nothing here.
		return current
	else:
		ids.sort() # Sort the IDs from small to big.
		nids = list(ids) # Copy a new list to be used as reference.
		choiceformat(ids, book) # Print the table with choices.
		i = 0
		while i not in range(1,len(nids)+1): # Get the choice
			i = getgoodans("Please choose a choice > ")
			if i not in range(1, len(nids)+1):
				print("Invalid choice.")
		current = [nids[i-1], book[nids[i-1]][0], book[nids[i-1]][1],
					book[nids[i-1]][2]] # Update the current
		print("Current selected.\n")
		return current # Give current back

def selectname(current, book):
	lookup = input("Give me the name to lookup > ") # Get the name
	sortlist = sorted(book.values())
	ids = []
	for k, v in book.items(): # If name starts with lookup
		if v[0].startswith(lookup):
			ids.append(k) # Append it to the list
		else:
			sortlist.remove(v) #Else, remove it. (sortlist is already sorted)
	if ids == []: 
		print("sorry, no matches found.\n") # End function if empty.
		return current
	else:
		nids = []
		for k, v in book.items(): # Gets ids in order.
			if v == sortlist[0]:
				nids.append(k)
		ids = list(nids) # Makes a copy for reference.
		choiceformat(nids, book) # Print the table of choices
		i = 0 
		while i not in range(1, len(ids)+1):
			i = getgoodans("Please choose a choice. > ") # Choose index of ids
			if i not in range(1, len(ids)+1):
				print("Invalid choice.")
		current = [ids[i-1], book[ids[i-1]][0], book[ids[i-1]][1],
					book[ids[i-1]][2]] # Update current
		print("Current selected.\n")
		return current # Give current back

def showname(book): # Shows the whole inventory in Ascii-betical
	sortlist = sorted(book.values())
	ids = []
	i = 0
	while sortlist != []: # Sort through the list
		for k,v in book.items():
			if sortlist == []: # If it is empty, break
				break
			if v == sortlist[0]: # If it matches up, add the id and remove val
				ids.append(k) # From ids and sortlist respectively.
				sortlist.remove(v)
	printformat(book, ids) # Print the table

def showid(book): # Straightforward.
	ids = sorted(book.keys())
	printformat(book, ids) # Print the table

def dicttolist(book, ids):
	temp = [] # Makes dictionaries into list
	for k, v in book.items():
		if k in ids: # Filters out the unnecessary ids.
			temp.append([k, v[0], v[1], v[2]])
	return temp # Returns the list.

def stringlist(temp): # Stringifies the list.
	# m, n, y, z will represent the max length of columns 0, 1, 2, 3.
	m = n = y = z = 0
	for i in temp:
		i[0] = str(i[0])
		i[2] = str(i[2])
		i[3] = "$" + "{:.2f}".format(i[3]/100) # For the price
		if m < len(i[0]): m = len(i[0])
		if n < len(i[1]): n = len(i[1])
		if y < len(i[2]): y = len(i[2])
		if z < len(i[3]): z = len(i[3])
	m = 6 if m <= 2 else m + 4 # length has to be at least len(ID) + 4
	n = 8 if n <= 4 else n + 4 # length has to be least len(name) + 4
	y = 8 if y <= 8 else y + 4 # length has to be at least len(quantity) + 4
	z = 9 if z <= 5 else z + 4 # length has to be at least len(price) + 4
	clength = [m,n,y,z] # Record these and put into a list
	return clength, temp # return the list and the stringified list

def printformat(book, ids): # Prints the table, non-choosing (option 8, 9)
	temp = dicttolist(book, ids) # Makes the dictionary to a list
	clength, temp = stringlist(temp) # Gets len. of column and string'd list
	print("{0: >{4}}    {1: <{5[1]}}{2: >{5[2]}}{3: >{5[3]}}".format("ID",
		"name", "quantity","price",clength[0]-4, clength)) # Plug in the header 
	print("-"*(sum(clength))) # Print the separator line
	while ids != []: # print from ids[0] until empty
		for j in temp:
			if ids == []: 
				break
			if ids[0] == int(j[0]): # Prints the first element of ids[0] + info
				print(
		"{0[0]: >{1}}    {0[1]: <{2[1]}}{0[2]: >{2[2]}}{0[3]: >{2[3]}}"
				.format(j,clength[0]-4, clength))
				ids.remove(ids[0]) # Remove the first element of ids[0]

def choiceformat(ids, book): # Prints the table for choosing (Option 6,7)
	temp = dicttolist(book, ids) # Make the dictionary to a list
	for i in temp:
		if i[0] not in ids:
			temp.remove(i) # Removes the irrelevant ids
	a = max(len(ids), 6) # The max len of the choices col.
	clength, temp = stringlist(temp) # Get the length of the other columns
	clength.insert(0, a) # Put the choice column length at the front
	print("{0:>{5[0]}}{1:>{5[1]}}    {2:<{5[2]}}{3:>{5[3]}}{4:>{5[4]}}"
			.format("choice", "ID", "name", "quantity", "price", clength))
	print("-"*(sum(clength)+4)) # print the header
	i = 1
	while ids != []: # Continue until empty.
		for j in temp:
			if ids == []:
				break
			if ids[0] == int(j[0]): # Print the info for the first ids.
				print(
	"{0: >{2[0]}}{1[0]: >{2[1]}}    {1[1]: <{2[2]}}{1[2]: >{2[3]}}{1[3]: >{2[4]}}"
				.format(i, j,clength)) # index and information
				ids.remove(ids[0]) # remove the first index
				i += 1 # Get the next number
	
def main():
	choice = book = {} # Just need to initialize choice to something.
	current = [] # Holds selected entry (change in option 6, 7)
	while choice != 10:
		choice = menu(current) # Get appropriate choice
		if choice == 0:
			book.clear() # Only needs to clear the book.
			current = []
			print("The book is cleared. You can add entries and build a new "+\
					"book from scratch\nor upload a new inventory csv.")
		if choice == 1:
			book = openbook(book) # Gives you a book to work with
		if choice == 2:
			savebook(book) # Saves your current book
		if choice == 3:
			book = addentry(book) # Add a new entry to the dictionary.
		if choice == 4:
			current, book = removecurrent(current, book) # Deletes selected
		if choice == 5:
			current, book = updatecurrent(current, book) # Changes selected quant.
		if choice == 6:
			current = selectid(current, book) # Select selected by ID
		if choice == 7:
			current = selectname(current, book) # Select selected by name
		if choice == 8:
			showname(book) # Prints entries ascii-betically
		if choice == 9:
			showid(book) # Prints entries ID-lowest to highest
		print() #Puts some space between everything.
	print("Bye!") # Say bye (option 10 was chosen)
if __name__ == "__main__": main()
