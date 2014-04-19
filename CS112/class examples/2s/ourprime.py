# ourprime

n = int(input("enter the number: "))


# print ("will check divisors from: ", list(range(2, n, 1)     ))


#for divisor in range(2,n,1):
#	if  n%divisor == 0 :
#		# we found a divisor! It isn't prime.
#		print ("\t"+str(divisor)+" divides it.")
#		is_prime = False
#		break


is_prime = True
divisor = 2
while is_prime==True and divisor <n:
	if n%divisor==0:
		print ("\t"+str(divisor)+" divides it.")
		is_prime = False
	divisor += 1		




print ("is ",n,"prime? ", is_prime)




