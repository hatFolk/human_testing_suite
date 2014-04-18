# factorial calculates n!, where n is given by the user. 
#
# n! = n*(n-1)*(n-2)*...*3*2*1.


# (Answer Below.....)


num = int(input("enter a number: "))

fac = 1
for val in range(1, num+1):
    fac *= val

print ("\n"+str(num)+"! = "+str(fac)+"\n\n")


# MODS:

# report an answer of 1 for all negative numbers and 0.
