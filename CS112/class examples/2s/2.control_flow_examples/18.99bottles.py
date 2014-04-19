# write out the lyrics to "99 bottles of beer on the wall"
# using a loop to simplify the process.



for num_bottles in range(99,0,-1):
	
	print(str(num_bottles)+" bottle", end="")
	if num_bottles!=1:
		print("s",end="")
	
	print(" of beer on the wall, "+str(num_bottles)+" bottle",end="")
	if num_bottles!=1:
		print("s",end="")
	
	print(" of beeeeer,"+ " you take one down, pass it around, "\
		+str(num_bottles-1)+" bottle",end="")

	if (num_bottles-1)!=1:
		print("s",end="")
	print(" of beer on the wall.")




print ("call an ambulance. ")

exit()




for i in range(99,0,-1):
    print (i,"bottles of beer on the wall,",i,"bottles of"\
               +" beeeeer --\n you take one down, pass it "\
               +"around,",(i-1),"bottles of beer on the wall.")

print ("""Closing time.  You don't have to go home, but you can't stay here!""")


# MODS and Qs:

# now write the lyrics to "999 bottles of beer on the wall".

# what happens if we leave out the `range' function name?
# (e.g., for i in (99,1,-1): )
