# ask for the radius of a circle, and report back the area (=pi*r*r) and the circumference (=2*pi*r).

# this line lets us use math.pi instead of typing 3.14159...
import math

# get a number from the user by calling the input function.  Assign that number to a variable named radius.
radius = float(input ("what is the radius of the circle?"))

# assign values to variables area and circumference, using the value for radius that the user gave us.
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# print out useful information.
print ("\tthe circle's area is: " +str(area))
print ("the circle's circumference is: " + str(circumference))


#MODIFICATIONS:
# use tabs to make the output slightly more visually pleasing.
# how could we perform the task without using variables for area and circumference?
# what if we used raw_input instead of input? (what would need to happen for the code to still work?)

