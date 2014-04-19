# factorial calculates n!, where n is given by the user. 
#
# n! = n*(n-1)*(n-2)*...*3*2*1.

n = int(input("fact(n) calculator: "))

total = 1

for val in range(1,n+1):
	total = val * total
print(str(n)+"! = ", total)

# MODS:

# report an answer of 1 for all negative numbers and 0.
