#checks whether a given number is prime or not by 
# checking divisiblilty by all smaller numbers.

num = int(input("enter a positive number to see if it is prime: "))

# has_divisor is a "flag" that starts False, and 
# only turns True when some condition is found.

has_divisor = False
divisor = ""

# check all possible divisors, updating has_divisor flag if necessary.
for i in range(2,(num//2) + 1):
    if (num % i) == 0 :
        has_divisor = True
        divisor = i
        break

# report to the user what we found out.
if has_divisor:
    print (str(num)+" is NOT prime. (ex: "+str(divisor)+")")
else:
    print (str(num)+" IS prime.")





#MODS and Qs:

# Q: why does the range start at 2?

# print out an example divisor when the number is not prime.

# check that the number is positive before searching for a 
# divisor.  If the number isn't, then skip the search.

# Find a tighter bound on the range for the for-loop, based
# on which numbers could be divisors.

