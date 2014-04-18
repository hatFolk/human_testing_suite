# Functions example where the functions return 


# draw a fancy M.
def getM():
    val  = "     ___   ___ \n"
    val += "    /   | /   |\n"
    val += "   / /| |/ /| |\n"
    val += "  / / |   / | |\n"
    val += " / /  |__/  | |\n"
    val += "/_/         |_|\n"
    return val
    
# draw a sort-of fancy A.
def getA():
    val  = "     ___ \n"
    val += "    /   |\n"
    val += "   / /| |\n"
    val += "  / ___ |\n"
    val += " / /  | |\n"
    val += "/_/   |_|\n"
    return val
    
# draw a fancy S.
def getS():
    val  = "    ______\n"
    val += "   / ____/\n"
    val += "  / /___  \n"
    val += " /____  | \n"
    val += " ____/ /  \n"
    val += "/_____/   \n"
    return val

# draw a boxy O.
def getO():
    val  = "     ______ \n"
    val += "    / ___  |\n"
    val += "   / /  / / \n"
    val += "  / /  / /  \n"
    val += " / /__/ /   \n"
    val += "|______/    \n"
    return val

# draw a fancy N.
def getN():
    val  = "     ___     __\n"
    val += "    /   |   / /\n"
    val += "   / /| |  / / \n"
    val += "  / / | | / /  \n"
    val += " / /  | |/ /   \n"
    val += "/_/   |___/    \n"
    return val

# draw a nice fat space.
def getSpace():
    val = "\n\n\n\n"
    return val

# define what our program should actually do when run.
def main():
    output  = getM()
    output += getA()
    output += getS()
    output += getO()
    output += getN()
    output += getSpace()
    print (output)


# actually run our program by calling the main() function.
main()    



# MODS and Qs:

# are all those val variables (named val) the same? Why or why not?
# (what is a 'local' variable?)

# move one of the return statements up a few lines. 
# What happens?

# print MASON out 25 times. (Use your sequence ops so that
# you don't have to type a lot!)

# ask the user how many times to print out MASON, and then
# do so.

# When we change what the program does, what part of the code
# do we tend to edit: main(), or the individual functions?

