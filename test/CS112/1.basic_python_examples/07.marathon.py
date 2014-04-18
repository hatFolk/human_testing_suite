# calculates the number of feet and inches in a marathon.

numMiles = 26.2
numFeet = 5280 * numMiles
numInches = numFeet * 12

output = " a marathon (" + str(numMiles)+" miles) has "
output = output + str(numFeet) + " feet"
output += ", which is " + str(numInches) + " inches."

print (output)

# MODIFICATIONS:
# format the printed output onto multiple lines.
# one inch = 2.56 centimeters.  Report how many _meters_ are in a marathon.

