#count the a's.

string = input("what is the string? I'll count the a's for you: ")


num_as = 0
num_chars = 0
for char in string:
	if char=="a":
		num_as += 1
	num_chars += 1

print ("the number of a's was: ", num_as)
print ("the number of characters was: ", num_chars)
