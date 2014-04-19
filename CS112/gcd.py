# 12, 6 | 6 is the answer.

def gcd(a, b):
	if b == 0: # if b==0, return a
		return a
	newa = b # Else, make a = b
	newb = a%b # and b = a%b
	return gcd(newa, newb) # Check if b == 0. Repeat.


