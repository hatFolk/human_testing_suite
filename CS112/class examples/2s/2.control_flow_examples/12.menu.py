print ("Welcome to Menu Selector")
print ()
print ("Select an option below:")
print ("  1 - Print OK")
print ("  2 - Exit")
print ()

option = 0

while (option!=2):
    option = int(input ("Enter option: "))
    
    if option==1:
        print ("OK")
    elif option==2:
        print ("Good Bye!")
    else:
        print ("Error! Incorrect option, please try again.")


# MODS:

# make this file a proper module by putting all the code
#  into a main function, and then calling main.

# add another option to print "That was fun!"
