# If-control-structure example.

# ask the user how many apples they want.
wanted_amount = int(input("how many apples would you like?"))

# state how may apples we have.
num_apples_available = 12

# start off by assuming we have enough apples for them.  It's not
# necessarily correct yet, but we'll check to make sure in a moment.
numGiven = wanted_amount

# if they wanted too many, though, we can only give
# them all that we have available.
if (wanted_amount > num_apples_available):
    numGiven = num_apples_available
    print ("We don't have that many apples...")


# at this point, numGiven is the correct answer.
# We can use it for printing.

print ("You are getting " + str(numGiven)+" apples.")

# Comments:

# if-stmts by themselves are somewhat rare; they are
# more commonly used in a larger context to find some
# special corner case that must be addressed.  We will
# see if-else-stmts soon, which are perhaps more
# common by themselves.
