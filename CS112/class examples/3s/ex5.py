
n = int(input("what is the number? "))


is_prime = True
#num_divisors = 2

for val in range(2,n):
	if n%val==0:
		#print (val,"divides",n)
		#num_divisors += 1
		is_prime = False
		break


if is_prime:
	print ("yes, it is prime!")
else:
	print ("no, it's composite.")
