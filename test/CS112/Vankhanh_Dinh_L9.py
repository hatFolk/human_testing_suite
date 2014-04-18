#Name: Vankhanh Dinh
#Section: X02
#Date: 7/17/2013
#Lab: 9

def sum_just_evens(xs):
	"""
Task 1. Write a function named sum_Just_evens. It accepts a list of integers as 
its only parameter, calculates the sum of all even integers found in the list,
and returns that value.
	"""
	sum = 0
	for i in xs:
		if i % 2 == 0:
			sum += i
	return sum

def remove_odds(xs):
	"""
Task 2. Write a function named remove_odds. It accepts a list of integers as its
only parameter and removes the odd numbers from the list. This function returns
the None value, and all modifications on the list must happen in-place.
	"""
	i = 0
	while i < len(xs):
		while xs[i] % 2 == 1:
			del xs[i]
		i += 1
	print(xs)
def main():
	"""
Task 3. Write a function named main. It must call your sum_just_evens function
with a list that has both evens and odds in it, printing out the result.
It then will create a list of integers, and store it to a variable named xs;
call remove_odds on that list; and then print out the contents of xs, so that we
can see by the printout that odds have actually been removed. Lastly, have your
Python file call main, to set everything in motion.
	"""
	xs = [0,1,2,3,4,5,6,7,8]
	print(sum_just_evens(xs))
	xs = [1,3,5,2,4,6]
	remove_odds(xs)
main()
