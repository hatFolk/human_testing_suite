# ask how many nums, store that many supplied nums in a list.

n = int(input("how many nums?"))

xs = [ ]
for _ in range(n):
	next = int(input("next num: "))
	xs.append(next)

print ("all your numbers: ",xs)


sum = 0
for x in xs:
	sum += x

print ("the sum of them is:",sum)


evens = 0
for x in xs:
	if x %2==0:
		evens += 1

print ("there are",evens,"evens in the list.")
