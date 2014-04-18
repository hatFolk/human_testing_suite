# while-loop example.  Tests for how "odd" a number is
# (for a new definition of odd).


# -----------------------------------------------------
# ALGORITHM:
# keep dividing an integer by two, until it reaches 1.
# Before each division, if the current value is odd,
# add one to its oddness.
# -----------------------------------------------------
# PSEUDOCODE:
# 
# BEGIN
#   get number from user
#   oddness = 0
#   LOOP while num is still > 0
#      if num is odd:
#         increase oddness by one.
#      divide num by 2 (integer division).
#   END LOOP
#   print out how odd the number was.
# END
# 
# -----------------------------------------------------

# get a number from the user after printing a helpful message.
print ("\n\nI will tell you just how odd a number is.")
num = int (input("What is the number? "))
original_num = num

# start with an oddness of zero.
oddness = 0

# keep looping as long as num is >0 (at which 
#point integer division would just give back zeroes).
while (num>1):
    # only increment oddness when num is
    # odd. (when num%2 == 1))
    if (num%2==1):
        oddness +=1
    # each time in the loop, int-divide num by two.
    num = num // 2
# the loop ends here.

# print out the results.
print ("the number "+str(original_num)+\
       " has an oddness value of "+str(oddness)+"."\
      )

#MODS:

# given that we're dividing by two, there's probably a relation
# to binary.  Can you figure out another meaning of the results
# in relation to the binary representation? (tough question)


