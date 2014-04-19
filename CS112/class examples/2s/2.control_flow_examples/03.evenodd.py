# if-else control structure.

print ("welcome to the Even-Odd program.")

# get an integer from the user.
number = int(input("please type an integer: "))

# figure out if the number is even, using the mod (%) operator.
# (it is the 'remainder' operator).
is_even = (  (number % 2)  ==  0);

# if-else control structure: when is_even is True, the first 
# print statement is run and the second is not.  When is_even
# is False, the first print statement is skipped and the second
# one is run.
if (is_even):
    # this only occurs when is_even is True.
    print ("the number " + str(number) + " is even.")
else:
    # this only occurs when is_even is False.
    print ("the number " + str(number) + " is odd.")

print ("thanks for using the even-odd program!")


# MODIFICATIONS:

# instead of using the is_even variable, place the boolean expression
# directly in the if-else statement.

# only print "even" or "odd" in the `branches' of the if-statement 
# (so we don't have duplicate printing text in both branches).

# don't print anything at all inside the if-else block, but still
# end up doing the same thing.  (How?)

# ask the user for two numbers, and tell them if the first is 
# divisible by the second.
