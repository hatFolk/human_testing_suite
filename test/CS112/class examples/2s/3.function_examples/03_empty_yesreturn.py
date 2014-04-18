# This function example has no parameters, but DOES return a value.
# so we do see "return blah" statements in the function definition.


def alwaysA5():
    print ("\t--> alwaysA5 running: time to get a five!")
    return 5


def main():
    print ("* main is starting...")
    what_we_got = alwaysA5()
    print ("* main is back!")
    print ("* What we got was a "+str(what_we_got)+".")

main()


# MODS: 

# use alwaysA5 as an inline function call, instead
# of using the what_we_got variable.  Does this 
# affect the order of printing stuff?  Why?

