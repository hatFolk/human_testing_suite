
# find index of maximum value in list




xs = [4,6,7,5,3,5,5,3,31,2,3,1]


maxVal = xs[0]
for val in xs:
	if val > maxVal:
		maxVal = val

print("maximum value is:", maxVal)

#max_ind = 0
#indexCounter = 0
#for x in xs:
#	if maxVal==x:
#		max_ind = indexCounter
#		break
#	indexCounter += 1

for i in range(len(xs)):
	if maxVal == xs[i]:
		max_ind = i
		break
	
print ("maximum value is at index "+str(max_ind))

print ("fused version:")

max_ind = 0
for i in range(len(xs)):
	if xs[i] > xs[max_ind]:
		max_ind = i

print ("index of maximum value is:",max_ind)
	









