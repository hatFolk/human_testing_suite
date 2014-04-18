
def main():
    print ("Welcome to Menu Selector 9000!!\n\n" + "  1 - Enter number\n  2 - Exit\n")
    
    option = 0
    
    while option !=2:
        option = int(input ("Enter option:"))
        if option==1:
            print ("The number entered is:" + input("Enter a number:"))
        elif option==2:
            print ("Good Bye!")
        else:
            print ("Incorrect option, try again...")

main()


#MODS:

# un-inline the input call to improve readability.  This
# is a trade-off for compactness, and your tastes may vary.

# Right now, the exit option is HARDCODED as a 2.  Use a variable
# instead. (Under what circumstances will this help you?)
