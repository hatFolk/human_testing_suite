# function example: these functions have no inputs (parameters),
# and they don't return values either (no "return val" statements).
# But they do useful 'work' by printing stuff.  Later on, we'll have
# variables that are visible in multiple functions, and could have 
# side-effects other than printing (such as updating a variable).

# draw a fancy M.
def drawM():
    print ("     ___   ___ ")
    print ("    /   | /   |")
    print ("   / /| |/ /| |")
    print ("  / / |   / | |")
    print (" / /  |__/  | |")
    print ("/_/         |_|")

# draw a sort-of fancy A.
def drawA():
    print ("     ___")
    print ("    /   |")
    print ("   / /| |")
    print ("  / ___ |")
    print (" / /  | |")
    print ("/_/   |_|")

# draw a fancy S.
def drawS():
    print ("    ______")
    print ("   / ____/")
    print ("  / /___")
    print (" /____  |")
    print (" ____/ /")
    print ("/_____/")

# draw a boxy O.
def drawO():
    print ("     _______")
    print ("    / ___  /")
    print ("   / /  / /")
    print ("  / /  / /")
    print (" / /__/ /")
    print ("/______/")

# draw a fancy N.
def drawN():
    print ("     ___     __")
    print ("    /   |   / /")
    print ("   / /| |  / /")
    print ("  / / | | / /")
    print (" / /  | |/ /")
    print ("/_/   |___/")

# draw a nice fat space.
def drawSpace():
    print ("\n\n\n\n")


# define some ascii-text as our main function.
def main():
    drawM()
    drawA()
    drawS()
    drawO()
    drawN()
    drawSpace()

# call the main function
main()

#MODS:

# use these letters to print some anagram (a message 
# that uses the letters in a different order).
# --> wasn't that nicer than cut-pasting lots of prints?

# NOTE: since these functions do not explicitly return values (they
# just return control), we see the function calls on lines
# by themselves. Control flows 'into' the function call,
# through the body of the function, and 'out' back to the 
# call-site, where that original location keeps running.
