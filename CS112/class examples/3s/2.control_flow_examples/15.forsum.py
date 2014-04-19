# for-loop example that calculates the sum of a range of numbers.


print ("I will sum up the numbers from 0 to your number.\n")
num = int(input ("what is your number? "))

sum = 0

for i in range(num+1):
    sum += i
    #print("\tsum so far: " + str(sum))

print ("\nthe sum is",sum,".\n")


# MODS:

# notice there is no printing inside the loop.  Once our
# code gets more complex, printing will stop being *most*
# of what we do.

# also calculate the average.

# add branching control code to ask the user whether 
# they want the sum, or want the average. (How will you
# determine their choice?  This is a design decision).

# make the code print numbers in descending order.
# (hint: there are two main ways to do this...)
